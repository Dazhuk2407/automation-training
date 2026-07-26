"""
Спільні фікстури для вправ Lesson 13.

Pytest автоматично підхоплює цей файл. У вправах ви використовуєте
фікстури нижче БЕЗ import — просто просіть їх як аргументи тестів.
"""

import pytest


@pytest.fixture
def sample_user():
    """Тестовий користувач."""
    return {"name": "Alice", "role": "admin", "age": 30}


@pytest.fixture
def app_config():
    """Конфігурація застосунку."""
    return {"base_url": "https://api.example.com", "timeout": 5, "retries": 3}


@pytest.fixture
def test_data():
    """Набір тестових даних."""
    return {
        "product": {"id": 42, "name": "Keyboard", "price": 9.99},
        "cart": ["Keyboard", "Mouse"],
    }
