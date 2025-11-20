import requests

print("=== Usuário Aleatório ===")

try:
    resposta = requests.get("https://randomuser.me/api/", timeout=5)

    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados["results"][0]

        nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    else:
        print(f"Falha ao buscar usuário. Status code: {resposta.status_code}")

except requests.exceptions.Timeout:
    print("Erro: Timeout na conexão com a API!")
except requests.exceptions.ConnectionError:
    print("Erro: Falha na conexão com a API!")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except KeyError as e:
    print(f"Erro: Campo não encontrado na resposta da API: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
