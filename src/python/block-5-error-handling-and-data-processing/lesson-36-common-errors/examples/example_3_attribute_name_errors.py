"""Приклад 3: AttributeError та NameError. Запуск: pytest example_3_attribute_name_errors.py -v"""

import pytest


def upper_or_none(value):
    """Викликати .upper() лише коли value не None."""
    if value is None:
        return None
    return value.upper()


def get_username(response):
    """Дістати ім'я користувача з вкладеного поля API-відповіді."""
    user = response.get("user")
    if user is None:
        return "guest"
    return user.get("name", "guest")


def test_attribute_error_none():
    # None не має методу foo
    with pytest.raises(AttributeError):
        None.foo()


def test_attribute_error_str():
    # str не має методу append
    with pytest.raises(AttributeError):
        "x".append("y")


def test_upper_or_none():
    assert upper_or_none("alice") == "ALICE"
    assert upper_or_none(None) is None


def _use_undefined_name():
    # друкарська помилка: змінну usename ніде не визначено
    return usename  # noqa: F821


def test_name_error():
    # звернення до невизначеної змінної кидає NameError у момент виконання
    with pytest.raises(NameError):
        _use_undefined_name()


def test_get_username():
    assert get_username({"user": {"name": "Alice"}}) == "Alice"
    assert get_username({"user": None}) == "guest"
    assert get_username({}) == "guest"
