"""
Приклад 1: Найпростіший тест

Тест — це функція, яка перевіряє що код працює правильно.
Запуск: pytest example_1_simple_test.py -v
"""


def add(a, b):
    """Додати два числа."""
    return a + b


def subtract(a, b):
    """Відняти b від a."""
    return a - b


# --- Тести ---

def test_add():
    """Перевірити додавання."""
    result = add(2, 3)
    assert result == 5


def test_subtract():
    """Перевірити віднімання."""
    result = subtract(10, 4)
    assert result == 6


def test_add_negative_numbers():
    """Перевірити додавання від'ємних чисел."""
    result = add(-2, -3)
    assert result == -5