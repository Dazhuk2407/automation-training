"""
Приклад 1: Ізоляція — function-scope дає свіжі дані кожному тесту.

Обидва тести мутують ту саму фікстуру, але НЕ впливають один на одного,
бо function-scope створює її заново для кожного тесту.

Запуск: pytest example_1_isolation.py -v
"""

import pytest


@pytest.fixture
def sample_user():
    """Свіжий користувач для КОЖНОГО тесту (function-scope за замовчуванням)."""
    return {"name": "Alice", "roles": ["viewer"]}


@pytest.fixture
def cart():
    """Порожній кошик — новий об'єкт на кожен тест."""
    return []


def test_add_role_mutates_local_copy(sample_user):
    """Тест змінює дані фікстури..."""
    sample_user["roles"].append("admin")
    assert sample_user["roles"] == ["viewer", "admin"]


def test_user_is_fresh(sample_user):
    """...а цей тест бачить свіжого користувача, без змін попереднього тесту."""
    assert sample_user["roles"] == ["viewer"]


def test_cart_starts_empty_first(cart):
    """Кошик порожній на старті."""
    cart.append("item-1")
    assert len(cart) == 1


def test_cart_starts_empty_again(cart):
    """Кошик знову порожній — ізоляція працює."""
    assert cart == []
