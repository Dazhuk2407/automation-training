"""Приклад 2: Multi-line docstrings (Google style). Запуск: pytest example_2_multiline.py -v"""

import pytest


def create_user(name, role="user"):
    """Створити словник користувача.

    Args:
        name: Ім'я користувача.
        role: Роль (за замовчуванням "user").

    Returns:
        Словник з полями name, role, active.

    Raises:
        ValueError: Якщо name порожній.
    """
    if not name:
        raise ValueError("Name cannot be empty")
    return {"name": name, "role": role, "active": True}


def calculate_discount(price, percent):
    """Розрахувати ціну зі знижкою.

    Args:
        price: Початкова ціна.
        percent: Відсоток знижки (0-100).

    Returns:
        Ціна після знижки.
    """
    return round(price * (1 - percent / 100), 2)


def test_create_user():
    user = create_user("Alice", "admin")
    assert user["name"] == "Alice"

def test_create_user_empty_name():
    with pytest.raises(ValueError, match="empty"):
        create_user("")

def test_discount():
    assert calculate_discount(100, 10) == 90.0