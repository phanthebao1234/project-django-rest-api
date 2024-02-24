import requests
from getpass import getpass

username = input('Enter username: ')
password = getpass("Enter your password: ")
auth_endpoints = "http://127.0.0.1:8000/api/auth/"
auth_response = requests.post(auth_endpoints, json={"username": username, "password": password})
print(auth_response.json())
if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {"Authorization": f"Token {token}"}
        
    endpoints = "http://127.0.0.1:8000/api/products/"

    get_response = requests.get(endpoints, headers=headers)
    print("********************")
    print(get_response.json())
