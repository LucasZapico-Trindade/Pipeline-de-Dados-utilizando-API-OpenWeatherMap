# 🌦️ Pipeline de Dados com OpenWeather API e PostgreSQL

Projeto de pipeline ETL em Python que consome dados da API OpenWeather, realiza transformações e armazena os dados em PostgreSQL.

## 🏗️ Arquitetura do Pipeline

- Extract: Consumo de dados da API OpenWeather.
- Transform: Conversão e tratamento dos dados.
- Load: Persistência dos dados em PostgreSQL.

## 🛠️ Tecnologias

- Python
- PostgreSQL
- OpenWeather API
- Requests
- Psycopg2
- Git/GitHub

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>

2. Instale as dependências:

   pip install -r requirements.txt

3. Crie a tabela no PostgreSQL:

   Execute o script em sql/create_table.sql.

4. Execute o pipeline:

   python src/main.py
