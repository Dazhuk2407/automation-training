"""Вправа 1: безпечні функції та розпізнавання винятків. Запуск: pytest exercise_1_identify.py -v"""

import pytest


def safe_int(text, default=0):
    # TODO: return int(text), а при ValueError/TypeError -> default
    pass

def safe_get(data, key, default=None):
    # TODO: return data.get(key, default)
    pass

def safe_divide(a, b, default=0):
    # TODO: якщо b == 0 -> default, інакше a / b
    pass

def test_safe_int_ok():
    # TODO: assert safe_int("42") == 42
    pass

def test_safe_int_bad():
    # TODO: assert safe_int("abc") == 0
    pass

def test_safe_get():
    # TODO: assert safe_get({"name": "Alice"}, "age", 0) == 0
    pass

def test_safe_divide():
    # TODO: assert safe_divide(10, 2) == 5 та safe_divide(10, 0) == 0
    pass

def test_raises_value_error():
    # TODO: with pytest.raises(ValueError): int("abc")
    pass
