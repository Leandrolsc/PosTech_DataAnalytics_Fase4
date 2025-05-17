import streamlit as st
import sys
import os
from streamlit_option_menu import option_menu

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from presentations.custom_pages import ml, storytelling, structure

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
        O objetivo é realizar uma análise do preço do petróleo Brent, utilizando dados históricos extraídos do IPEA (Instituto de Pesquisa Econômica Aplicada).  
        A aplicação permite visualizar os dados, gerar gráficos temporais, realizar previsões com Machine Learning e baixar as informações em formato CSV.
        """
    }
)

with st.sidebar:
    escolha = option_menu(
        "Menu",
        ["Home", "Storytelling e download dos dados", "Machine Learning", "Estrutura do Projeto"],
        icons=['house', 'bar-chart', 'gear', 'book'],
        menu_icon="cast",
        default_index=0
    )

if escolha == "Storytelling e download dos dados":
    storytelling.exibir()
elif escolha == "Machine Learning":
    ml.exibir()
elif escolha == "Estrutura do Projeto":
    structure.exibir()
elif escolha == "Home":
    st.title("Análise do Preço do Petróleo Brent")
    st.markdown("""
    Este projeto faz parte do trabalho da **Fase 4 da Pós Tech em Data Analytics na FIAP**.  
    O objetivo é realizar uma análise do preço do petróleo Brent, utilizando dados históricos extraídos do **IPEA (Instituto de Pesquisa Econômica Aplicada)**.

    A aplicação permite **visualizar os dados**, **gerar gráficos temporais**, **realizar previsões com Machine Learning** e **baixar as informações em formato CSV**.
    """)

    #Link powerbi:
    st.markdown("""
            <iframe title="Vendas v02" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNjgwYWVmNzQtMmMxYy00ZDE0LWI1OGEtNzI2NGZhYTEyYjA3IiwidCI6IjljOGEzMjFhLTcyNzktNDE5NS1hZjNkLTRjYmViMzY3YjA5ZSJ9" frameborder="0" allowFullScreen="true"></iframe>
            """,
    unsafe_allow_html=True
    )


    st.markdown("Repositório do projeto: [GitHub - Leandrolsc/PosTech_DataAnalytics_Fase4](https://github.com/Leandrolsc/PosTech_DataAnalytics_Fase4)")

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 0.95em;'>
        <b>Fase 4 da PosTech em Data Analytics da FIAP</b><br>
        Desenvolvido por: 
        <a href='https://www.linkedin.com/in/leandro-victor-silva-8a319b228/' target='_blank'><b>Leandro Victor Silva</b></a> e 
        <a href='https://www.linkedin.com/in/murilo-maioli-21195aaa/' target='_blank'><b>Murilo Maioli</b></a><br>
        Repositório do projeto: 
        <a href='https://github.com/Leandrolsc/PosTech_DataAnalytics_Fase4' target='_blank'>
           <b>GitHub - Leandrolsc/PosTech_DataAnalytics_Fase4</b>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)