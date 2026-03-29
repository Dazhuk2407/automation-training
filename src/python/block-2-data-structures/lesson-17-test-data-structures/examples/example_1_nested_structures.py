"""
Приклад 1: Навігація по вкладених API responses.

Запуск: pytest example_1_nested_structures.py -v
"""


API_RESPONSE = {
    "status": 200,
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@test.com", "roles": ["admin"]},
            {"id": 2, "name": "Bob", "email": "bob@test.com", "roles": ["user"]},
            {"id": 3, "name": "Charlie", "email": "charlie@test.com", "roles": ["user", "editor"]},
        ],
        "total": 3,
        "page": 1,
    },
}


def test_status_code():
    assert API_RESPONSE["status"] == 200


def test_users_count():
    users = API_RESPONSE["data"]["users"]
    assert len(users) == 3


def test_total_matches():
    data = API_RESPONSE["data"]
    assert data["total"] == len(data["users"])


def test_first_user_name():
    name = API_RESPONSE["data"]["users"][0]["name"]
    assert name == "Alice"


def test_admin_exists():
    users = API_RESPONSE["data"]["users"]
    admins = [u for u in users if "admin" in u["roles"]]
    assert len(admins) >= 1


def test_all_have_email():
    users = API_RESPONSE["data"]["users"]
    for user in users:
        assert "email" in user
        assert "@" in user["email"]