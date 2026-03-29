"""
Приклад 2: Фабрика тестових даних з deepcopy.

Запуск: pytest example_2_data_factory.py -v
"""

import copy


BASE_USER = {
    "id": 1,
    "name": "Test User",
    "email": "test@example.com",
    "roles": ["user"],
    "settings": {"theme": "light", "notifications": True},
}


def make_user(**overrides):
    """Фабрика користувача з можливістю overrides."""
    user = copy.deepcopy(BASE_USER)
    user.update(overrides)
    return user


def test_default_user():
    user = make_user()
    assert user["name"] == "Test User"
    assert user["roles"] == ["user"]


def test_admin_user():
    user = make_user(name="Admin", roles=["admin"])
    assert user["name"] == "Admin"
    assert "admin" in user["roles"]


def test_custom_email():
    user = make_user(email="custom@test.com")
    assert user["email"] == "custom@test.com"


def test_base_not_modified():
    """Фабрика не змінює BASE_USER."""
    user = make_user(name="Changed")
    assert BASE_USER["name"] == "Test User"


def test_two_users_independent():
    u1 = make_user(name="Alice")
    u2 = make_user(name="Bob")
    u1["roles"].append("admin")
    assert "admin" not in u2["roles"]