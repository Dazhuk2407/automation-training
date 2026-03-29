"""
Вправа 1: Навігація по вкладених даних.
Запуск: pytest exercise_1_navigation.py -v
"""

RESPONSE = {
    "status": 200,
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@test.com"},
            {"id": 2, "name": "Bob", "email": "bob@test.com"},
        ],
        "total": 2,
    },
}


def test_status():
    """status == 200."""
    # TODO: замініть pass на: assert RESPONSE["status"] == 200
    pass


def test_users_count():
    """Кількість users == 2."""
    # TODO: замініть pass на:
    #   users = RESPONSE["data"]["users"]
    #   assert len(users) == 2
    pass


def test_first_user_name():
    """Ім'я першого user == 'Alice'."""
    # TODO: замініть pass на:
    #   name = RESPONSE["data"]["users"][0]["name"]
    #   assert name == "Alice"
    pass


def test_safe_access():
    """Безпечний доступ до відсутнього поля."""
    # TODO: замініть pass на:
    #   data = RESPONSE.get("data", {})
    #   meta = data.get("meta", {})
    #   version = meta.get("version", "unknown")
    #   assert version == "unknown"
    pass