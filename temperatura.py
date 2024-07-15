import requests
import json
from senha import chave_api


def api():  
     
    cidade = input ('Informe a cidade ?\n')
    api= requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}')
    api_cidade = api.json()
    return api_cidade

def informacoes_cidade(api_cidade):
    
    nome = api_cidade['name']
    temperatura = api_cidade['main']['temp']
    temperatura_celsius = round(temperatura - 273.15,2)
    return nome, temperatura_celsius


quantidade = int(input('informe a quantidade de cidades que deseja fazer: '))

cidades = []
for x in range (1, quantidade + 1):
    api_cidade = api()
    nome, temperatura = informacoes_cidade(api_cidade)
   
    cidade1 = f'A cidade {nome}, está com uma temperatura de {temperatura}°C'
    cidades.append(cidade1)

print(cidades)