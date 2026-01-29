from api import buscar_clima
from transform import transformar_dados
from database import salvar_no_postgres

def main():
    cidade_input = input("Digite o nome da cidade: ")
    
    dados_api = buscar_clima(cidade_input)
    cidade, pais, temperatura, umidade, clima, data_coleta = transformar_dados(dados_api)
    
    salvar_no_postgres(cidade, pais, temperatura, umidade, clima, data_coleta)
    
    print("Dados inseridos no PostgreSQL com sucesso!")

if __name__ == "__main__":
    main()
