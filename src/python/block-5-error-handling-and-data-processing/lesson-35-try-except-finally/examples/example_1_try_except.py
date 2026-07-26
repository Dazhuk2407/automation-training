"""Приклад 1: базовий try/except. Запуск: pytest example_1_try_except.py -v"""


def to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0.0

def get_value(data, key):
    try:
        return data[key]
    except KeyError:
        return "missing"

def test_to_int_ok():
    assert to_int("42") == 42
    assert to_int("-7") == -7

def test_to_int_bad():
    assert to_int("abc") is None
    assert to_int("") is None

def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == 0.0

def test_get_value():
    assert get_value({"a": 1}, "a") == 1
    assert get_value({"a": 1}, "b") == "missing"
