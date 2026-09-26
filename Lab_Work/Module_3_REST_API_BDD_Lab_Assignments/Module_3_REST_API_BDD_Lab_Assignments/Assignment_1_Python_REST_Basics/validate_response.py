# Assignment 1 - Python basics for REST response validation

def validate_post(data):
    required = ["id", "title", "userId"]
    for key in required:
        if key not in data:
            return False
    return data["id"] > 0 and bool(data["title"])

sample = {
    "id": 1,
    "title": "REST Automation",
    "userId": 1
}

assert validate_post(sample)
print("Response validation: PASS")
