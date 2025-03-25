import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da página que contém a tabela
url = "http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view"  # Substitua pela URL real

# Faz a requisição HTTP para obter o HTML da página
response = requests.get(url)
html_content = response.text

# Parseia o HTML com BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Encontra a tabela pelo ID
table = soup.find("table", {"id": "grd_DXMainTable"})

# Coletar os cabeçalhos da tabela
headers = [header.text.strip() for header in table.find_all("td", class_="dxgvHeader")]

# Coletar os dados das linhas da tabela
data = []
for row in table.find_all("tr", {"id": lambda x: x and x.startswith("grd_DXDataRow")}):
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Criar um DataFrame pandas
df = pd.DataFrame(data, columns=headers)

# Exibir a tabela extraída
print(df)

# Opcional: Salvar em CSV
df.to_csv("tabela_extraida.csv", index=False)
