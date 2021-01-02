import requests

BASE_URL='http://127.0.0.1:8000/api/'
ENDPOINT='cbv/post'


def get_post(id):
    response = requests.get(BASE_URL + ENDPOINT + '/' + str(id))
    # This json() method internally convert json object into python dictionary by calling load() method
    if(response.status_code == requests.codes.ok):
        print(response.json());
    else:
        print("ID {} could not found!!".format(id))

def get_posts():
    response = requests.get(BASE_URL + ENDPOINT)
    # This json() method internally convert json object into python dictionary by calling load() method
    print(response.status_code);
    print(response.json());

get_post(4)
get_posts()