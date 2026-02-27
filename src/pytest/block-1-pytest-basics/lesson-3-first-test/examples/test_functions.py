"""
Lesson 3: Example 2 - Testing a Function
"""


# Функція для тестування
def add(a, b):
    """Додати два числа."""
    return a + b


def multiply(a, b):
    """Помножити два числа."""
    return a * b


# Тести
def test_add_positive_numbers():
    """Тест додавання позитивних чисел."""
    result = add(3, 5)
    assert result == 8


def test_add_negative_numbers():
    """Тест додавання негативних чисел."""
    result = add(-3, -5)
    assert result == -8


def test_add_zero():
    """Тест додавання нуля."""
    result = add(5, 0)
    assert result == 5


def test_multiply():
    """Тест множення."""
    result = multiply(4, 5)
    assert result == 20


def test_multiply_by_zero():
    """Тест множення на нуль."""
    result = multiply(10, 0)
    assert result == 0

