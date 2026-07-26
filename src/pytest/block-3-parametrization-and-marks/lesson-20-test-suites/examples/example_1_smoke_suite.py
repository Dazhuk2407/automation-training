"""
Приклад 1: Smoke-набір — невелика підмножина критичних тестів.

Smoke відповідає на питання "чи система взагалі жива?".
Тести швидкі та покривають лише критичні шляхи.

Запуск усього файлу:   pytest example_1_smoke_suite.py -v
Запуск тільки smoke:   pytest example_1_smoke_suite.py -m smoke -v
"""

import pytest


@pytest.mark.smoke
def test_homepage_status_ok():
    """Головна сторінка відповідає 200 — критичний шлях."""
    status = 200
    assert status == 200


@pytest.mark.smoke
def test_login_accepts_valid_user():
    """Логін валідного користувача проходить — критичний шлях."""
    user = {"name": "Alice", "logged_in": True}
    assert user["logged_in"] is True


@pytest.mark.smoke
def test_api_health_check():
    """Health-check ендпоінт живий — критичний шлях."""
    health = {"status": "ok"}
    assert health["status"] == "ok"


@pytest.mark.smoke
@pytest.mark.critical
def test_database_connection():
    """Підключення до БД встановлюється — критичний шлях."""
    connected = True
    assert connected
