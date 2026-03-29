"""
Приклад 1: Створення та виклик функцій.
Запуск: pytest example_1_basics.py -v
"""


def add(a, b):
    """Додати два числа."""
    return a + b


def greet(name):
    """Привітати користувача."""
    return f"Hello, {name}!"


def is_positive(n):
    """Чи позитивне число."""
    return n > 0


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-3) is False
    assert is_positive(0) is False


def test_no_return():
    """Функція без return повертає None."""
    def log(msg):
        _ = msg  # просто щось робить

    result = log("test")
    assert result is None