import requests

url = input("Digite a URL: ")

try:
    # Fazer uma solicitação GET
    response = requests.get(url)

    # Obter informações do servidor
    server_info = response.headers

    print("Servidor web ativo")
    print(server_info)
except requests.RequestException as e:
    print(f"Erro ao conectar ao servidor: {e}")

