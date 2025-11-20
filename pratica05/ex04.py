from datetime import datetime

print("=== Dias de Vida ===")

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converter para data
nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

# Data atual
hoje = datetime.now()

# Diferença em dias
dias_vivo = (hoje - nascimento).days

print(f"\nVocê está vivo há aproximadamente {dias_vivo} dias.")
