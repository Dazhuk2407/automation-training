"""Приклад 1: найпростіший власний виняток. Запуск: pytest example_1_basic_custom.py -v"""

import pytest


class ValidationError(Exception):
    pass


def validate_age(age):
    if age < 0:
        raise ValidationError("age must be positive")
    return age


def validate_email(email):
    if "@" not in email:
        raise ValidationError("email invalid")
    return email


def test_valid_age():
    assert validate_age(25) == 25


def test_raises_on_negative():
    with pytest.raises(ValidationError):
        validate_age(-1)


def test_message():
    with pytest.raises(ValidationError, match="positive"):
        validate_age(-5)


def test_email_message():
    with pytest.raises(ValidationError, match="invalid"):
        validate_email("bad-email")


def test_str_of_exception():
    try:
        validate_age(-3)
    except ValidationError as e:
        assert str(e) == "age must be positive"
