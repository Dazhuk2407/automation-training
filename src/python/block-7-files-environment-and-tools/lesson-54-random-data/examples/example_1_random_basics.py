"""Приклад 1: випадкові числа. Запуск: pytest example_1_random_basics.py -v"""
import random


def roll_dice():
    return random.randint(1, 6)


def random_ratio():
    return random.random()


def random_price(low, high):
    return random.uniform(low, high)


def test_dice_seeded():
    random.seed(42)
    assert roll_dice() == 6


def test_dice_in_range():
    random.seed(1)
    assert all(1 <= roll_dice() <= 6 for _ in range(50))


def test_ratio_in_range():
    for _ in range(50):
        r = random_ratio()
        assert 0.0 <= r < 1.0


def test_price_in_range():
    for _ in range(50):
        p = random_price(10.0, 20.0)
        assert 10.0 <= p <= 20.0
