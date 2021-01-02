import json

import requests

BASE_URL = 'http://127.0.0.1:8000/api/'
ENDPOINT = 'cbv/post'


def get_post(id):
    response = requests.get(BASE_URL + ENDPOINT + '/' + str(id))
    # This json() method internally convert json object into python dictionary by calling load() method
    if (response.status_code == requests.codes.ok):
        print(response.json());
    else:
        print("ID {} could not found!!".format(id))


def get_posts():
    response = requests.get(BASE_URL + ENDPOINT)
    # This json() method internally convert json object into python dictionary by calling load() method
    print(response.status_code);
    print(response.json());

def insert_post():
    post = {
        'title': 'USA',
        'slug': 'usa',
        'body': 'USA means United states America.',
        'status': 'published',
        'tags': 'USA,Nepal,India'
    }
    json_data = json.dumps(post)
    resp = requests.post(BASE_URL + ENDPOINT + '/', data=json_data)
    print(resp.status_code)
    print(resp.json())


#get_post(4)
#get_posts()
insert_post()
