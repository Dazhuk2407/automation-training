"""
Вправа 2: Безпечний доступ до вкладених словників.
Запуск: pytest exercise_2_nested.py -v
"""


RESPONSE_FULL = {
    "status": 200,
    "data": {"user": {"name": "Alice", "email": "alice@test.com"}},
}

RESPONSE_EMPTY = {"status": 200}


def test_nested_safe_access():
    """Дістати name через ланцюжок .get()."""
    # TODO: замініть pass на:
    #   data = RESPONSE_FULL.get("data", {})
    #   user = data.get("user", {})
    #   name = user.get("name", "Unknown")
    #   assert name == "Alice"
    pass


def test_missing_level():
    """Якщо 'data' відсутній — name має бути 'Unknown'."""
    # TODO: замініть pass на:
    #   data = RESPONSE_EMPTY.get("data", {})
    #   user = data.get("user", {})
    #   name = user.get("name", "Unknown")
    #   assert name == "Unknown"
    pass


def test_nested_list():
    """Дістати першого user зі списку."""
    response = {"data": {"users": [{"name": "Alice"}, {"name": "Bob"}]}}
    # TODO: замініть pass на:
    #   users = response.get("data", {}).get("users", [])
    #   assert len(users) == 2
    #   assert users[0].get("name") == "Alice"
    pass