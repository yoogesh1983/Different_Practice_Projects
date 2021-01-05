import json

import requests

BASE_URL = 'http://127.0.0.1:8000/api/'
ENDPOINT = 'cbv/post'
ENDPOINT_DRF = 'drf/post'


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

def update_post(id):
    post = {
        'title': 'Nepal',
        'body': 'updated:::::::::Nepal means United states America.',
        'status': 'published',
        'tags': 'django'
    }
    json_data = json.dumps(post)
    resp = requests.put(BASE_URL + ENDPOINT + '/' + str(id) + '/', data=json_data)
    print(resp.status_code)
    print(resp.json())

def delete_post(id):
    resp = requests.delete(BASE_URL + ENDPOINT + '/' + str(id))
    print(resp.status_code)
    print(resp.json())


#get_post(4)
#get_posts()
#insert_post()
#update_post(14)
#delete_post(18)



def get_post_drf(id):
    response = requests.get(BASE_URL + ENDPOINT_DRF + '/' + str(id))
    if (response.status_code == requests.codes.ok):
        print(response.json());
    else:
        print("ID {} could not found!!".format(id))

def get_posts_drf():
    response = requests.get(BASE_URL + ENDPOINT_DRF)
    print(response.status_code);
    print(response.json());

def insert_post_drf():
    post = {
        'title': 'statefarm',
        'slug': 'usa',
        'body': 'USA means United states America.',
        'status': 'published',
        'tags': 'USA,Nepal,India'
    }
    json_data = json.dumps(post)
    resp = requests.post(BASE_URL + ENDPOINT_DRF + '/', data=json_data)
    print(resp.status_code)
    print(resp.json())

#get_post_drf(4)
#get_posts_drf()
insert_post_drf()
