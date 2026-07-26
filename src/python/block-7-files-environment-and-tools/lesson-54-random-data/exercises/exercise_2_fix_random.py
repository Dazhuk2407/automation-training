"""Вправа 2: виправ помилку. Запуск: pytest exercise_2_fix_random.py -v

Один тест падає. Знайди баг (позначено # BUG:) і виправ його.
Після виправлення всі тести мають бути зеленими.
"""
import random


def roll_dice():
    # BUG: у кубика 6 граней, а не 5 — виправ верхню межу
    return random.randint(1, 5)


def coin_flip():
    return random.choice(["H", "T"])


def test_dice_seeded_is_six():
    random.seed(42)
    assert roll_dice() == 6


def test_dice_in_range():
    random.seed(1)
    assert all(1 <= roll_dice() <= 6 for _ in range(20))


def test_coin_in_set():
    assert coin_flip() in ("H", "T")


def test_coin_five_flips():
    random.seed(3)
    flips = [coin_flip() for _ in range(5)]
    assert len(flips) == 5 and set(flips) <= {"H", "T"}
