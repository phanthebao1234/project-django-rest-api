import requests

endpoints = "http://127.0.0.1:8000/api/products/1/update/"
data = {"title": "Hello world my best friends", "price": 3999.69}
get_response = requests.put(endpoints, json=data)
print(get_response.json())