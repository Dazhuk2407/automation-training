"""
Вправа 1: Напишіть базову yield-фікстуру.

Мета: код до yield — setup, код після yield — teardown.
Замініть pass / TODO на правильний код.

Запуск: pytest exercise_1_yield.py -v
"""

import pytest


@pytest.fixture
def temp_data():
    """
    Фікстура має:
      1. створити dict {"opened": True}  (setup)
      2. віддати його через yield
      3. після тесту поставити data["opened"] = False  (teardown)
    """
    # TODO: setup — створіть: data = {"opened": True}
    # TODO: віддайте значення: yield data
    # TODO: teardown — після yield: data["opened"] = False
    pass


def test_data_is_dict(temp_data):
    """temp_data має бути словником."""
    # TODO: замініть pass на: assert isinstance(temp_data, dict)
    pass


def test_opened_is_true(temp_data):
    """Усередині тесту opened == True."""
    # TODO: замініть pass на: assert temp_data["opened"] is True
    pass


def test_can_add_key(temp_data):
    """Можна додати ключ у фікстуру."""
    temp_data["value"] = 10
    # TODO: замініть pass на: assert temp_data["value"] == 10
    pass


def test_fresh_each_time(temp_data):
    """Кожен тест отримує свіжу фікстуру (ключа value ще немає)."""
    # TODO: замініть pass на: assert "value" not in temp_data
    pass
