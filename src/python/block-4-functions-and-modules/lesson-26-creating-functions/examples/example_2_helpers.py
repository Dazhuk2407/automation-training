"""
Приклад 2: Helper-функції для валідації та форматування.
Запуск: pytest example_2_helpers.py -v
"""


def is_valid_email(email):
    """Перевірити що email валідний."""
    return bool(email) and "@" in email and "." in email.split("@")[-1]


def is_success_code(code):
    """Перевірити що HTTP код — успішний."""
    return 200 <= code < 300


def format_user(name, role="user"):
    """Створити словник користувача."""
    return {"name": name, "role": role, "active": True}


def calculate_discount(price, percent):
    """Розрахувати ціну зі знижкою."""
    return round(price * (1 - percent / 100), 2)


def test_valid_emails():
    assert is_valid_email("alice@test.com") is True
    assert is_valid_email("") is False
    assert is_valid_email("no-at-sign") is False


def test_success_codes():
    assert is_success_code(200) is True
    assert is_success_code(201) is True
    assert is_success_code(404) is False


def test_format_user():
    user = format_user("Alice", "admin")
    assert user == {"name": "Alice", "role": "admin", "active": True}


def test_discount():
    assert calculate_discount(100, 10) == 90.0
    assert calculate_discount(200, 25) == 150.0
    assert calculate_discount(50, 0) == 50.0