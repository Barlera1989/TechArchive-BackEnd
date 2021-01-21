from pytest import fail
from werkzeug.exceptions import NotFound

import requests

base_url = "http://127.0.0.1:5000/user"
headers = {
    "accept": "*/*",
    'User-Agent': 'request'
}


def test_get_all_users():
    get_url = base_url + '/all'
    data = requests.get(get_url, headers=headers)
    answer = requests.get(get_url, headers=headers)
    assert answer.status_code == 200


def create_user():
    create_url = base_url+'/create'
    data = {
        "name": "Usuário comum",
        "description": "Escritor de tecnologia",
        "email": "usuario@email.com",
        "password": "123456"
    }
    response = requests.post(create_url, json=data, headers=headers)
    assert response.status_code == 200
