import requests

print("=== Consulta CEP ===")

cep = input("Digite o CEP (somente números): ")

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)

    if resposta.status_code == 200:
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado!")
        else:
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    else:
        print("Erro na requisição!")

except:
    print("Falha na conexão com a API!")
