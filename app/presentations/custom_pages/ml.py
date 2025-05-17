import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os
import altair as alt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from scrapping import GetIpeaDataPetroleo
from model import train_and_forecast, evaluate_model, previsao

def exibir():
    st.title("Machine Learning")
    # Treinar o modelo e obter previsões
    df_brent_forecast_25 = train_and_forecast()
    mae, rmse, wmape = evaluate_model(df_brent_forecast_25)
    st.write(f"**WMAPE:** {wmape:.4%}")
    st.write("Escolha o período para previsão:")
    periods = st.selectbox(
        "Selecione o número de dias para previsão:",
        options=[7, 15, 30, 45, 60, 90],
        index=0
    )
    # Obter previsões
    df_previsao = previsao(periods)

    # Converter a coluna de data para o tipo date
    df_previsao["ds"] = pd.to_datetime(df_previsao["ds"]).dt.date

    # Renomear colunas para nomes amigáveis
    df_previsao = df_previsao.rename(columns={
        "ds": "Data",
        "yhat": "Previsão",
        "yhat_lower": "Limite Inferior",
        "yhat_upper": "Limite Superior"
    })

    # Gráfico com faixa de confiança e linha da previsão
    st.write("**Gráfico com faixa de previsão:**")

    # Faixa de confiança sombreada
    faixa_confianca = alt.Chart(df_previsao).mark_area(
        opacity=0.25,
        color="#005B96"  # azul escuro translúcido
    ).encode(
        x=alt.X("Data:T", title="Data", axis=alt.Axis(labelAngle=45, format="%d/%m/%y")),
        y="Limite Inferior:Q",
        y2="Limite Superior:Q",
        tooltip=["Previsão:Q", "Limite Inferior:Q", "Limite Superior:Q"]
    )

    # Linha da previsão
    linha_previsao = alt.Chart(df_previsao).mark_line(
        color="#3399FF",  # azul claro
        strokeWidth=3
    ).encode(
        x=alt.X("Data:T", title="Data", axis=alt.Axis(labelAngle=45, format="%d/%m")),
        y=alt.Y("Previsão:Q", title="Valor Previsto", axis=alt.Axis(orient="right")),
        tooltip=["Data:T", "Previsão:Q", "Limite Inferior:Q", "Limite Superior:Q"]
    )

    # Combinar gráficos
    grafico = (faixa_confianca + linha_previsao).properties(
        width=1000,
        height=500,
        title="Previsão com Faixa de Confiança"
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_view(
        strokeOpacity=0
    )

    st.altair_chart(grafico, use_container_width=True)


    st.write("**Resultados das previsões:**")
    st.dataframe(df_previsao)

    ##Criar logo FP Petroleo
    ##Projetar 7/15/30/60/90 dias para frente
    ##Utilizar todo historico ou apenas 2022/2023/2024...