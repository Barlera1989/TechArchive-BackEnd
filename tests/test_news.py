from pytest import fail
from werkzeug.exceptions import NotFound

import requests

base_url = "http://localhost:5000/news"
headers = {
    "accept": "*/*",
    'User-Agent': 'request',
    'Authorization': 'Bearer AUTH_TOKEN_HERE'
}


def test_get_all_news_route_exists():
    data = requests.get(base_url, headers=headers)
    answer = requests.get(base_url, headers=headers)
    assert answer.status_code == 200


def test_post_news():
    post_url = base_url + '/create'
    data = {
        "title": "Titulo exemplo111",
        "subtitle": "Author",
        "content": "Descrição muita longa aqui...",
        "upvotes": 1,
        "downvotes": 1,
        "approved": False,
    }
    answer = requests.post(post_url, json=data, headers=headers)
    assert answer.status_code == 200
