from behave import when, then
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@when("I request post {id}")
def request_post(context, id):
    context.response = requests.get(
        f"{BASE_URL}/posts/{id}",
        timeout=10
    )

@then("the response status should be 200")
def check_status(context):
    assert context.response.status_code == 200
