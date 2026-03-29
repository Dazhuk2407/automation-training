"""
Приклад 1: Основи словників — створення, доступ, перевірка ключів.

Запуск: pytest example_1_basics.py -v
"""


def test_create_dict():
    """Створення словника."""
    user = {"name": "Alice", "role": "admin", "active": True}
    assert len(user) == 3


def test_access_by_key():
    """Доступ за ключем."""
    config = {"host": "localhost", "port": 8080}
    assert config["host"] == "localhost"
    assert config["port"] == 8080


def test_key_existence():
    """Перевірка наявності ключа."""
    user = {"name": "Alice", "role": "admin"}
    assert "name" in user
    assert "email" not in user


def test_in_checks_keys_not_values():
    """in перевіряє ключі, а не значення."""
    user = {"name": "Alice"}
    assert "name" in user          # ключ — True
    assert "Alice" not in user     # значення — False для in
    assert "Alice" in user.values()  # так перевіряють значення


def test_dict_from_list_of_tuples():
    """Створення словника зі списку пар."""
    pairs = [("status", 200), ("message", "OK")]
    result = dict(pairs)
    assert result == {"status": 200, "message": "OK"}