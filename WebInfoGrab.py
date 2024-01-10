import requests

url = input("Digite a URL: ")

try:
    response = requests.get(url)

    server_info = response.headers

    print("Servidor web ativo")
    print(server_info)
except requests.RequestException as e:
    print(f"Erro ao conectar ao servidor: {e}")

