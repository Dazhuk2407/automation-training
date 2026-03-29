"""
Вправа 3: Тестування винятків через pytest.raises.

Запуск: pytest exercise_3_exceptions.py -v
"""

import pytest


def test_zero_division():
    """10 / 0 має кинути ZeroDivisionError."""
    # TODO: замініть pass на:
    #   with pytest.raises(ZeroDivisionError):
    #       result = 10 / 0
    pass


def test_value_error():
    """int('abc') має кинути ValueError."""
    # TODO: замініть pass на:
    #   with pytest.raises(ValueError):
    #       int("abc")
    pass


def test_key_error():
    """Доступ до неіснуючого ключа має кинути KeyError."""
    # TODO: замініть pass на:
    #   with pytest.raises(KeyError):
    #       d = {}
    #       _ = d["missing"]
    pass


def test_error_message():
    """int('xyz') має кинути ValueError з текстом 'invalid literal'."""
    # TODO: замініть pass на:
    #   with pytest.raises(ValueError, match="invalid literal"):
    #       int("xyz")
    pass