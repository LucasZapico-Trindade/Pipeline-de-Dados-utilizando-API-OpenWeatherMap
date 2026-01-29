import requests

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
