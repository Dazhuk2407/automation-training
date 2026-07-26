"""
Приклад 2: Порядок teardown при кількох фікстурах (LIFO).

setup виконується у порядку залежностей,
teardown — у ЗВОРОТНЬОМУ порядку (Last In — First Out).

Запуск: pytest example_2_teardown_order.py -v
"""

import pytest


# Журнал подій, який заповнюють фікстури.
events = []


@pytest.fixture
def outer():
    """Зовнішня фікстура — налаштовується першою, прибирається останньою."""
    events.append("outer setup")
    yield "outer"
    events.append("outer teardown")


@pytest.fixture
def inner(outer):
    """Внутрішня фікстура залежить від outer — прибирається раніше за outer."""
    events.append("inner setup")
    yield "inner"
    events.append("inner teardown")


def test_both_fixtures(inner, outer):
    """Тест використовує обидві фікстури."""
    assert inner == "inner"
    assert outer == "outer"
    # setup обох уже виконано, teardown ще ні
    assert events == ["outer setup", "inner setup"]


def test_teardown_order_is_lifo():
    """
    Після попереднього тесту фікстури прибрались.
    Порядок: outer setup → inner setup → inner teardown → outer teardown.
    """
    assert events == [
        "outer setup",
        "inner setup",
        "inner teardown",   # inner прибрався першим (LIFO)
        "outer teardown",   # outer — останнім
    ]
