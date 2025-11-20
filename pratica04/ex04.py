print("=== Contador de Pares e Ímpares ===")

pares = 0
impares = 0

while True:
    num = int(input("Digite um número (ou 0 para parar): "))

    if num == 0:
        break

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
