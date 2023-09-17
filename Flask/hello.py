import requests

name = "Dima"
response_age = requests.get(f'https://api.agify.io?name={name}').json()['age']
