"""Приклад 1: return, None, print vs return. Запуск: pytest example_1_basics.py -v"""


def add(a, b):
    return a + b

def no_return():
    x = 42

def test_return_value():
    assert add(2, 3) == 5

def test_none_without_return():
    assert no_return() is None

def test_return_stops_execution():
    def first_positive(numbers):
        for n in numbers:
            if n > 0:
                return n
        return None
    assert first_positive([-1, -2, 3, 4]) == 3
    assert first_positive([-1, -2]) is None