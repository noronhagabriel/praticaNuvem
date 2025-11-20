print("=== Leitura de Arquivo TXT ===")

arquivo = input("Digite o nome do arquivo TXT: ")

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            print(linha.strip())

except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
except Exception as e:
    print("Erro ao ler o arquivo:", e)
