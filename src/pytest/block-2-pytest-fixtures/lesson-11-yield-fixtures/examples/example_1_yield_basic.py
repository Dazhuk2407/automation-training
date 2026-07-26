"""
Приклад 1: Базова yield-фікстура — setup → yield → teardown.

Код до yield — це setup (підготовка).
Код після yield — це teardown (прибирання), виконується ПІСЛЯ тесту.

Запуск: pytest example_1_yield_basic.py -v
"""

import pytest


# Спільний журнал подій — щоб побачити ЩО і КОЛИ виконалось.
events = []


@pytest.fixture
def temp_data():
    """yield-фікстура: віддає dict, після тесту закриває його."""
    data = {"opened": True}       # setup
    events.append("setup")
    yield data                     # тест працює тут
    data["opened"] = False         # teardown
    events.append("teardown")


def test_uses_resource(temp_data):
    """Тест отримує значення з фікстури через yield."""
    assert temp_data == {"opened": True}
    assert temp_data["opened"] is True


def test_can_modify_data(temp_data):
    """Кожен тест отримує свіжу фікстуру."""
    temp_data["value"] = 42
    assert temp_data["value"] == 42
    assert temp_data["opened"] is True


def test_teardown_ran_after_previous_tests():
    """
    Перевіряємо факт teardown: попередні тести використали фікстуру,
    тому setup і teardown вже мали виконатись (тести йдуть по порядку).
    """
    assert "setup" in events
    assert "teardown" in events
    # setup завжди передує своєму teardown
    assert events.index("setup") < events.index("teardown")
