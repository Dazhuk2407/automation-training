"""
Вправа 3: Виправ неправильний кейс у наборі даних.

Логіка функцій правильна. Але один рядок у наборі даних містить
НЕПРАВИЛЬНЕ очікуване значення — через це рівно один кейс падає.

Крок 1: Запустіть файл — рівно один кейс падає.
Крок 2: Прочитайте вивід pytest: який id/параметри кейса впав.
Крок 3: Виправте ДАНІ (очікуване значення), не чіпаючи логіку тесту.
Крок 4: Заповніть блок ВІДПОВІДЬ.

Запуск: pytest exercise_3_fix_data.py -v
"""

import pytest


# ---- Логіка, яку перевіряємо (правильна) ----

def double(x):
    return x * 2


def is_positive(n):
    return n > 0


def word_length(word):
    return len(word)


# ---- Дані ----

DOUBLE_CASES = [
    (2, 4),
    (0, 0),
    (5, 10),
]

# ⚠️ Один із цих рядків має неправильне очікуване значення
POSITIVE_CASES = [
    (5, True),
    (-3, False),
    (0, False),
    (10, False),   # <-- 10 є додатнім, тож тут має бути True
]

LENGTH_CASES = [
    ("a", 1),
    ("test", 4),
    ("pytest", 6),
]


@pytest.mark.parametrize("value,expected", DOUBLE_CASES)
def test_double(value, expected):
    assert double(value) == expected


@pytest.mark.parametrize("n,expected", POSITIVE_CASES)
def test_is_positive(n, expected):
    assert is_positive(n) is expected


@pytest.mark.parametrize("word,expected", LENGTH_CASES)
def test_word_length(word, expected):
    assert word_length(word) == expected


# ВІДПОВІДЬ:
# Впав кейс: _______________
# Неправильне очікуване значення було: _______________
# Правильне значення: _______________
