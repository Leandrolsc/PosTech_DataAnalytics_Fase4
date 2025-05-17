import streamlit as st


def exibir():
    st.title("Dashboard")
    st.markdown("""
    O Dashboard apresenta uma visão geral dos dados extraídos do IPEA, permitindo ao usuário visualizar a evolução do preço do petróleo Brent ao longo do tempo.  
    A interface é interativa e permite explorar os dados de forma intuitiva.
    """)
    
    st.markdown("""
            <iframe title="Vendas v02" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNjgwYWVmNzQtMmMxYy00ZDE0LWI1OGEtNzI2NGZhYTEyYjA3IiwidCI6IjljOGEzMjFhLTcyNzktNDE5NS1hZjNkLTRjYmViMzY3YjA5ZSJ9" frameborder="0" allowFullScreen="true"></iframe>
            """,
    unsafe_allow_html=True
    )