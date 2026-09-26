from behave import given, when, then
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@given("the posts API is available")
def api_available(context):
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert response.status_code == 200

@when("I request post 1")
def request_post(context):
    context.response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=10
    )

@then("the response status should be 200")
def status_200(context):
    assert context.response.status_code == 200

@then("the response should contain post id 1")
def contains_id(context):
    assert context.response.json()["id"] == 1
