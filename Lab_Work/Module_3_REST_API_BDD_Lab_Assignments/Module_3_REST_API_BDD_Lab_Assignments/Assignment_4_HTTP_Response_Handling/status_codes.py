import requests

success = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10
)
assert success.status_code == 200

missing = requests.get(
    "https://jsonplaceholder.typicode.com/posts/999999",
    timeout=10
)
assert missing.status_code == 404

print("Positive and negative responses: PASS")
