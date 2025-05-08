import streamlit as st
import pandas as pd
import plotly.express as px
from scrapping import GetIpeaDataPetroleo
from model import train_and_forecast, evaluate_model,plot_results
import json
import os

st.set_page_config(
    page_title="Análise do Preço do Petróleo Brent",
    page_icon=":oil_drum:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "https://github.com/Leandrolsc/PosTech_DataAnalytics_Fase4/issues",
        'About': """
        ## Sobre o Projeto
        Esta aplicação foi desenvolvida como parte do trabalho da Fase 4 da Pós Tech em Data Analytics na FIAP.  
        O objetivo é realizar uma análise do preço do petróleo Brent, utilizando dados históricos extraídos do IPEA.  
        """
    }
)

st.title("Análise do Preço do Petróleo Brent")
st.markdown("""
* Este projeto faz parte do trabalho da Fase 4 da Pós Tech em Data Analytics na FIAP.  
* O objetivo é realizar uma análise do preço do petróleo Brent, utilizando dados históricos extraídos do IPEA (Instituto de Pesquisa Econômica Aplicada).  
* A aplicação permite visualizar os dados, gerar gráficos temporais e realizar o download das informações em formato CSV. --Até o momento...
""")

# Criar as abas
tab1, tab2, tab3 = st.tabs(["Storytelling e download dos dados", "Machine Learning", "Estrutura do projeto"])

# Aba 1: Storytelling e download dos dados
with tab1:
    st.title("Storytelling e download dos dados")

    csv_file = "data/tabela_extraida.csv"
    metadata_file = "data/metadata.json"
    
    ultima_data_extracao = "Não disponível"
    if os.path.exists(metadata_file):
        try:
            with open(metadata_file, "r", encoding="utf-8") as json_file:
                metadata_list = json.load(json_file)
                if metadata_list:
                    ultima_data_extracao = metadata_list[-1]["data_extracao"]
        except Exception as e:
            st.error(f"Erro ao carregar o arquivo de metadados: {e}")

    try:
        df = pd.read_csv(csv_file)
        
        if "Data" in df.columns and "Preço - petróleo bruto - Brent (FOB)" in df.columns:
            # Converter a coluna "Data" para o formato datetime
            df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y", errors="coerce")
            
            # Remover linhas com valores inválidos
            df = df.dropna(subset=["Data", "Preço - petróleo bruto - Brent (FOB)"])
            
            datamaxima = df["Data"].max()
            dataminima = df["Data"].min()

            st.markdown(f"""Data de: **{dataminima.strftime('%d/%m/%Y')}** ate **{datamaxima.strftime('%d/%m/%Y')}**  
                        Total de registros: **{len(df)}**  
                        Dados extraidos do IPEA - Instituto de Pesquisa Econômica Aplicada  
                        Fonte: http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view  
                        Dados extraidos em: **{ultima_data_extracao}**
                        """)

            st.write("------")

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
        
        st.write("------") 

        st.subheader("Dados do CSV")
        st.write("")
        st.dataframe(df)

        st.subheader("Baixar Dados")
        st.write("")
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
    st.write("------") 

    # Botão para executar o script scrapping.py
    st.subheader("Atualizar Tabela")
    st.markdown(f"""
                Clique no botão abaixo para atualizar a tabela, caso esteja desatualizada.  
                **Antes de prosseguir, verifique a data da última extração exibida acima e confirme se há novos dados disponíveis na fonte oficial.**  
                Data da Ultima extração: **{ultima_data_extracao}**
                
                """)

    st.write("")

    if st.button("Atualizar Tabela caso esteja desatualizada"):
        try:
            # Executar o script scrapping.py
            data_fetcher = GetIpeaDataPetroleo()
            df = data_fetcher.fetch_data()
            
            if df is not None:
                # Salvar o DataFrame em um arquivo CSV
                data_fetcher.save_to_csv(df)
                st.success(f"Tabela atualizada e salva como '{csv_file}'.")
                st.rerun()  # Recarregar a página para mostrar os dados atualizados
            else:
                st.error("Erro ao atualizar a tabela.")
        except Exception as e:
            st.error(f"Ocorreu um erro ao executar o script: {e}")

# Aba 2: Machine Learning (vazia)
with tab2:
    st.title("Machine Learning")
    # Treinar o modelo e obter previsões
    st.write("Treinando o modelo e gerando previsões...")
    df_brent_forecast_25 = train_and_forecast()

    # Avaliar o modelo
    st.write("Avaliando o modelo...")
    mae, rmse, wmape = evaluate_model(df_brent_forecast_25)
    st.write(f"**MAE:** {mae:.4f}")
    st.write(f"**RMSE:** {rmse:.4f}")
    st.write(f"**WMAPE:** {wmape:.4%}")

    # Exibir os resultados
    st.write("**Resultados das previsões:**")
    st.dataframe(df_brent_forecast_25)

    # Plotar os resultados
    st.write("**Gráfico de Previsões:**")
    st.pyplot(plot_results(df_brent_forecast_25))


    ##Projetar 7/15/30/60/90 dias para frente
    ##Utilizar todo historico ou apenas 2022/2023/2024...

# Aba 3: Estrutura do Projeto (vazia)
with tab3:
    st.title("Estrutura do Projeto")
    st.write("Conteúdo em desenvolvimento.")