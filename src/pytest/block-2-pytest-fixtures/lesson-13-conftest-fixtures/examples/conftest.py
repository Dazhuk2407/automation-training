"""
Спільні фікстури для прикладів Lesson 13.

Pytest автоматично підхоплює цей файл. Приклади в цій теці
використовують фікстури нижче БЕЗ жодного import.
"""

import pytest


@pytest.fixture
def sample_user():
    """Тестовий користувач — доступний усім тестам теки БЕЗ import."""
    return {"name": "Alice", "role": "admin"}


@pytest.fixture
def app_config():
    """Конфігурація застосунку для тестів."""
    return {"base_url": "https://api.example.com", "timeout": 5}


@pytest.fixture
def client(app_config):
    """Фіктивний клієнт — залежить від іншої conftest-фікстури (app_config)."""
    return {"base_url": app_config["base_url"], "session_id": "abc-123"}
