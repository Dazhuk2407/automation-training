"""Приклад 2: парсинг API-відповіді. Запуск: pytest example_2_parse_api.py -v"""
import json

API_RESPONSE = '''
{
  "status": "ok",
  "data": {
    "total": 2,
    "users": [
      {"id": 1, "name": "Alice", "email": "alice@test.com", "active": true},
      {"id": 2, "name": "Bob", "email": "bob@test.com", "active": false}
    ]
  }
}
'''


def get_status(raw):
    return json.loads(raw)["status"]

def get_users(raw):
    return json.loads(raw)["data"]["users"]

def first_email(raw):
    return json.loads(raw)["data"]["users"][0]["email"]

def find_email(raw, user_id):
    for user in json.loads(raw)["data"]["users"]:
        if user["id"] == user_id:
            return user["email"]
    return None

def safe_total(raw):
    return json.loads(raw).get("data", {}).get("total")

def test_status():
    assert get_status(API_RESPONSE) == "ok"

def test_get_users():
    users = get_users(API_RESPONSE)
    assert len(users) == 2
    assert users[0]["name"] == "Alice"

def test_first_email():
    assert first_email(API_RESPONSE) == "alice@test.com"

def test_find_email():
    assert find_email(API_RESPONSE, 2) == "bob@test.com"
    assert find_email(API_RESPONSE, 99) is None

def test_types_after_parse():
    users = get_users(API_RESPONSE)
    assert users[0]["active"] is True
    assert users[1]["active"] is False

def test_safe_navigation():
    assert safe_total(API_RESPONSE) == 2
    assert safe_total('{"status": "empty"}') is None
