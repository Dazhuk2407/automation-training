"""
Приклад 1: Арифметичні оператори та порівняння.
Запуск: pytest example_1_arithmetic.py -v
"""


def test_basic_arithmetic():
    assert 10 + 5 == 15
    assert 10 - 3 == 7
    assert 4 * 5 == 20
    assert 10 / 3 == 10 / 3  # float


def test_integer_division():
    assert 10 // 3 == 3
    assert 7 // 2 == 3
    assert -7 // 2 == -4  # floor division


def test_modulo():
    assert 10 % 3 == 1
    assert 15 % 5 == 0
    assert 7 % 2 == 1  # непарне


def test_power():
    assert 2 ** 3 == 8
    assert 10 ** 0 == 1
    assert 3 ** 2 == 9


def test_comparisons():
    assert 5 == 5
    assert 5 != 3
    assert 5 > 3
    assert 3 < 5
    assert 5 >= 5
    assert 5 <= 5


def test_chained_comparisons():
    x = 5
    assert 1 < x < 10
    assert 0 <= x <= 100