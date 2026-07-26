"""
Вправа 1: Базовий parametrize.

Декоратор @pytest.mark.parametrize уже наданий.
Замініть pass на правильний assert, використовуючи параметри тесту.

Запуск: pytest exercise_1_parametrize.py -v
"""

import pytest


@pytest.mark.parametrize("n,expected", [(2, 4), (3, 9), (5, 25)])
def test_square(n, expected):
    """Квадрат числа має дорівнювати expected."""
    # TODO: замініть pass на: assert n * n == expected
    pass


@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (10, 5, 15), (0, 0, 0)])
def test_add(a, b, expected):
    """Сума a + b має дорівнювати expected."""
    # TODO: замініть pass на: assert a + b == expected
    pass


@pytest.mark.parametrize("value,expected", [(2, True), (4, True), (3, False)])
def test_is_even(value, expected):
    """Парність value має збігатися з expected."""
    # TODO: замініть pass на: assert (value % 2 == 0) == expected
    pass


@pytest.mark.parametrize("text,expected", [("hi", "HI"), ("PyTest", "PYTEST")])
def test_upper(text, expected):
    """text.upper() має дорівнювати expected."""
    # TODO: замініть pass на: assert text.upper() == expected
    pass


@pytest.mark.parametrize("items,length", [([1, 2, 3], 3), ([], 0), (["a"], 1)])
def test_len(items, length):
    """Довжина items має дорівнювати length."""
    # TODO: замініть pass на: assert len(items) == length
    pass
