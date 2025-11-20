print("=== Verificador de Senha ===")

senha = input("Digite uma senha: ")

tem_tamanho = len(senha) >= 8
tem_numero = any(ch.isdigit() for ch in senha)

if tem_tamanho and tem_numero:
    print("Senha válida! ✔")
else:
    print("Senha inválida! ❌")
    if not tem_tamanho:
        print("- A senha deve ter pelo menos 8 caracteres.")
    if not tem_numero:
        print("- A senha deve conter pelo menos um número.")
