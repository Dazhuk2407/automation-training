"""
Приклад 1: Фікстура як параметр тесту + незалежність тестів.

pytest бачить ім'я параметра → шукає фікстуру з таким іменем → підставляє результат.
Кожен тест отримує СВІЙ екземпляр результату фікстури.

Запуск: pytest example_1_fixture_as_param.py -v
"""

import pytest


@pytest.fixture
def username():
    """Проста фікстура, що повертає значення."""
    return "alice"


@pytest.fixture
def cart():
    """Новий порожній список для КОЖНОГО тесту."""
    return []


def test_username_is_passed(username):
    """pytest підставив результат фікстури `username` як параметр."""
    assert username == "alice"


def test_username_type(username):
    """Ту саму фікстуру можна використати в іншому тесті."""
    assert isinstance(username, str)


def test_add_to_cart(cart):
    """Змінюємо cart у цьому тесті."""
    cart.append("apple")
    cart.append("banana")
    assert len(cart) == 2


def test_cart_is_fresh(cart):
    """cart тут — НОВИЙ список: зміни з попереднього тесту не протекли."""
    assert cart == []
    assert len(cart) == 0


def test_cart_independent_again(cart):
    """Ще раз переконуємось: кожен тест отримує власний екземпляр."""
    cart.append("only-here")
    assert cart == ["only-here"]
