"""Вправа 1: random. Запуск: pytest exercise_1_random.py -v

Реалізуй функції (прибери pass) і допиши asserts у тестах.
Для детермінованих перевірок став random.seed(N) всередині тесту.
"""
import random


def roll_dice():
    # TODO: return random.randint(1, 6)
    pass


def pick_one(seq):
    # TODO: return random.choice(seq)
    pass


def random_code():
    # TODO: поверни рядок з 4 цифр, напр. f"{random.randint(1000, 9999)}"
    pass


def test_dice_seeded():
    # TODO: random.seed(42)
    # TODO: assert roll_dice() == 6
    pass


def test_dice_in_range():
    # TODO: assert 1 <= roll_dice() <= 6
    pass


def test_pick_one_membership():
    # TODO: assert pick_one(["a", "b", "c"]) in ["a", "b", "c"]
    pass


def test_code_length():
    # TODO: assert len(random_code()) == 4
    pass


def test_code_is_digits():
    # TODO: assert random_code().isdigit()
    pass
