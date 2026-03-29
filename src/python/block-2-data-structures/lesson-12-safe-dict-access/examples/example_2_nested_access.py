"""
Приклад 2: Безпечний доступ до вкладених словників.

Запуск: pytest example_2_nested_access.py -v
"""


def test_nested_access_safe():
    """Покроковий безпечний доступ."""
    response = {
        "status": 200,
        "data": {"user": {"name": "Alice", "email": "alice@test.com"}},
    }
    data = response.get("data", {})
    user = data.get("user", {})
    name = user.get("name", "Unknown")
    assert name == "Alice"


def test_nested_missing_level():
    """Один з рівнів відсутній — .get() рятує."""
    response = {"status": 200}  # немає "data"

    data = response.get("data", {})
    user = data.get("user", {})
    name = user.get("name", "Unknown")
    assert name == "Unknown"


def test_nested_with_list():
    """Вкладений список у словнику."""
    response = {
        "data": {
            "users": [
                {"name": "Alice"},
                {"name": "Bob"},
            ]
        }
    }
    users = response.get("data", {}).get("users", [])
    assert len(users) == 2
    assert users[0].get("name") == "Alice"


def test_deeply_nested_safe():
    """Глибока вкладеність — кожен рівень через .get()."""
    api = {"response": {"body": {"result": {"value": 42}}}}

    value = (
        api.get("response", {})
           .get("body", {})
           .get("result", {})
           .get("value", 0)
    )
    assert value == 42