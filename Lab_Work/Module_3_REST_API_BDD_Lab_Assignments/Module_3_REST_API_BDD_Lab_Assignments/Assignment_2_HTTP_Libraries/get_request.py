import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10
)

print("Status:", response.status_code)
data = response.json()

assert response.status_code == 200
assert data["id"] == 1
print("GET request: PASS")
