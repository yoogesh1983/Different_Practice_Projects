import requests

BASE_URL='http://127.0.0.1:8000/api/'
ENDPOINT='post'

response = requests.get(BASE_URL + ENDPOINT)

#This json() method internally convert json object into python dictionary by calling load() method
print(response.json());