"""
Приклад 1: Реальні тести зі змістовними іменами.

Усі тести проходять. Це матеріал для тренування справжнього -k:

    pytest example_1_named_tests.py -k login -v
    pytest example_1_named_tests.py -k "login and not invalid" -v
    pytest example_1_named_tests.py -k "login or logout" -v

Зверніть увагу на послідовний неймінг: префікс фічі (login_, logout_, signup_)
робить фільтрацію -k передбачуваною.
"""

VALID_USER = "alice"
VALID_TOKEN = "token-ok"


def _try_login(username, token):
    """Спрощений login: повертає True лише для валідної пари (dummy-логіка)."""
    return username == VALID_USER and token == VALID_TOKEN


def test_login_valid():
    """Успішний вхід з правильними даними."""
    assert _try_login("alice", "token-ok") is True


def test_login_invalid_credentials():
    """Вхід з неправильними даними відхилено."""
    assert _try_login("alice", "token-wrong") is False


def test_login_locked_account():
    """Заблокований акаунт не може увійти навіть з валідними даними."""
    account_locked = True
    logged_in = (not account_locked) and _try_login("alice", "token-ok")
    assert logged_in is False


def test_logout_clears_session():
    """Вихід очищає сесію."""
    session = {"user": "alice", "token": "abc"}
    session.clear()
    assert session == {}


def test_signup_creates_user():
    """Реєстрація створює нового користувача."""
    users = []
    users.append({"username": "bob"})
    assert len(users) == 1
    assert users[0]["username"] == "bob"


def test_signup_rejects_duplicate():
    """Реєстрація відхиляє дубльований username."""
    existing = {"alice"}
    new_username = "alice"
    accepted = new_username not in existing
    assert accepted is False
