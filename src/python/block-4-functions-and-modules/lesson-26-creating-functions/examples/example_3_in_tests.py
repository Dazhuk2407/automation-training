"""
Приклад 3: Функції як будівельні блоки тестів.
Запуск: pytest example_3_in_tests.py -v
"""


def make_user(name, role="user", active=True):
    """Фабрика тестових користувачів."""
    return {"name": name, "role": role, "active": active}


def get_active_users(users):
    """Відфільтрувати активних."""
    return [u for u in users if u["active"]]


def validate_response(response, expected_status=200):
    """Валідувати API response."""
    assert response["status"] == expected_status
    assert "data" in response


def test_make_user_default():
    user = make_user("Alice")
    assert user["role"] == "user"
    assert user["active"] is True


def test_make_user_admin():
    admin = make_user("Bob", role="admin")
    assert admin["role"] == "admin"


def test_active_users():
    users = [
        make_user("Alice", active=True),
        make_user("Bob", active=False),
        make_user("Charlie", active=True),
    ]
    active = get_active_users(users)
    assert len(active) == 2


def test_validate_response():
    response = {"status": 200, "data": {"users": []}}
    validate_response(response)


def test_validate_response_custom_status():
    response = {"status": 201, "data": {"id": 1}}
    validate_response(response, expected_status=201)