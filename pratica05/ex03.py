print("=== Cálculo de Desconto ===")

valor = float(input("Digite o preço original do produto: R$ "))
desconto = float(input("Digite a porcentagem de desconto (%): "))

# Cálculo
valor_desconto = valor * (desconto / 100)
preco_final = valor - valor_desconto

# Exibição
print(f"\nValor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
