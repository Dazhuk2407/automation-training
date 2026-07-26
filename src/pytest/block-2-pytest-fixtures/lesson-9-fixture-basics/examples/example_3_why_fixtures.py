"""
Приклад 3: Навіщо фікстури — «до» і «після».

Спочатку — три тести з дублюванням setup-коду.
Потім — ті самі тести, але підготовка даних винесена у фікстуру.
Усі тести проходять; порівняйте кількість повторюваного коду.

Запуск: pytest example_3_why_fixtures.py -v
"""

import pytest


# ============================================================
# ДО: дублювання — той самий user копіюється у кожен тест
# ============================================================

def test_before_name():
    user = {"name": "Alice", "role": "admin", "active": True}  # setup
    assert user["name"] == "Alice"


def test_before_role():
    user = {"name": "Alice", "role": "admin", "active": True}  # той самий setup
    assert user["role"] == "admin"


def test_before_active():
    user = {"name": "Alice", "role": "admin", "active": True}  # знову те саме
    assert user["active"] is True


# ============================================================
# ПІСЛЯ: setup один раз у фікстурі, тести лише споживають
# ============================================================

@pytest.fixture
def user():
    """Підготовка даних живе в одному місці."""
    return {"name": "Alice", "role": "admin", "active": True}


def test_after_name(user):
    assert user["name"] == "Alice"


def test_after_role(user):
    assert user["role"] == "admin"


def test_after_active(user):
    assert user["active"] is True


# ============================================================
# Бонус: ізоляція — кожен тест отримує свіже значення
# ============================================================

@pytest.fixture
def items():
    return [1, 2, 3]


def test_isolation_modifies(items):
    """Цей тест змінює список..."""
    items.append(4)
    assert items == [1, 2, 3, 4]


def test_isolation_fresh(items):
    """...а цей отримує свіжий, бо фікстура викликається заново."""
    assert items == [1, 2, 3]
