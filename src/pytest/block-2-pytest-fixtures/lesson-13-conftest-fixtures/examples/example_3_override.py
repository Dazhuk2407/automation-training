"""
Приклад 3: Перекриття (override) conftest-фікстури.

У conftest.py sample_user = Alice/admin.
Тут ми оголошуємо ЛОКАЛЬНУ фікстуру з тим самим ім'ям —
для тестів цього файлу вона перекриває conftest-версію.

Запуск: pytest example_3_override.py -v
"""

import pytest


@pytest.fixture
def sample_user():
    """Локальна фікстура перекриває conftest-фікстуру з тим самим ім'ям."""
    return {"name": "Bob", "role": "guest"}


def test_local_override_wins(sample_user):
    """У цьому файлі виграє локальна фікстура — Bob, не Alice."""
    assert sample_user["name"] == "Bob"
    assert sample_user["role"] == "guest"


def test_config_still_from_conftest(app_config):
    """app_config НЕ перекрито — приходить із conftest як завжди."""
    assert app_config["base_url"] == "https://api.example.com"
