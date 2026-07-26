"""
Вправа 2: Використайте готові фікстури.

Фікстури вже написані за вас — НЕ змінюйте їх. Ваше завдання:
1. Додати ім'я потрібної фікстури у параметри тесту.
2. Замінити pass на assert, який використовує значення фікстури.

Нагадування: фікстуру НЕ викликають дужками. Параметр уже містить
повернуте значення (наприклад, config — це вже dict).

Запуск: pytest exercise_2_use_fixture.py -v
"""

import pytest


@pytest.fixture
def config():
    """Готовий конфіг (не змінюйте)."""
    return {"base_url": "https://api.example.com", "timeout": 30, "retries": 3}


@pytest.fixture
def order():
    """Готове замовлення (не змінюйте)."""
    return {"id": 1001, "items": ["book", "pen", "cup"], "total": 25.50}


# Підказка: додайте фікстуру у параметри — def test_...(config):

def test_base_url(config):
    """base_url має починатися з 'https://'."""
    # TODO: замініть pass на: assert config["base_url"].startswith("https://")
    pass


def test_timeout():
    """timeout має дорівнювати 30.

    Підказка: цей тест ще НЕ приймає фікстуру.
    """
    # TODO: 1) додайте параметр config у сигнатуру тесту вище
    #       2) замініть pass на: assert config["timeout"] == 30
    pass


def test_retries():
    """retries має дорівнювати 3.

    Підказка: цей тест ще НЕ приймає фікстуру.
    """
    # TODO: 1) додайте параметр config у сигнатуру тесту вище
    #       2) замініть pass на: assert config["retries"] == 3
    pass


def test_order_item_count(order):
    """У замовленні має бути 3 позиції."""
    # TODO: замініть pass на: assert len(order["items"]) == 3
    pass


def test_order_total(order):
    """Сума замовлення має дорівнювати 25.50."""
    # TODO: замініть pass на: assert order["total"] == 25.50
    pass
