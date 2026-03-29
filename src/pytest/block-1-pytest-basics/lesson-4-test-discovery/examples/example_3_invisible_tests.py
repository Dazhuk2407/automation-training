"""
Приклад 3: Тести, які pytest НЕ знайде.

Запуск: pytest example_3_invisible_tests.py -v
Результат: 0 items collected — pytest нічого не знайшов!

Всі функції тут мають правильну логіку, але НЕПРАВИЛЬНІ назви.
"""


# ❌ Не починається з test_
def check_addition():
    assert 2 + 2 == 4


# ❌ Не починається з test_
def verify_subtraction():
    assert 10 - 3 == 7


# ❌ Клас не починається з Test
class CalculatorChecks:
    def check_multiply(self):
        assert 3 * 4 == 12


# ❌ Клас має __init__ — pytest не створить екземпляр
class TestWithInit:
    def __init__(self):
        self.value = 42

    def test_value(self):
        assert self.value == 42