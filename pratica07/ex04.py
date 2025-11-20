import json

print("=== Arquivo JSON ===")

arquivo = "dados.json"

dados = {
    "nome": "João",
    "idade": 28,
    "cidade": "Belo Horizonte"
}

# --- Escrever o arquivo JSON ---
try:
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print("Arquivo JSON salvo com sucesso!")
except:
    print("Erro ao salvar o arquivo JSON!")

# --- Ler o arquivo JSON ---
try:
    with open(arquivo, "r", encoding="utf-8") as f:
        dados_lidos = json.load(f)
        print("\nDados lidos do JSON:")
        print(f"Nome: {dados_lidos['nome']}")
        print(f"Idade: {dados_lidos['idade']}")
        print(f"Cidade: {dados_lidos['cidade']}")

except FileNotFoundError:
    print("Erro: Arquivo JSON não encontrado!")
except Exception as e:
    print("Erro ao ler o arquivo JSON:", e)
