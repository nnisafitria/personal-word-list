import requests

api_key = '6b086aa8-a0d3-454a-a62f-72ff9e9f1e4d'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=6b086aa8-a0d3-454a-a62f-72ff9e9f1e4d'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print (definition)