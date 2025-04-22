import requests
from bs4 import BeautifulSoup
import pandas as pd

class GetIpeaDataPetroleo:
    def __init__(self):
        self.url = "http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view"
        self.csv_file = "tabela_extraida.csv"

    def fetch_data(self):
        try:
            # Fazer a requisição HTTP para obter o conteúdo da página
            response = requests.get(self.url)
            response.raise_for_status()  # Verifica se houve algum erro na requisição
            html_content = response.text

            # Analisar o conteúdo HTML com BeautifulSoup
            soup = BeautifulSoup(html_content, "html.parser")

            # Encontrar a tabela com os dados
            table = soup.find("table", {"id": "grd_DXMainTable"})
            if not table:
                raise ValueError("Tabela com ID 'grd_DXMainTable' não encontrada na página.")

            # Extrair os cabeçalhos da tabela
            headers = [header.text.strip() for header in table.find_all("td", class_="dxgvHeader")]

            # Extrair os dados das linhas da tabela
            data = []
            for row in table.find_all("tr", {"id": lambda x: x and x.startswith("grd_DXDataRow")}):
                cols = row.find_all("td")
                cols = [col.text.strip() for col in cols]
                data.append(cols)

            # Criar um DataFrame com os dados extraídos
            df = pd.DataFrame(data, columns=headers)

            return df

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a URL: {e}")
            return None
        except ValueError as e:
            print(f"Erro ao processar os dados: {e}")
            return None
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None

    def save_to_csv(self, df):
        try:
            # Salvar o DataFrame em um arquivo CSV
            df.to_csv(self.csv_file, index=False, encoding="utf-8-sig")
            print(f"Tabela salva com sucesso no arquivo '{self.csv_file}'.")
        except Exception as e:
            print(f"Erro ao salvar o arquivo CSV: {e}")
