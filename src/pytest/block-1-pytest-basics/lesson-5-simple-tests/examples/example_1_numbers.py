"""
Приклад 1: Тести для чисел (int та float).

Запуск: pytest example_1_numbers.py -v
"""

import pytest


def test_equality():
    """Перевірка рівності цілих чисел."""
    assert 2 + 3 == 5
    assert 10 - 4 == 6


def test_comparison():
    """Порівняння чисел."""
    assert 10 > 5
    assert 3 < 7
    assert 10 >= 10
    assert 5 != 10


def test_arithmetic():
    """Арифметичні операції."""
    assert 4 * 5 == 20
    assert 10 // 3 == 3   # ціле ділення
    assert 10 % 3 == 1    # остача
    assert 2 ** 3 == 8    # степінь


def test_negative_numbers():
    """Від'ємні числа."""
    assert -5 < 0
    assert -10 + 15 == 5
    assert abs(-10) == 10


def test_large_numbers():
    """Великі числа (Python підтримує без обмежень)."""
    million = 1_000_000
    assert million == 1000000
    assert million * million == 1_000_000_000_000


def test_float_with_approx():
    """Float порівняння через pytest.approx (правильний спосіб)."""
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 22 / 7 == pytest.approx(3.14, abs=0.01)


def test_float_without_approx_fails():
    """Float порівняння через tolerance (альтернативний спосіб)."""
    result = 0.1 + 0.2
    assert abs(result - 0.3) < 0.0001