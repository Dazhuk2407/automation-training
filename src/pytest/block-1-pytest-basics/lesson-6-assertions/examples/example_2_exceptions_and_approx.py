"""
Приклад 2: pytest.raises (винятки) та pytest.approx (float).

Запуск: pytest example_2_exceptions_and_approx.py -v
"""

import pytest


# --- Винятки ---

def test_zero_division():
    """ZeroDivisionError при діленні на нуль."""
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0


def test_value_error():
    """ValueError при некоректному перетворенні."""
    with pytest.raises(ValueError):
        int("not a number")


def test_error_message():
    """Перевірка тексту помилки через match."""
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")


# --- Float ---

def test_float_approx():
    """Порівняння float через pytest.approx."""
    assert 0.1 + 0.2 == pytest.approx(0.3)


def test_float_with_tolerance():
    """pytest.approx з явною точністю."""
    assert 22 / 7 == pytest.approx(3.14, abs=0.01)