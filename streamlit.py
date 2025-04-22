import streamlit as st
import pandas as pd
import plotly.express as px
from scrapping import GetIpeaDataPetroleo

st.title("Visualização e Download de Dados")

csv_file = "tabela_extraida.csv"

# Botão para executar o script scrapping.py
if st.button("Atualizar Tabela"):
    try:
        # Executar o script scrapping.py
        data_fetcher = GetIpeaDataPetroleo()
        df = data_fetcher.fetch_data()
        
        if df is not None:
            # Salvar o DataFrame em um arquivo CSV
            data_fetcher.save_to_csv(df)
            st.success(f"Tabela atualizada e salva como '{csv_file}'.")
        else:
            st.error("Erro ao atualizar a tabela.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao executar o script: {e}")

try:
    df = pd.read_csv(csv_file)
    
    if "Data" in df.columns and "Preço - petróleo bruto - Brent (FOB)" in df.columns:
        # Converter a coluna "Data" para o formato datetime
        df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y", errors="coerce")
        
        # Remover linhas com valores inválidos
        df = df.dropna(subset=["Data", "Preço - petróleo bruto - Brent (FOB)"])
        
        # Converter a coluna de preços para float
        df["Preço - petróleo bruto - Brent (FOB)"] = df["Preço - petróleo bruto - Brent (FOB)"].str.replace(",", ".").astype(float)
        
        st.subheader("Gráfico Temporal")
        fig = px.line(
            df,
            x="Data",
            y="Preço - petróleo bruto - Brent (FOB)",
            title="Evolução do Preço do Petróleo Brent",
            labels={"Data": "Data", "Preço - petróleo bruto - Brent (FOB)": "Preço"},
        )
        st.plotly_chart(fig)
    else:
        st.error("O arquivo CSV não contém as colunas necessárias: 'Data' e 'Preço - petróleo bruto - Brent (FOB)'.")

    st.subheader("Dados do CSV")
    st.dataframe(df)

    st.subheader("Baixar Dados")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Baixar tabela_extraida.csv",
        data=csv,
        file_name="tabela_extraida.csv",
        mime="text/csv",
    )

except FileNotFoundError:
    st.error(f"O arquivo '{csv_file}' não foi encontrado.")
except Exception as e:
    st.error(f"Ocorreu um erro: {e}")