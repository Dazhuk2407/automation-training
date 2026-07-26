"""
Вправа 2: Рефакторинг фікстури-"комбайна" у маленькі композовані фікстури.

Було (АНТИ-ПАТЕРН) — одна фікстура робить усе одразу:

    @pytest.fixture
    def everything():
        user = {"name": "Alice"}
        client = {"user": user, "base_url": "https://example.test"}
        session = {"client": client, "token": "session-abc"}
        return user, client, session

Стало — три маленькі фікстури з однією відповідальністю кожна,
що компонуються: user -> client(user) -> authed_session(client).

Ваше завдання:
  1. Допишіть тіла трьох фікстур нижче (заміна pass на return ...).
  2. Замініть pass у тестах на потрібні assert.

("token"/"session-abc" — фейкові рядки-приклади, не справжні креденшели.)

Запуск: pytest exercise_2_refactor.py -v
"""

import pytest


@pytest.fixture
def user():
    """Готує ОДНУ річ — користувача."""
    # TODO: замініть pass на: return {"name": "Alice"}
    pass


@pytest.fixture
def client(user):
    """Бере user і додає шар клієнта."""
    # TODO: замініть pass на: return {"user": user, "base_url": "https://example.test"}
    pass


@pytest.fixture
def authed_session(client):
    """Компонується з client, додає фейковий токен сесії."""
    # TODO: замініть pass на: return {"client": client, "token": "session-abc"}
    pass


def test_user_name(user):
    """user повертає Alice."""
    # TODO: замініть pass на: assert user["name"] == "Alice"
    pass


def test_client_has_user(client):
    """client містить user."""
    # TODO: замініть pass на: assert client["user"]["name"] == "Alice"
    pass


def test_client_base_url(client):
    """client має base_url."""
    # TODO: замініть pass на: assert client["base_url"] == "https://example.test"
    pass


def test_session_composition(authed_session):
    """authed_session бачить user крізь усі шари."""
    # TODO: замініть pass на: assert authed_session["client"]["user"]["name"] == "Alice"
    pass


def test_session_token(authed_session):
    """authed_session має токен-приклад."""
    # TODO: замініть pass на: assert authed_session["token"] == "session-abc"
    pass
