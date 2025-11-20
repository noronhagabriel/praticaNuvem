def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Exemplo de uso:
# print(calcular_gorjeta(100, 10))  # Resultado: 10.0
