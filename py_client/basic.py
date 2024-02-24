import requests

# endpoints = 'https://httpbin.org/status/200'
# endpoints = 'https://httpbin.org/anything'
endpoints = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoints, params={"abc": 123}, json={"query": 'Hello world'})
print(get_response.text)
print(get_response.headers)
# print(get_response.status_code)

# HTTP Request -> HTML
# Rest API HTTP Request -> JSON
# Javascript Object Nototion ~ Python Dict
# print(get_response.json())
# print(get_response.status_code)
