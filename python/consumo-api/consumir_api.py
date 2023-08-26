import requests

api_url = 'https://jsonplaceholder.typicode.com/posts/2'

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print('Dados da API: ', data)
else:
    print('Erro ao consumir a API: ', response.status_code)