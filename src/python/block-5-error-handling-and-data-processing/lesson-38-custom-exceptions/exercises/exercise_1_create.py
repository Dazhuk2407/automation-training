"""Вправа 1: створити власні винятки. Запуск: pytest exercise_1_create.py -v"""

import pytest


# TODO: створи клас InvalidEmailError(Exception): pass


# TODO: створи клас InvalidAgeError(Exception): pass


def validate_email(email):
    """Підняти InvalidEmailError, якщо в email немає '@'."""
    # TODO:
    #   if "@" not in email:
    #       raise InvalidEmailError("email must contain @")
    #   return email
    pass


def validate_age(age):
    """Підняти InvalidAgeError, якщо age < 0."""
    # TODO:
    #   if age < 0:
    #       raise InvalidAgeError("age must be positive")
    #   return age
    pass


def test_email_ok():
    # TODO: assert validate_email("a@b.com") == "a@b.com"
    pass


def test_email_raises():
    # TODO:
    #   with pytest.raises(InvalidEmailError):
    #       validate_email("bad-email")
    pass


def test_email_message():
    # TODO:
    #   with pytest.raises(InvalidEmailError, match="@"):
    #       validate_email("bad")
    pass


def test_age_ok():
    # TODO: assert validate_age(25) == 25
    pass


def test_age_raises():
    # TODO:
    #   with pytest.raises(InvalidAgeError):
    #       validate_age(-1)
    pass
