"""
Приклад 2: Зміна словників — додавання, оновлення, видалення.

Запуск: pytest example_2_modification.py -v
"""


def test_add_key():
    """Додати новий ключ."""
    user = {"name": "Alice"}
    user["role"] = "admin"
    assert user == {"name": "Alice", "role": "admin"}


def test_update_key():
    """Змінити існуючий ключ."""
    user = {"name": "Alice", "role": "user"}
    user["role"] = "admin"
    assert user["role"] == "admin"


def test_update_multiple():
    """update() оновлює кілька ключів одночасно."""
    config = {"host": "localhost"}
    config.update({"port": 8080, "debug": True})
    assert config == {"host": "localhost", "port": 8080, "debug": True}


def test_delete_key():
    """del видаляє ключ."""
    user = {"name": "Alice", "role": "admin", "age": 25}
    del user["age"]
    assert "age" not in user
    assert len(user) == 2


def test_pop_returns_value():
    """pop видаляє ключ і повертає значення."""
    user = {"name": "Alice", "role": "admin"}
    role = user.pop("role")
    assert role == "admin"
    assert "role" not in user


def test_pop_with_default():
    """pop з default — без KeyError якщо ключа немає."""
    user = {"name": "Alice"}
    email = user.pop("email", "not set")
    assert email == "not set"