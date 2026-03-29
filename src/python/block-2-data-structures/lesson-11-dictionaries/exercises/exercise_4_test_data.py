"""
Вправа 4: Словники як тестові дані.
Запуск: pytest exercise_4_test_data.py -v
"""


API_RESPONSE = {
    "status": 200,
    "data": {
        "user": {"id": 1, "name": "Alice", "email": "alice@test.com"},
    },
}

USER = {"name": "Bob", "role": "user", "active": True}


def test_required_fields():
    """API response має id, name, email."""
    user_data = API_RESPONSE["data"]["user"]
    required = ["id", "name", "email"]
    # TODO: замініть pass на:
    #   for field in required:
    #       assert field in user_data
    pass


def test_status_code():
    """response status == 200."""
    # TODO: замініть pass на: assert API_RESPONSE["status"] == 200
    pass


def test_nested_access():
    """Дістати name з вкладеної структури."""
    # TODO: замініть pass на:
    #   name = API_RESPONSE["data"]["user"]["name"]
    #   assert name == "Alice"
    pass


def test_user_is_active():
    """user['active'] is True."""
    # TODO: замініть pass на: assert USER["active"] is True
    pass