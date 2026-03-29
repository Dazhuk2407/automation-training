"""
Приклад 1: .get() — безпечний доступ до словника.

Запуск: pytest example_1_get_basics.py -v
"""

import pytest


def test_get_existing_key():
    """.get() повертає значення якщо ключ є."""
    user = {"name": "Alice", "role": "admin"}
    assert user.get("name") == "Alice"


def test_get_missing_key_returns_none():
    """.get() повертає None якщо ключа немає."""
    user = {"name": "Alice"}
    assert user.get("email") is None


def test_get_with_default():
    """.get() з default значенням."""
    user = {"name": "Alice"}
    assert user.get("email", "N/A") == "N/A"
    assert user.get("age", 0) == 0


def test_get_does_not_modify_dict():
    """.get() НЕ змінює словник."""
    config = {"host": "localhost"}
    config.get("port", 8080)
    assert "port" not in config  # не додано


def test_bracket_access_raises_keyerror():
    """[] кидає KeyError якщо ключа немає."""
    user = {"name": "Alice"}
    with pytest.raises(KeyError):
        _ = user["email"]


def test_setdefault_adds_key():
    """setdefault() додає ключ якщо його немає."""
    config = {"host": "localhost"}
    config.setdefault("port", 8080)
    assert config["port"] == 8080  # ключ додано