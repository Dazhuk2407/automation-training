"""
Вправа 1: Винести дані в набір + parametrize.

Логіка тестів уже написана. Ваше завдання — наповнити набори даних
(списки кортежів) і замінити TODO. У наборі мають бути ГОТОВІ значення,
а не обчислення.

Запуск: pytest exercise_1_datasets.py -v
"""

import pytest


# ---- Логіка, яку перевіряємо ----

def double(x):
    return x * 2


def is_even(x):
    return x % 2 == 0


def add(a, b):
    return a + b


def max_of(a, b):
    return a if a > b else b


# ---- Набори даних: допишіть кортежі ----

DOUBLE_CASES = [
    (2, 4),
    # TODO: додайте ще 2-3 кортежі (вхід, очікуване), напр. (0, 0), (5, 10)
]

EVEN_CASES = [
    (2, True),
    # TODO: додайте кейси, зокрема непарні числа, напр. (3, False), (0, True)
]

SUM_CASES = [
    (1, 1, 2),
    # TODO: додайте ще кортежі (a, b, очікуване), напр. (2, 3, 5), (0, 0, 0)
]

MAX_CASES = [
    (5, 3, 5),
    # TODO: додайте кортежі (a, b, більше), напр. (1, 9, 9), (7, 7, 7)
]


@pytest.mark.parametrize("value,expected", DOUBLE_CASES)
def test_double(value, expected):
    assert double(value) == expected


@pytest.mark.parametrize("value,expected", EVEN_CASES)
def test_is_even(value, expected):
    assert is_even(value) is expected


@pytest.mark.parametrize("a,b,expected", SUM_CASES)
def test_sum(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", MAX_CASES)
def test_max(a, b, expected):
    assert max_of(a, b) == expected
