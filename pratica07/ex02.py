print("=== Criar Arquivo TXT Tabulado ===")

arquivo = input("Digite o nome do arquivo para salvar (ex: dados.txt): ")

pessoas = [
    {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Carlos", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Marina", "idade": 22, "cidade": "Curitiba"}
]

try:
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write("Nome\tIdade\tCidade\n")

        for p in pessoas:
            f.write(f"{p['nome']}\t{p['idade']}\t{p['cidade']}\n")

    print("Arquivo salvo com sucesso!")

except:
    print("Falha ao salvar o arquivo!")
