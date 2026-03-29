"""
Приклад 3: Тестування винятків (pytest.raises)

Іноді функція ПОВИННА кинути помилку.
pytest.raises перевіряє, що помилка дійсно виникла.

Запуск: pytest example_3_exceptions.py -v
"""

import pytest


def divide(a, b):
    """Поділити a на b. Кидає ValueError якщо b == 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def get_element(lst, index):
    """Отримати елемент списку. Кидає IndexError якщо індекс невірний."""
    if index >= len(lst) or index < -len(lst):
        raise IndexError(f"Index {index} is out of range")
    return lst[index]


# --- Тести ---

def test_divide_normal():
    """Звичайне ділення працює."""
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    """Ділення на нуль кидає ValueError."""
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_by_zero_message():
    """Перевірити текст помилки."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_get_element_normal():
    """Звичайне отримання елемента працює."""
    assert get_element([10, 20, 30], 1) == 20


def test_get_element_out_of_range():
    """Невірний індекс кидає IndexError."""
    with pytest.raises(IndexError):
        get_element([10, 20, 30], 10)