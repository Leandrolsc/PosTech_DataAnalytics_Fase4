import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def exibir():

    st.title("Entenda o Preço do Petróleo")
    st.markdown("""
O petróleo é uma das commodities mais sensíveis às crises globais, sendo diretamente afetado por conflitos geopolíticos, recessões econômicas e pandemias. Ao longo da história, diversas crises moldaram o mercado petrolífero, provocando oscilações drásticas nos preços e afetando economias ao redor do mundo.

### Guerra do Golfo (1990-1991)
A Guerra do Golfo foi desencadeada pela invasão do Kuwait pelo Iraque, levando a uma intervenção militar liderada pelos Estados Unidos. O conflito gerou preocupações sobre o fornecimento de petróleo do Oriente Médio, uma região responsável por grande parte da produção global. Como resultado, os preços do petróleo dispararam, atingindo cerca de US\$ 41 por barril em 1990, após o fim do conflito.

### Crise dos Tigres Asiáticos (1997)
A crise financeira asiática de 1997 teve origem na Tailândia e rapidamente se espalhou para outros países do Sudeste Asiático. A recessão econômica resultante reduziu a demanda por petróleo, levando a uma queda nos preços. Durante a crise, o preço do barril caiu de US\$ 23 para cerca de US\$ 12, refletindo a menor demanda global.

### Crise Financeira de 2008
A crise financeira global de 2008, causada pelo colapso do mercado imobiliário dos Estados Unidos, teve um impacto significativo no setor de petróleo. Inicialmente, os preços do petróleo atingiram um pico histórico de quase US\$ 147 por barril em julho de 2008, mas, com o agravamento da recessão, a demanda despencou, levando a uma queda abrupta para cerca de US\$ 33 por barril em fevereiro de 2009.

### Pandemia de COVID-19 (2020-2021)
A pandemia de COVID-19 provocou uma das maiores quedas na demanda por petróleo da história. Com lockdowns ao redor do mundo e a redução drástica do transporte e da atividade industrial, os preços do petróleo chegaram a ficar negativos em abril de 2020, um evento sem precedentes. Em 2021, com a recuperação econômica, o barril voltou a subir, atingindo US\$ 80 no final do ano.

### Guerra na Ucrânia (2022)
A invasão da Ucrânia pela Rússia em 2022 gerou uma nova onda de instabilidade no mercado de petróleo. A Rússia, um dos maiores produtores mundiais, enfrentou sanções econômicas que afetaram suas exportações, levando os preços do petróleo a atingirem US\$ 120 por barril em março de 2022.

                
O gráfico abaixo ilustra a evolução do preço do petróleo Brent ao longo das últimas décadas, destacando os principais eventos que impactaram o mercado.
""")
    st.image("app/data/images/grafico_explicativo.jpg", caption="Evolução do Preço do Petróleo Brent (1987-2025)")
    st.markdown("""

---

#### Referências

- FORBES. Cinco crises que moldaram o mercado de petróleo e o impacto na Petrobras. 2024. Disponível em: <https://forbes.com.br/forbes-money/2024/10/cinco-crises-que-moldaram-o-mercado-de-petroleo-e-o-impacto-na-petrobras/>. Acesso em: 17 maio 2025.  
- CNN BRASIL. Preço do petróleo bate maior nível desde 2008 com atrasos em negociações no Irã. 2022. Disponível em: <https://www.cnnbrasil.com.br/economia/macroeconomia/preco-do-petroleo-bate-maior-nivel-desde-2008-com-atrasos-em-negociacoes-no-ira/>. Acesso em: 17 maio 2025.  
- CNN BRASIL. Há um ano, preço do petróleo estava negativo, mas isso agora é passado. 2021. Disponível em: <https://www.cnnbrasil.com.br/economia/macroeconomia/ha-um-ano-preco-do-petroleo-estava-negativo-mas-isso-agora-e-passado/>. Acesso em: 17 maio 2025.  
- BBC NEWS BRASIL. Alta e queda do petróleo de 2008 a 2009. 2008. Disponível em: <https://www.bbc.com/portuguese/reporterbbc/story/2008/12/081217_petroleo_qandarg>. Acesso em: 17 maio 2025.  
- BRASIL ESCOLA. Guerra do Golfo: causas, desdobramentos e consequências. 2025. Disponível em: <https://brasilescola.uol.com.br/historiag/guerra-golfo.htm>. Acesso em: 17 maio 2025.  
- SUNO RESEARCH. Crise asiática: causas, impactos e desdobramentos. 2025. Disponível em: <https://www.suno.com.br/artigos/crise-asiatica/>. Acesso em: 17 maio 2025.  
    """)