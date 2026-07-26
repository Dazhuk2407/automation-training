"""
Приклад 2: Кілька фікстур в одному тесті.

Перелічіть імена фікстур як параметри — порядок не має значення,
pytest шукає їх за іменем.

Запуск: pytest example_2_multiple_fixtures.py -v
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


def test_two_fixtures(user, config):
    """Тест приймає дві фікстури одночасно."""
    assert user["role"] == "admin"
    assert config["timeout"] == 30


def test_three_fixtures(user, config, base_url):
    """Три фікстури в одному тесті."""
    assert user["name"] == "alice"
    assert config["retries"] == 3
    assert base_url.startswith("https://")


def test_order_does_not_matter(config, user):
    """Порядок параметрів довільний — pytest шукає за іменем."""
    assert user["name"] == "alice"
    assert config["timeout"] == 30


def test_only_what_is_needed(base_url):
    """Беремо лише ту фікстуру, яка дійсно потрібна тесту."""
    assert base_url == "https://api.example.com"
