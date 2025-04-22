import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view"  

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

table = soup.find("table", {"id": "grd_DXMainTable"})

headers = [header.text.strip() for header in table.find_all("td", class_="dxgvHeader")]

data = []
for row in table.find_all("tr", {"id": lambda x: x and x.startswith("grd_DXDataRow")}):
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]
    data.append(cols)

df = pd.DataFrame(data, columns=headers)

print(df)

df.to_csv("tabela_extraida.csv", index=False)
