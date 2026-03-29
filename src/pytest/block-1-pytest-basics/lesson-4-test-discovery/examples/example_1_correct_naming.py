"""
Приклад 1: Правильні та неправильні назви тестів.

Запуск: pytest example_1_correct_naming.py -v
Результат: pytest знайде тільки 3 тести (test_*), решту проігнорує.
"""


# ✅ Pytest ЗНАЙДЕ ці функції (починаються з test_)

def test_addition():
    assert 2 + 2 == 4


def test_subtraction():
    assert 10 - 3 == 7


def test_string_upper():
    assert "hello".upper() == "HELLO"


# ❌ Pytest НЕ знайде ці функції (не починаються з test_)

def addition_test():
    assert 2 + 2 == 4


def verify_subtraction():
    assert 10 - 3 == 7


def check_string():
    assert "hello".upper() == "HELLO"