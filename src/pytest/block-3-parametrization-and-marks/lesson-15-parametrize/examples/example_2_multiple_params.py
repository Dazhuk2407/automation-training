"""
Приклад 2: Кілька параметрів — кортежі значень.

Параметрів може бути скільки завгодно. Кількість імен у рядку
має збігатися з довжиною кожного кортежу значень.

Запуск: pytest example_2_multiple_params.py -v
"""

import pytest


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (10, 5, 15),
    (0, 0, 0),
    (-1, 1, 0),
    (-4, -6, -10),
])
def test_add(a, b, expected):
    """Три параметри: два входи та очікуваний результат."""
    assert a + b == expected


@pytest.mark.parametrize("a,b,expected", [
    (6, 2, 3),
    (9, 3, 3),
    (10, 4, 2.5),
    (7, 7, 1),
])
def test_divide(a, b, expected):
    """Ділення на різних наборах даних."""
    assert a / b == expected


@pytest.mark.parametrize("age,country,can_vote", [
    (18, "UA", True),
    (17, "UA", False),
    (21, "US", True),
    (16, "US", False),
])
def test_can_vote(age, country, can_vote):
    """Чотири параметри читаються як таблиця даних."""
    result = age >= 18
    assert result == can_vote
