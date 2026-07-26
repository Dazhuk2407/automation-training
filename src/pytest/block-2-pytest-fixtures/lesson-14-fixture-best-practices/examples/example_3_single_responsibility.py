"""
Приклад 3: Одна відповідальність + композиція + зрозумілі імена.

Замість однієї фікстури-"комбайна" будуємо об'єкт шарами:
    user -> client(user) -> authed_session(client)
Кожна фікстура додає рівно один шар і має зрозуміле ім'я.

("token"/"session-abc" — фейкові рядки-приклади, не справжні креденшели.)

Запуск: pytest example_3_single_responsibility.py -v
"""

import pytest


@pytest.fixture
def user():
    """Готує ОДНУ річ — користувача."""
    return {"id": 1, "name": "Alice"}


@pytest.fixture
def admin_user():
    """Окрема зрозуміла фікстура для адміна (ім'я говорить саме за себе)."""
    return {"id": 2, "name": "Bob", "role": "admin"}


@pytest.fixture
def client(user):
    """Бере user і додає шар клієнта — одна відповідальність."""
    return {"user": user, "base_url": "https://example.test"}


@pytest.fixture
def authed_session(client):
    """Компонується з client, додає фейковий токен сесії."""
    return {"client": client, "token": "session-abc"}


def test_user_only(user):
    """Тест просить рівно те, що потрібно — лише user."""
    assert user["name"] == "Alice"


def test_client_wraps_user(client):
    """client коректно містить user."""
    assert client["user"]["name"] == "Alice"
    assert client["base_url"] == "https://example.test"


def test_authed_session_composition(authed_session):
    """Повна композиція шарів user -> client -> authed_session."""
    assert authed_session["client"]["user"]["name"] == "Alice"
    assert authed_session["token"] == "session-abc"


def test_admin_user_name_is_clear(admin_user):
    """Зрозуміле ім'я фікстури робить тест самодокументованим."""
    assert admin_user["role"] == "admin"
