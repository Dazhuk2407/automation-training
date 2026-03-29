"""
Модуль калькулятора.

Код програми живе в src/.
Тести для нього — у tests/test_calculator.py.
"""


def add(a, b):
    """Додати два числа."""
    return a + b


def subtract(a, b):
    """Відняти b від a."""
    return a - b


def multiply(a, b):
    """Помножити два числа."""
    return a * b


def divide(a, b):
    """Поділити a на b. Кидає ValueError якщо b == 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b