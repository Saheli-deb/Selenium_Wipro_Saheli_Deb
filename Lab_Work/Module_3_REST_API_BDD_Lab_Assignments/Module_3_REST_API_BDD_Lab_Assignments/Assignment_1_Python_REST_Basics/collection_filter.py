# Collection handling for API-style JSON data

posts = [
    {"id": 1, "title": "Login API", "userId": 1},
    {"id": 2, "title": "POST API", "userId": 1},
    {"id": 3, "title": "BDD Test", "userId": 2}
]

user_one = [post for post in posts if post["userId"] == 1]

print(user_one)
assert len(user_one) == 2
