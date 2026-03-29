"""Приклад 1: One-line docstrings. Запуск: pytest example_1_oneline.py -v"""


def is_even(n):
    """Повернути True якщо n парне."""
    return n % 2 == 0

def is_positive(n):
    """Перевірити чи число позитивне."""
    return n > 0

def double(n):
    """Подвоїти число."""
    return n * 2

def test_is_even():
    """Перевірити парність."""
    assert is_even(4) is True
    assert is_even(7) is False

def test_is_positive():
    """Перевірити позитивність."""
    assert is_positive(5) is True
    assert is_positive(-3) is False

def test_double():
    """Перевірити подвоєння."""
    assert double(5) == 10