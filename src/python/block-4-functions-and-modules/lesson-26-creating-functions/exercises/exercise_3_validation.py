"""
Вправа 3: Функції валідації.
Запуск: pytest exercise_3_validation.py -v
"""


def is_valid_email(email):
    """True якщо email не порожній і містить '@'."""
    # TODO: замініть pass на: return bool(email) and "@" in email
    pass


def validate_password(pwd):
    """True якщо >= 8 символів і є хоча б одна цифра."""
    # TODO: замініть pass на:
    #   return len(pwd) >= 8 and any(c.isdigit() for c in pwd)
    pass


def is_valid_age(age):
    """True якщо 0 <= age <= 150."""
    # TODO: замініть pass на: return 0 <= age <= 150
    pass


def test_email_valid():
    # TODO: замініть pass на: assert is_valid_email("a@b.com") is True
    pass

def test_email_empty():
    # TODO: замініть pass на: assert is_valid_email("") is False
    pass

def test_password_valid():
    # TODO: замініть pass на: assert validate_password("MyPass123") is True
    pass

def test_password_short():
    # TODO: замініть pass на: assert validate_password("Ab1") is False
    pass

def test_age_valid():
    # TODO: замініть pass на: assert is_valid_age(25) is True
    pass

def test_age_invalid():
    # TODO: замініть pass на: assert is_valid_age(-5) is False
    pass