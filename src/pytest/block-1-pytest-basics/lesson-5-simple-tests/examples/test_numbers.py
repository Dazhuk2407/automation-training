"""
Lesson 5: Example 1 - Testing Numbers
"""
import pytest


def test_integer_equality():
    """Тест рівності цілих чисел."""
    x = 10
    y = 10
    assert x == y


def test_integer_comparisons():
    """Тест порівнянь."""
    assert 5 < 10
    assert 15 > 10
    assert 10 <= 10
    assert 10 >= 10
    assert 5 != 10


def test_arithmetic_operations():
    """Тест арифметичних операцій."""
    assert 2 + 3 == 5
    assert 10 - 4 == 6
    assert 3 * 4 == 12
    assert 10 / 2 == 5
    assert 10 // 3 == 3
    assert 10 % 3 == 1
    assert 2 ** 3 == 8


def test_float_equality():
    """Тест float чисел."""
    # ❌ НЕБЕЗПЕЧНО - float precision issues
    # assert 0.1 + 0.2 == 0.3  # може fail!

    # ✅ ПРАВИЛЬНО - використати tolerance
    result = 0.1 + 0.2
    expected = 0.3
    tolerance = 0.0001
    assert abs(result - expected) < tolerance


def test_float_with_approx():
    """Тест float з pytest.approx."""
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 22 / 7 == pytest.approx(3.14, abs=0.01)


def test_negative_numbers():
    """Тест негативних чисел."""
    assert -5 < 0
    assert -10 + 15 == 5
    assert abs(-10) == 10


def test_large_numbers():
    """Тест великих чисел."""
    million = 1_000_000
    assert million == 1000000
    assert million > 999_999


# Запустіть: pytest test_numbers.py -v

