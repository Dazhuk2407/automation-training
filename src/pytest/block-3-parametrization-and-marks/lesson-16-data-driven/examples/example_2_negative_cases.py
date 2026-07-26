"""
Приклад 2: Позитивні І негативні кейси в одному наборі.

Тест лише на валідних входах — ілюзія покриття. Баги живуть на невалідних:
порожній рядок, відсутній формат, значення за межею. Кладемо обидва боки
в один набір і додаємо ids.

Запуск: pytest example_2_negative_cases.py -v
"""

import pytest


# ---- Логіка, яку перевіряємо ----

def is_valid_email(email):
    """Дуже спрощена валідація: рівно один '@' і непорожні частини."""
    if email.count("@") != 1:
        return False
    local, _, domain = email.partition("@")
    return bool(local) and bool(domain)


def has_access(age):
    """Доступ дозволено з 18 років включно."""
    return age >= 18


# ---- Email: позитив + негатив ----

EMAIL_CASES = [
    ("alice@example.com", True),
    ("bob@test.org", True),
    ("no-at-sign", False),
    ("", False),
    ("@example.com", False),
    ("alice@", False),
    ("a@@b.com", False),
]

EMAIL_IDS = [
    "valid_dotcom",
    "valid_dotorg",
    "missing_at",
    "empty_string",
    "empty_local",
    "empty_domain",
    "double_at",
]


@pytest.mark.parametrize("email,expected", EMAIL_CASES, ids=EMAIL_IDS)
def test_email_validation(email, expected):
    """Валідні й невалідні email в одному наборі."""
    assert is_valid_email(email) is expected


# ---- Межі як дані: правило "18+" ----

AGE_CASES = [
    (0, False),
    (17, False),
    (18, True),
    (19, True),
    (100, True),
]


@pytest.mark.parametrize(
    "age,allowed",
    AGE_CASES,
    ids=["zero", "under_edge", "on_edge", "over_edge", "old"],
)
def test_access_by_age(age, allowed):
    """Межі 17 vs 18 ловлять помилку > замість >=."""
    assert has_access(age) is allowed
