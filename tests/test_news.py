import requests
base_url = "http://127.0.0.1:5000/news/"
headers = {
    "accept": "*/*",
    'User-Agent': 'request'
}



def test_get_all_news_return_information():
    data = requests.get(base_url, headers=headers)
    answer = requests.get(base_url, headers=headers)
    expected = 200
    assert answer.status_code == expected

def test_post_news():    
    post_url = base_url+'1/create'
    data = {
        "title": "Livro saddassdkj",
        "subtitle": "Author",
        "content": "Long sjdasddajskjnckn",
        "upvotes": 1,
        "downvotes": 1,
        "create_at": "10/10/2010",
        "approved": True
        }
    answer = requests.post(post_url,json=data,headers=headers)
    assert answer.status_code == 200 
        
