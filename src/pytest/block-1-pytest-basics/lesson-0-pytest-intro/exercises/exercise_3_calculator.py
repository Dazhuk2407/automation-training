"""
Вправа 3: Тестування калькулятора з винятками

Функції add, subtract, divide вже написані.
Ваше завдання — дописати тести.
Для тесту на помилку використайте pytest.raises().

Запуск: pytest exercise_3_calculator.py -v
"""

import pytest


# --- Готові функції (НЕ змінюйте!) ---

def add(a, b):
    """Додати два числа."""
    return a + b


def subtract(a, b):
    """Відняти b від a."""
    return a - b


def divide(a, b):
    """Поділити a на b. Кидає ValueError якщо b == 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# --- Ваші тести (допишіть замість pass) ---

def test_add_positive():
    """add(2, 3) має повернути 5."""
    # TODO: замініть pass на: assert add(2, 3) == 5
    pass


def test_add_negative():
    """add(-1, 1) має повернути 0."""
    # TODO: замініть pass на: assert add(-1, 1) == 0
    pass


def test_subtract():
    """subtract(10, 3) має повернути 7."""
    # TODO: замініть pass на: assert subtract(10, 3) == 7
    pass


def test_divide():
    """divide(10, 2) має повернути 5.0."""
    # TODO: замініть pass на: assert divide(10, 2) == 5.0
    pass


def test_divide_by_zero():
    """divide(10, 0) має кинути ValueError."""
    # TODO: замініть pass на:
    #   with pytest.raises(ValueError):
    #       divide(10, 0)
    pass