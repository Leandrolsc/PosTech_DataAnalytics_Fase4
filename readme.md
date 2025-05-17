# Análise do Preço do Petróleo Brent

Este projeto faz parte do trabalho da **Fase 4 da Pós Tech em Data Analytics na FIAP**. O objetivo é realizar uma análise do preço do petróleo Brent, utilizando dados históricos extraídos do **IPEA (Instituto de Pesquisa Econômica Aplicada)**.

A aplicação permite **visualizar os dados**, **gerar gráficos temporais**, **realizar previsões com Machine Learning** e **baixar as informações em formato CSV**.

---

## 📁 Estrutura do Projeto

```
PosTech_FIAP_F4/
├── .streamlit/                # Configurações do tema e aparência no Streamlit
├── app/
│   ├── data/                  # Dados extraídos e metadados
│   ├── presentations/         # Interface Streamlit e páginas customizadas
│   │   └── custom_pages/      # Páginas específicas (ML, Storytelling)
│   ├── use_cases/             # Lógica de negócio (modelos, scraping)
│   └── __pycache__/           # Arquivos temporários do Python
├── notebooks/                 # Notebooks de exploração e modelagem
├── requirements.txt           # Dependências do projeto
├── README.md                  # Este arquivo
└── .gitignore
```

---

## 🚀 Funcionalidades

- **📊 Storytelling e Download dos Dados**  
  Visualize a evolução histórica do preço do petróleo Brent com gráficos interativos e exporte os dados em CSV.

- **🤖 Machine Learning (ML)**  
  Estime o preço do Brent para os próximos dias com o modelo Prophet. O usuário define o período de previsão e visualiza resultados com faixas de confiança.

- **🌐 Atualização Automática dos Dados**  
  Dados extraídos diretamente do site do IPEA via Web Scraping, garantindo informações sempre atualizadas.

---

## 🧪 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Leandrolsc/PosTech_DataAnalytics_Fase4.git
   cd PosTech_FIAP_F4
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação Streamlit:**
   ```bash
   streamlit run app/presentations/Home.py
   ```

4. **Acesse no navegador:**  
   [http://localhost:8501](http://localhost:8501)

---

## 📌 Principais Arquivos

| Caminho                                 | Descrição                                      |
|------------------------------------------|------------------------------------------------|
| app/presentations/Home.py                | Página principal da aplicação Streamlit         |
| app/presentations/custom_pages/ml.py     | Página de Machine Learning e previsões          |
| app/presentations/custom_pages/storytelling.py | Página de visualização e download dos dados |
| app/use_cases/model.py                   | Funções de modelagem e previsão                 |
| app/use_cases/scrapping.py               | Script de scraping dos dados do IPEA            |

---

## 📚 Referências

- [IPEA - Instituto de Pesquisa Econômica Aplicada](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view)
- [Forbes - Crises do petróleo](https://forbes.com.br/forbes-money/2024/10/cinco-crises-que-moldaram-o-mercado-de-petroleo-e-o-impacto-na-petrobras/)
- [CNN Brasil - Alta de 2022](https://www.cnnbrasil.com.br/economia/macroeconomia/preco-do-petroleo-bate-maior-nivel-desde-2008-com-atrasos-em-negociacoes-no-ira/)
- [BBC - Alta e queda de 2008 a 2009](https://www.bbc.com/portuguese/reporterbbc/story/2008/12/081217_petroleo_qandarg)
- [CNN Brasil - Petróleo entre 2020 e 2021 (COVID)](https://www.cnnbrasil.com.br/economia/macroeconomia/ha-um-ano-preco-do-petroleo-estava-negativo-mas-isso-agora-e-passado/)
- [Wikipedia - Crise financeira de 2007–2008](https://pt.wikipedia.org/wiki/Crise_financeira_de_2007%E2%80%932008)

---

## 👨‍💻 Desenvolvedores

- [Leandro Victor Silva](https://www.linkedin.com/in/leandro-victor-silva-8a319b228/)
- [Murilo Maioli](https://www.linkedin.com/in/murilo-maioli-21195aaa/)