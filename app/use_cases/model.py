import pandas as pd
from prophet import Prophet
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

def train_and_forecast():
    # Carregar os dados do Brent a partir do arquivo CSV
    df_brent = pd.read_csv('app/data/tabela_extraida.csv', sep=',')
    df_brent.columns = ['Data', 'Preço Brent FOB (US$/barril)']

    # Converter a coluna de data
    df_brent['Data'] = pd.to_datetime(df_brent['Data'], format='%d/%m/%Y')

    # Corrigir valores de preço (vírgula para ponto) e converter para float
    df_brent['Preço Brent FOB (US$/barril)'] = df_brent['Preço Brent FOB (US$/barril)'].astype(str)
    df_brent['Preço Brent FOB (US$/barril)_Corrigido'] = df_brent['Preço Brent FOB (US$/barril)'].str.replace(',', '.', regex=False).astype(float)

    # Remover a coluna original
    df_brent.drop(columns=['Preço Brent FOB (US$/barril)'], inplace=True)

    # Preparar dados para o Prophet
    df_prophet = df_brent[['Data', 'Preço Brent FOB (US$/barril)_Corrigido']].copy()
    df_prophet.columns = ['ds', 'y']
    df_prophet['year'] = df_prophet['ds'].dt.year

    # Treinar o modelo Prophet
    model = Prophet(
        changepoint_prior_scale=0.5,
        seasonality_prior_scale=0.01,
        n_changepoints=50
    )
    model.fit(df_prophet.query('year >= 2022 and year < 2025'))

    # Criar previsões para os próximos 90 dias
    future = model.make_future_dataframe(periods=90)
    forecast = model.predict(future)
    forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    forecast['year'] = forecast['ds'].dt.year

    # Filtrar previsões para 2025
    forecast_2025 = forecast.query('year >= 2025').drop(columns=['yhat_lower', 'yhat_upper'])

    # Combinar previsões com dados reais (se houver)
    df_merged = df_brent.merge(
        forecast_2025,
        left_on='Data',
        right_on='ds',
        how='inner'
    ).drop(columns=['ds'])

    return df_merged

def evaluate_model(df_merged):
    # Avaliar o modelo
    y_true = df_merged["Preço Brent FOB (US$/barril)_Corrigido"]
    y_pred = df_merged["yhat"]

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    wmape = np.sum(np.abs(y_true - y_pred)) / np.sum(y_true)

    return mae, rmse, wmape

def previsao(dias=30):
    # Carregar os dados
    df_brent = pd.read_csv('app/data/tabela_extraida.csv', sep=',')
    df_brent.columns = ['Data', 'Preço Brent FOB (US$/barril)']

    # Converter datas e preços
    df_brent['Data'] = pd.to_datetime(df_brent['Data'], format='%d/%m/%Y')
    df_brent['Preço Brent FOB (US$/barril)'] = df_brent['Preço Brent FOB (US$/barril)'].astype(str)
    df_brent['Preço Brent FOB (US$/barril)_Corrigido'] = (
        df_brent['Preço Brent FOB (US$/barril)']
        .str.replace(',', '.', regex=False)
        .astype(float)
    )
    df_brent.drop(columns=['Preço Brent FOB (US$/barril)'], inplace=True)

    # Preparar dados para o Prophet
    df_prophet = df_brent[['Data', 'Preço Brent FOB (US$/barril)_Corrigido']].copy()
    df_prophet.columns = ['ds', 'y']

    #Filtro 2022 em diante
    df_prophet_filtrado = df_prophet[df_prophet['ds'].dt.year >= 2022] #Filtrei aqui por conta do tempo de processamento e dos outliers do dataframe original.
    # Treinar o modelo Prophet
    model = Prophet(
        changepoint_prior_scale=0.5,
        seasonality_prior_scale=0.01,
        n_changepoints=50
    )
    model.fit(df_prophet_filtrado)

    # Gerar previsões a partir da última data do histórico
    last_date = df_prophet['ds'].max()
    forecast_periods = dias  # dias futuros
    future = model.make_future_dataframe(periods=forecast_periods)
    future = future[future['ds'] > last_date]  # manter apenas datas futuras

    forecast = model.predict(future)
    forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    return forecast