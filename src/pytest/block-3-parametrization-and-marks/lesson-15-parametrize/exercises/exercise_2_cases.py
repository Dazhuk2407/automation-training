"""
Вправа 2: Додайте набори даних.

Тіло тесту вже написане. Ваше завдання — дописати НАБОРИ ДАНИХ
у список parametrize так, щоб покрити звичайні, межові та негативні входи.

Запуск: pytest exercise_2_cases.py -v
"""

import pytest


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    # TODO: додайте ще 2 набори, напр. (10, 5, 15) та (-1, 1, 0)
])
def test_add(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize("age,allowed", [
    (18, True),
    # TODO: додайте межовий (17, False) та звичайний (25, True) кейси
])
def test_can_vote(age, allowed):
    assert (age >= 18) == allowed


@pytest.mark.parametrize("text,expected_len", [
    ("hello", 5),
    # TODO: додайте межовий кейс порожнього рядка ("", 0)
])
def test_length(text, expected_len):
    assert len(text) == expected_len


@pytest.mark.parametrize(
    "email,is_valid",
    [
        ("user@example.com", True),
        # TODO: додайте негативний кейс без "@", напр. ("invalid", False)
    ],
    # TODO: додайте ids=[...] з читабельними іменами для кожного кейсу
)
def test_email(email, is_valid):
    assert ("@" in email) == is_valid


@pytest.mark.parametrize("n,is_positive", [
    (5, True),
    # TODO: додайте межовий (0, False) та негативний (-3, False)
])
def test_is_positive(n, is_positive):
    assert (n > 0) == is_positive
