import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )
    response.raise_for_status()
    print("Request successful")
    print(response.json())

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.RequestException as exc:
    print("Request/network error:", exc)
