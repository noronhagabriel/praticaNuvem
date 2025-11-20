def eh_palindromo(texto: str) -> str:
    texto_limpo = "".join(ch.lower() for ch in texto if ch.isalnum())
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"


# Exemplos:
# print(eh_palindromo("arara"))
# print(eh_palindromo("A sacada da casa"))
# print(eh_palindromo("Python"))
