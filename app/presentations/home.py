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
        O objetivo é realizar uma análise do preço do petróleo Brent, utilizando dados históricos extraídos do IPEA.  
        """
    }
)

with st.sidebar:
    escolha = option_menu("Menu", ["Home",
                                   "Storytelling e download dos dados", 
                                   "Machine Learning", 
                                   "Estrutura do Projeto"],
                          icons=['house', 'bar-chart', 'gear','book'], 
                          menu_icon="cast", 
                          default_index=0)
    
if escolha == "Storytelling e download dos dados":
    storytelling.exibir()
elif escolha == "Machine Learning":
    ml.exibir()
elif escolha == "Estrutura do Projeto":
    structure.exibir()
elif escolha == "Home":
    st.title("Análise do Preço do Petróleo Brent")
    st.markdown("""
    * Este projeto faz parte do trabalho da Fase 4 da Pós Tech em Data Analytics na FIAP.  
    * O objetivo é realizar uma análise do preço do petróleo Brent, utilizando dados históricos extraídos do IPEA (Instituto de Pesquisa Econômica Aplicada).  
    * A aplicação permite visualizar os dados, gerar gráficos temporais e realizar o download das informações em formato CSV.
    """)

    st.write("------")
    st.markdown("Link para o repositório do projeto: [GitHub - Leandrolsc/PosTech_DataAnalytics_Fase4](https://github.com/Leandrolsc/PosTech_DataAnalytics_Fase4)")
    st.write("------")





