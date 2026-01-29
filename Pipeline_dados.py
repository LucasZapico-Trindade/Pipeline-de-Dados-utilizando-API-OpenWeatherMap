import requests
import psycopg2
from datetime import datetime

API_KEY = "0c986d4b3de23554b1fc3ad8ac31a8ed"
URL = "https://api.openweathermap.org/data/2.5/weather"

def buscar_clima(cidade):
    parametros = {
        "q": cidade,
        "appid": API_KEY,
        "lang": "pt_br"
    }
    resposta = requests.get(URL, params=parametros)
    return resposta.json()

def transformar_dados(data):
    cidade = data["name"]
    pais = data["sys"]["country"]
    temperatura_kelvin = data["main"]["temp"]
    umidade = data["main"]["humidity"]
    clima = data["weather"][0]["description"]
    timestamp = data["dt"]

    temperatura_celsius = temperatura_kelvin - 273.15
    data_coleta = datetime.fromtimestamp(timestamp)

    return cidade, pais, temperatura_celsius, umidade, clima, data_coleta
def salvar_no_postgres(cidade, pais, temperatura_celsius, umidade, clima, data_coleta):
    conn = psycopg2.connect(
        host="localhost",
        database="weather_db",
        user="postgres",
        password="spfc1909"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO weather_data (cidade, pais, temperatura, umidade, clima, data_coleta)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (cidade, pais, temperatura_celsius, umidade, clima, data_coleta)
)

    conn.commit()
    cursor.close()
    conn.close()

def main():
    cidade_input = str(input("Digite o nome da cidade: "))
    dados_api = buscar_clima(cidade_input)
    cidade, pais, temperatura_celsius, umidade, clima, data_coleta = transformar_dados(dados_api)
    salvar_no_postgres(cidade, pais, temperatura_celsius, umidade, clima, data_coleta)

    print("Dados inseridos no PostgreSQL com sucesso!!")


if __name__ == "__main__":
    main()










