"""
Вправа 2: Кілька фікстур в одному тесті.

Прийміть потрібні фікстури як параметри (порядок не має значення)
і замініть pass на правильний assert.

Запуск: pytest exercise_2_multiple.py -v
"""

import pytest


@pytest.fixture
def user():
    return {"name": "alice", "role": "admin"}


@pytest.fixture
def config():
    return {"timeout": 30, "retries": 3}


@pytest.fixture
def base_url():
    return "https://api.example.com"


def test_user_role(user):
    """Роль користувача — 'admin'."""
    # TODO: замініть pass на: assert user["role"] == "admin"
    pass


def test_config_timeout(config):
    """timeout дорівнює 30."""
    # TODO: замініть pass на: assert config["timeout"] == 30
    pass


def test_user_and_config(user, config):
    """Дві фікстури разом: ім'я 'alice' та retries == 3."""
    # TODO: замініть pass на два assert:
    #   assert user["name"] == "alice"
    #   assert config["retries"] == 3
    pass


def test_url_is_https(base_url):
    """URL починається з 'https://'."""
    # TODO: замініть pass на: assert base_url.startswith("https://")
    pass


def test_all_three(user, config, base_url):
    """Три фікстури в одному тесті."""
    # TODO: замініть pass на три assert:
    #   assert user["role"] == "admin"
    #   assert config["timeout"] == 30
    #   assert base_url.startswith("https://")
    pass
