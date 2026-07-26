"""
Приклад 1: Набори даних як окрема структура + parametrize.

Ідея data-driven: логіка тесту одна, дані — окремо, в іменованій структурі.
Додати новий кейс = додати рядок у список, логіку не чіпаємо.

Запуск: pytest example_1_data_sets.py -v
"""

import pytest


# ---- Логіка, яку перевіряємо (ЩО) ----

def apply_discount(price, percent):
    """Порахувати ціну після знижки у відсотках."""
    return price - price * percent / 100


def is_valid_login(user, pwd):
    """Логін валідний, якщо і користувач, і пароль не порожні."""
    return bool(user) and bool(pwd)


# ---- Дані (НА ЧОМУ) — список кортежів ----

DISCOUNT_CASES = [
    (100, 0, 100),
    (100, 10, 90),
    (100, 50, 50),
    (100, 100, 0),
    (200, 25, 150),
]


@pytest.mark.parametrize("price,percent,expected", DISCOUNT_CASES)
def test_discount(price, percent, expected):
    """Одна логіка — багато наборів даних."""
    assert apply_discount(price, percent) == expected


# ---- Дані для логіну (паролі — фейкові приклади валідації) ----

LOGIN_CASES = [
    ("alice", "pass123", True),
    ("bob", "qwerty", True),
    ("", "pass123", False),
    ("carol", "", False),
]


@pytest.mark.parametrize("user,pwd,expected", LOGIN_CASES)
def test_login(user, pwd, expected):
    """Валідність логіну для різних входів."""
    assert is_valid_login(user, pwd) is expected


# ---- Той самий тест з ids для читабельного виводу ----

@pytest.mark.parametrize(
    "user,pwd,expected",
    LOGIN_CASES,
    ids=["valid_alice", "valid_bob", "empty_user", "empty_password"],
)
def test_login_with_ids(user, pwd, expected):
    """Ті самі дані, але вивід читається як звіт завдяки ids."""
    assert is_valid_login(user, pwd) is expected
