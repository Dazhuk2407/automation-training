"""
Вправа 2: Негативні кейси та ids.

Кожен набір має покривати позитив І негатив. Хоча б один набір додайте
з ids, щоб вивід читався як звіт. Зверніть увагу на межі (7 vs 8, 0 vs 1).

Запуск: pytest exercise_2_negative.py -v
"""

import pytest


# ---- Логіка, яку перевіряємо ----

def is_non_empty(text):
    return len(text) > 0


def is_strong_password(pwd):
    """Пароль сильний, якщо має щонайменше 8 символів (фейкове правило)."""
    return len(pwd) >= 8


def in_range(n):
    """Число в діапазоні 1..10 включно."""
    return 1 <= n <= 10


def is_valid_username(name):
    """Ім'я валідне, якщо довжина 3..15 символів."""
    return 3 <= len(name) <= 15


# ---- Набори даних: додайте позитив + негатив ----

NON_EMPTY_CASES = [
    ("hello", True),    # позитивний
    ("", False),        # негативний
    # TODO: додайте ще 1-2 кейси (позитивний і/або негативний)
]

PASSWORD_CASES = [
    ("longenough", True),   # позитивний
    ("short", False),       # негативний
    # TODO: додайте межі: 7 символів (False), рівно 8 символів (True)
]

RANGE_CASES = [
    (5, True),      # всередині
    (0, False),     # під межею
    # TODO: додайте межі 1 і 10 (True) та значення за межею, напр. 11 (False)
]

# TODO: додайте ids для читабельного виводу (по одному рядку на кейс)
USERNAME_CASES = [
    ("bob", True),          # рівно 3 символи — межа
    ("al", False),          # 2 символи — під межею
    ("alice", True),        # всередині
]
USERNAME_IDS = [
    "min_edge",
    "too_short",
    "valid_name",
]


@pytest.mark.parametrize("text,expected", NON_EMPTY_CASES)
def test_non_empty(text, expected):
    assert is_non_empty(text) is expected


@pytest.mark.parametrize("pwd,expected", PASSWORD_CASES)
def test_password_strength(pwd, expected):
    assert is_strong_password(pwd) is expected


@pytest.mark.parametrize("n,expected", RANGE_CASES)
def test_in_range(n, expected):
    assert in_range(n) is expected


@pytest.mark.parametrize("name,expected", USERNAME_CASES, ids=USERNAME_IDS)
def test_username_valid(name, expected):
    assert is_valid_username(name) is expected
