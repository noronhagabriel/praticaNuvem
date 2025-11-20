import random
import string

print("=== Gerador de Senhas ===")

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = "".join(random.choice(caracteres) for _ in range(tamanho))

print(f"Senha gerada: {senha}")
