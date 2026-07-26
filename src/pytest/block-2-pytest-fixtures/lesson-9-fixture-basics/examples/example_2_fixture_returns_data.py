"""
Приклад 2: Фікстура може повертати будь-що.

Фікстура — звичайна функція, тож через return вона може віддати
dict, list, число, рядок або екземпляр класу.

Запуск: pytest example_2_fixture_returns_data.py -v
"""

import pytest


@pytest.fixture
def numbers():
    """Повертає список."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def pi():
    """Повертає число."""
    return 3.14159


@pytest.fixture
def greeting():
    """Повертає рядок."""
    return "hello, qa"


@pytest.fixture
def config():
    """Повертає словник конфігурації."""
    return {"timeout": 30, "retries": 3}


class Cart:
    """Простий об'єкт-кошик для демонстрації."""

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total_count(self):
        return len(self.items)


@pytest.fixture
def empty_cart():
    """Повертає екземпляр класу."""
    return Cart()


def test_numbers_sum(numbers):
    """Фікстура повертає list."""
    assert sum(numbers) == 15


def test_pi_value(pi):
    """Фікстура повертає float."""
    assert pi == pytest.approx(3.14, abs=0.01)


def test_greeting_text(greeting):
    """Фікстура повертає str."""
    assert "qa" in greeting


def test_config_timeout(config):
    """Фікстура повертає dict."""
    assert config["timeout"] == 30


def test_cart_object(empty_cart):
    """Фікстура повертає екземпляр класу."""
    empty_cart.add("book")
    empty_cart.add("pen")
    assert empty_cart.total_count() == 2
