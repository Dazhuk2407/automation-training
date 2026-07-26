"""
Приклад 1: Базовий parametrize — один тест, багато наборів даних.

Один @pytest.mark.parametrize замінює кілька майже однакових тест-функцій.
Кожен кортеж у списку стає окремим тест-кейсом у звіті.

Запуск: pytest example_1_basic_parametrize.py -v
"""

import pytest


@pytest.mark.parametrize("n,expected", [(2, 4), (3, 9), (4, 16), (5, 25)])
def test_square(n, expected):
    """Квадрат числа — 4 кейси замість 4 окремих функцій."""
    assert n * n == expected


@pytest.mark.parametrize("value,expected", [
    (0, True),
    (2, True),
    (100, True),
    (1, False),
    (3, False),
])
def test_is_even(value, expected):
    """Парність числа: звичайні та межові входи в одному тесті."""
    assert (value % 2 == 0) == expected


@pytest.mark.parametrize("text,expected", [
    ("hello", "HELLO"),
    ("PyTest", "PYTEST"),
    ("", ""),
])
def test_upper(text, expected):
    """Кожен набір даних розгортається в окремий тест-кейс."""
    assert text.upper() == expected
