"""
Вправа 3: Виправити падаючий тест.

Крок 1: Запустіть файл — один тест навмисно падає.
Крок 2: Прочитайте вивід pytest — яке значення фікстура повертає насправді?
Крок 3: Виправте assert так, щоб тест проходив.
Крок 4: Заповніть блок ВІДПОВІДЬ.

Запуск: pytest exercise_3_fix_usage.py -v
"""

import pytest


@pytest.fixture
def config():
    return {"base_url": "https://api.example.com", "timeout": 30}


@pytest.fixture
def client(config):
    """client будується на основі config (fixture requesting fixture)."""
    return {"base_url": config["base_url"], "timeout": config["timeout"]}


def test_client_timeout(client):
    """Цей тест падає — фікстура повертає не те значення, яке очікує assert."""
    # TODO: Виправте очікуване значення відповідно до того, що повертає config/client
    assert client["timeout"] == 60


def test_client_url(client):
    """Цей тест працює правильно."""
    assert client["base_url"] == "https://api.example.com"


def test_url_is_https(client):
    """Цей тест працює правильно."""
    assert client["base_url"].startswith("https://")


# ВІДПОВІДЬ:
# У test_client_timeout фікстура повертає timeout = _______________
# pytest показав: _______________
# Я виправив assert на: _______________
