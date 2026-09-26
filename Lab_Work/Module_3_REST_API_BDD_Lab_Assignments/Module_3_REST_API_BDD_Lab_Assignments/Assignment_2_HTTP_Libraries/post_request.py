import requests

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "title": "Module 3 Lab",
    "body": "Python REST automation",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload,
    headers=headers,
    timeout=10
)

assert response.status_code == 201
assert response.json()["title"] == payload["title"]
print("POST request: PASS")
