"""Приклад 2: choice, choices, sample, shuffle. Запуск: pytest example_2_choice_sample.py -v"""
import random

FRUITS = ["apple", "banana", "cherry"]


def pick_one(seq):
    return random.choice(seq)


def pick_many(seq, k):
    return random.choices(seq, k=k)  # з поверненням


def pick_unique(seq, k):
    return random.sample(seq, k)  # без повернення


def shuffled_copy(seq):
    copy = list(seq)
    random.shuffle(copy)  # на місці
    return copy


def test_choice_seeded():
    random.seed(7)
    assert pick_one(FRUITS) == "banana"


def test_choices_length_and_membership():
    result = pick_many(FRUITS, 5)
    assert len(result) == 5
    assert all(item in FRUITS for item in result)


def test_sample_unique():
    result = pick_unique(FRUITS, 3)
    assert len(result) == 3
    assert len(set(result)) == 3  # усі різні


def test_shuffled_copy_keeps_elements():
    original = [1, 2, 3, 4, 5]
    result = shuffled_copy(original)
    assert sorted(result) == original  # ті самі елементи
    assert original == [1, 2, 3, 4, 5]  # оригінал не змінився
