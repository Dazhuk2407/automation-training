"""
Вправа 3: Фабрика тестових даних.
Запуск: pytest exercise_3_factory.py -v
"""

import copy

BASE_USER = {
    "id": 1,
    "name": "Test User",
    "email": "test@example.com",
    "roles": ["user"],
}


def make_user(**overrides):
    """Фабрика — deepcopy + overrides."""
    user = copy.deepcopy(BASE_USER)
    user.update(overrides)
    return user


def test_default_user():
    """Фабрика повертає user з defaults."""
    # TODO: замініть pass на:
    #   user = make_user()
    #   assert user["name"] == "Test User"
    #   assert user["roles"] == ["user"]
    pass


def test_override_name():
    """make_user(name='Bob') змінює ім'я."""
    # TODO: замініть pass на:
    #   user = make_user(name="Bob")
    #   assert user["name"] == "Bob"
    pass


def test_base_not_modified():
    """Оригінал BASE_USER не змінюється."""
    # TODO: замініть pass на:
    #   user = make_user(name="Changed")
    #   assert BASE_USER["name"] == "Test User"
    pass