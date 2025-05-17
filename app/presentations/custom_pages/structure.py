import streamlit as st

def exibir():
    st.title("Estrutura do Projeto")

    st.markdown("""
    ```
    PosTech_FIAP_F4/
    ├── .streamlit/                # Configurações do tema e aparência do Streamlit
    ├── app/
    │   ├── data/                  # Dados extraídos do IPEA e metadados de extração
    │   ├── presentations/         # Interface Streamlit e páginas customizadas
    │   │   └── custom_pages/      # Páginas específicas: ML, Storytelling, Estrutura
    │   ├── use_cases/             # Lógica de negócio: modelos de ML e scraping
    │   └── __pycache__/           # Arquivos temporários do Python
    ├── notebooks/                 # Notebooks de exploração e modelagem
    ├── requirements.txt           # Dependências do projeto
    ├── README.md                  # Documentação principal
    └── .gitignore                 # Arquivos e pastas ignorados pelo Git
    ```
    """)

    st.subheader("Principais Componentes Utilizados")

    st.markdown("""
    - **Streamlit**: Framework para construção da interface web interativa.
    - **Pandas**: Manipulação e análise de dados tabulares.
    - **Plotly/Altair**: Visualização de dados com gráficos interativos.
    - **Prophet**: Modelo de previsão de séries temporais para estimar o preço futuro do Brent.
    - **BeautifulSoup/Requests**: Web scraping dos dados do IPEA.
    - **JSON**: Armazenamento de metadados sobre as extrações.
    """)

    st.subheader("Fluxo da Aplicação")

    st.markdown("""
    1. **Extração dos Dados**  
       Os dados históricos do preço do petróleo Brent são extraídos automaticamente do site do IPEA pelo módulo [`use_cases/scrapping.py`](../../use_cases/scrapping.py) e salvos em [`app/data/tabela_extraida.csv`](../../data/tabela_extraida.csv). Metadados da extração são registrados em [`app/data/metadata.json`](../../data/metadata.json).

    2. **Visualização e Download**  
       A página de storytelling ([`custom_pages/storytelling.py`](storytelling.py)) permite visualizar os dados, gráficos temporais e baixar o CSV atualizado.

    3. **Previsão com Machine Learning**  
       O módulo [`use_cases/model.py`](../../use_cases/model.py) utiliza Prophet para prever o preço do Brent. O usuário pode escolher o período de previsão na interface ([`custom_pages/ml.py`](ml.py)).

    4. **Interface Unificada**  
       Toda a navegação é feita pela interface principal ([`presentations/home.py`](../home.py)), que integra as páginas de storytelling, ML e estrutura do projeto.

    5. **Notebooks**  
       Os notebooks em [`notebooks/`](../../../notebooks/) foram utilizados para exploração, testes e validação dos modelos antes da implementação final.
    """)

    st.info("Consulte o README.md para mais detalhes sobre o projeto e instruções de uso.")