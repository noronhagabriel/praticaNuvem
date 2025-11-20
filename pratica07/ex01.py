import csv

print("=== Leitura de CSV ===")

arquivo = input("Digite o nome do arquivo CSV: ")

try:
    with open(arquivo, "r", newline="", encoding="utf-8") as csvfile:
        leitor = csv.DictReader(csvfile)

        valores = []

        for linha in leitor:
            if "tempo_execucao" in linha:
                valores.append(float(linha["tempo_execucao"]))

        if len(valores) == 0:
            print("A coluna 'tempo_execucao' não foi encontrada ou está vazia.")
        else:
            media = sum(valores) / len(valores)
            maior = max(valores)

            print(f"Média: {media:.2f}")
            print(f"Maior tempo de execução: {maior:.2f}")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
except Exception as e:
    print("Erro ao ler o arquivo:", e)
