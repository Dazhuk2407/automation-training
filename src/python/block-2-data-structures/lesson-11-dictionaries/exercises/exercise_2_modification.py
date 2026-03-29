"""
Вправа 2: Модифікація словників.
Запуск: pytest exercise_2_modification.py -v
"""


def test_add_key():
    """Додати ключ 'email'."""
    user = {"name": "Alice"}
    # TODO: замініть pass на:
    #   user["email"] = "alice@test.com"
    #   assert user["email"] == "alice@test.com"
    pass


def test_update_value():
    """Змінити role на 'admin'."""
    user = {"name": "Alice", "role": "user"}
    # TODO: замініть pass на:
    #   user["role"] = "admin"
    #   assert user["role"] == "admin"
    pass


def test_delete_key():
    """Видалити ключ 'age'."""
    user = {"name": "Alice", "age": 25, "role": "admin"}
    # TODO: замініть pass на:
    #   del user["age"]
    #   assert "age" not in user
    pass


def test_pop_key():
    """pop повертає значення та видаляє ключ."""
    user = {"name": "Alice", "role": "admin"}
    # TODO: замініть pass на:
    #   role = user.pop("role")
    #   assert role == "admin"
    #   assert "role" not in user
    pass


def test_update_multiple():
    """update() додає кілька ключів."""
    config = {"host": "localhost"}
    # TODO: замініть pass на:
    #   config.update({"port": 8080, "debug": True})
    #   assert config == {"host": "localhost", "port": 8080, "debug": True}
    pass