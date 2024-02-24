import requests

headers = {"Authorization": "Bearer dd63aad8bf6632c2b51024c392b675d11b561065"}
endpoints = "http://127.0.0.1:8000/api/products/"
data = {
    "title": "This field is done", 
    "price": 2002
}
get_response = requests.post(endpoints, json=data, headers=headers)
print(get_response.json())