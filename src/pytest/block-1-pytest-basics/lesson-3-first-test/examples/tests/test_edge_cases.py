"""
Edge cases: нуль, від'ємні числа, граничні значення.

Запуск з папки examples/:
    pytest tests/test_edge_cases.py -v
"""

from src.calculator import add, subtract, multiply


def test_add_zeros():
    """Додавання нулів."""
    assert add(0, 0) == 0


def test_add_negative():
    """Додавання від'ємних чисел."""
    assert add(-1, -1) == -2


def test_add_mixed():
    """Від'ємне + позитивне."""
    assert add(-5, 10) == 5


def test_subtract_to_negative():
    """Результат від'ємний."""
    assert subtract(3, 10) == -7


def test_subtract_zero():
    """Віднімання від нуля."""
    assert subtract(0, 5) == -5


def test_multiply_by_zero():
    """Множення на нуль."""
    assert multiply(100, 0) == 0


def test_multiply_negatives():
    """Мінус на мінус дає плюс."""
    assert multiply(-3, -4) == 12