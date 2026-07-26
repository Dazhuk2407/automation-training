"""
Приклад 3: Читабельні ids для тест-кейсів.

За замовчуванням pytest будує id зі значень (наприклад [user@example.com-True]).
Параметр ids=[...] дає власні зрозумілі імена кейсів у звіті.
Довжина ids має дорівнювати кількості наборів даних.

Запуск: pytest example_3_ids.py -v

Порівняйте вивід: у test_email_validation імена читабельні (valid_email, ...),
а в test_login — pytest генерує id автоматично.
"""

import pytest


@pytest.mark.parametrize(
    "email,is_valid",
    [
        ("user@example.com", True),
        ("admin@site.org", True),
        ("no-at-sign", False),
        ("@no-name", True),
        ("", False),
    ],
    ids=["valid_user", "valid_admin", "missing_at", "at_only", "empty"],
)
def test_email_validation(email, is_valid):
    """ids роблять звіт самодокументованим."""
    assert ("@" in email) == is_valid


@pytest.mark.parametrize(
    "password,strong",
    [
        ("abc", False),
        ("password", False),
        ("Str0ng!Pass", True),
    ],
    ids=["too_short", "no_digits", "good_password"],
)
def test_password_strength(password, strong):
    """Зрозумілі імена одразу показують який кейс впав."""
    result = len(password) >= 8 and any(c.isdigit() for c in password)
    assert result == strong


@pytest.mark.parametrize("username,password", [
    ("alice", "1234"),
    ("bob", "qwerty"),
])
def test_login(username, password):
    """Без ids — pytest сам згенерує id зі значень (alice-1234, ...)."""
    assert len(username) > 0
    assert len(password) > 0
