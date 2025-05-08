import pandas as pd
from prophet import Prophet
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

def train_and_forecast():
    # Carregar os dados do Brent a partir do arquivo CSV
    df_brent = pd.read_csv('data/tabela_extraida.csv', sep=',')
    df_brent.columns = ['Data', 'Preço Brent FOB (US$/barril)']

    # Limpar e ajustar os dados
    df_brent['Data'] = pd.to_datetime(df_brent['Data'], format='%d/%m/%Y')
    df_brent['Preço Brent FOB (US$/barril)_Corrigido'] = df_brent['Preço Brent FOB (US$/barril)'].str.replace(',', '.').astype(float)
    df_brent.drop(columns=['Preço Brent FOB (US$/barril)'], inplace=True)

    # Ajustar os dados para o Prophet
    df_brent_prophet = df_brent[['Data', 'Preço Brent FOB (US$/barril)_Corrigido']].copy()
    df_brent_prophet.columns = ['ds', 'y']

    # Treinar o modelo Prophet otimizado
    year = 2000  # Ano inicial para treinamento
    df_brent_prophet['year'] = df_brent_prophet['ds'].dt.year

    df_prophet_model = Prophet(
        changepoint_prior_scale=0.5,
        seasonality_prior_scale=0.01,
        n_changepoints=50
    )
    df_prophet_model.fit(df_brent_prophet.query(f'year >= {year} and year < 2025'))

    # Criar previsões para os próximos 90 dias
    df_brent_forecast = df_prophet_model.predict(df_prophet_model.make_future_dataframe(periods=90))
    df_brent_forecast = df_brent_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    df_brent_forecast['year'] = df_brent_forecast['ds'].dt.year

    # Filtrar previsões para 2025
    df_brent_forecast_25 = df_brent_forecast.query('year >= 2025').drop(columns=['yhat_lower', 'yhat_upper'])

    # Combinar os dados reais com as previsões
    df_brent_forecast_25 = df_brent.merge(
        df_brent_forecast_25,
        left_on='Data',
        right_on='ds',
        how='inner'
    )

    # Remover as colunas que não são mais necessárias
    df_brent_forecast_25.drop(columns=['ds'], inplace=True)

    return df_brent_forecast_25

def evaluate_model(df_brent_forecast_25):
    # Avaliar o modelo
    y_true = df_brent_forecast_25["Preço Brent FOB (US$/barril)_Corrigido"]
    y_pred = df_brent_forecast_25["yhat"]

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    wmape = np.sum(np.abs(y_true - y_pred)) / np.sum(y_true)

    return mae, rmse, wmape

def plot_results(df_brent_forecast_25):
    # Plotar os resultados
    df_brent_forecast_25.sort_values('Data', inplace=True)

    plt.figure(figsize=(12, 6))
    plt.plot(df_brent_forecast_25['Data'], 
             df_brent_forecast_25["Preço Brent FOB (US$/barril)_Corrigido"], 
             label='Preço Real', color='blue')
    plt.plot(df_brent_forecast_25['Data'], 
             df_brent_forecast_25['yhat'], 
             label='Previsão (yhat)', color='red', linestyle='--')

    plt.xlabel('Data')
    plt.ylabel('Preço (US$/barril)')
    plt.title('Comparação entre Preço Real e Previsão do Modelo')
    plt.legend()
    plt.grid(True)
    plt.show()