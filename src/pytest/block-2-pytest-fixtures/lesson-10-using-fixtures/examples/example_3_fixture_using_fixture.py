"""
Приклад 3: Фікстура, що використовує іншу фікстуру (ланцюг фікстур).

Фікстура сама може приймати інші фікстури як параметри.
Патерн QA: `client`, що залежить від `config`.

Запуск: pytest example_3_fixture_using_fixture.py -v
"""

import pytest


@pytest.fixture
def config():
    """Базові налаштування."""
    return {"base_url": "https://api.example.com", "timeout": 30}


@pytest.fixture
def client(config):
    """client будується НА ОСНОВІ config (fixture requesting fixture)."""
    return {
        "base_url": config["base_url"],
        "timeout": config["timeout"],
        "session_id": "sess-001",
        "connected": True,
    }


@pytest.fixture
def session(client):
    """Ще один шар ланцюга: session залежить від client."""
    return {"client": client, "token": "tok-123"}


def test_client_connected(client):
    """client приходить уже зібраним — ланцюг config → client виконано."""
    assert client["connected"] is True


def test_client_uses_config_values(client):
    """Значення з config опинилися всередині client."""
    assert client["base_url"] == "https://api.example.com"
    assert client["timeout"] == 30


def test_url_is_https(client):
    """URL — лише https:// (без реальної мережі)."""
    assert client["base_url"].startswith("https://")


def test_session_chain(session):
    """Ланцюг з трьох шарів: config → client → session."""
    assert session["token"] == "tok-123"
    assert session["client"]["connected"] is True
