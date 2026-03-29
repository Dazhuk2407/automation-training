"""
Базові тести для calculator.py

Запуск з папки examples/:
    pytest tests/test_calculator.py -v
"""

from src.calculator import add, subtract, multiply, divide


def test_add():
    """Додавання двох позитивних чисел."""
    assert add(2, 3) == 5


def test_subtract():
    """Віднімання."""
    assert subtract(10, 4) == 6


def test_multiply():
    """Множення."""
    assert multiply(3, 4) == 12


def test_divide():
    """Ділення."""
    assert divide(10, 2) == 5.0