from datetime import datetime

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
