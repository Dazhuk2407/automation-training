"""
Приклад 1: Перша фікстура.

Оголошуємо фікстуру через @pytest.fixture і використовуємо її,
передаючи ім'я фікстури як параметр тесту. Pytest сам викликає
фікстуру і підставляє повернуте значення.

Запуск: pytest example_1_first_fixture.py -v
"""

import pytest


@pytest.fixture
def sample_user():
    """Готує тестового користувача — один раз, в одному місці."""
    return {"name": "Alice", "role": "admin", "active": True}


def test_user_name(sample_user):
    """Тест приймає ім'я фікстури як параметр."""
    assert sample_user["name"] == "Alice"


def test_user_role(sample_user):
    """Той самий користувач доступний іншому тесту."""
    assert sample_user["role"] == "admin"


def test_user_active(sample_user):
    """Значення фікстури — звичайний dict."""
    assert sample_user["active"] is True


def test_user_has_all_keys(sample_user):
    """Перевіряємо структуру підготовлених даних."""
    assert set(sample_user.keys()) == {"name", "role", "active"}
