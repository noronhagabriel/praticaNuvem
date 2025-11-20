import requests

print("=== Consulta de Cotação ===")

moeda = input("Digite a moeda desejada (ex: USD, EUR, BTC): ").upper()

try:
    resposta = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL", timeout=5)

    if resposta.status_code == 200:
        dados = resposta.json()

        chave = moeda + "BRL"

        if chave in dados:
            info = dados[chave]

            print(f"Moeda: {info['code']} → BRL")
            print(f"Valor atual: R$ {info['bid']}")
            print(f"Máxima do dia: R$ {info['high']}")
            print(f"Mínima do dia: R$ {info['low']}")
            print(f"Última atualização: {info['create_date']}")
        else:
            print("Moeda não encontrada!")
    else:
        print("Erro ao consultar a API!")

except:
    print("Falha na conexão com a API!")
