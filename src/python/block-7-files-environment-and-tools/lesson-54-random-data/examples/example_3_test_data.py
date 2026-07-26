"""Приклад 3: генерація тестових даних. Запуск: pytest example_3_test_data.py -v"""
import random


def random_email():
    return f"user{random.randint(1000, 9999)}@test.com"


def random_user():
    return {
        "name": random.choice(["Alice", "Bob", "Eve"]),
        "age": random.randint(18, 80),
    }


def test_email_format():
    email = random_email()
    assert email.startswith("user")
    assert email.endswith("@test.com")


def test_user_keys():
    user = random_user()
    assert set(user.keys()) == {"name", "age"}
    assert 18 <= user["age"] <= 80


def test_reproducible_with_seed():
    # Однаковий seed → однакові дані (відтворюваність тесту)
    random.seed(1)
    first = random_user()
    random.seed(1)
    second = random_user()
    assert first == second


def test_email_seeded():
    random.seed(123)
    assert random_email() == "user1857@test.com"
