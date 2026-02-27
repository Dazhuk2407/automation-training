"""
Lesson 4: Example 1 - Correct Test Naming
Демонстрація правильних назв тестів
"""


# ✅ ПРАВИЛЬНІ назви функцій
def test_addition():
    """Тест додавання."""
    assert 2 + 2 == 4


def test_subtraction():
    """Тест віднімання."""
    assert 5 - 3 == 2


def test_string_uppercase():
    """Тест перетворення в upper case."""
    assert "hello".upper() == "HELLO"


# ❌ НЕПРАВИЛЬНІ назви (pytest НЕ знайде ці функції)
def addition_test():  # Не починається з test_
    assert 2 + 2 == 4


def verify_subtraction():  # Не починається з test_
    assert 5 - 3 == 2


def check_uppercase():  # Не починається з test_
    assert "hello".upper() == "HELLO"


# Запустіть: pytest -v
# pytest знайде тільки 3 тести (test_*)

