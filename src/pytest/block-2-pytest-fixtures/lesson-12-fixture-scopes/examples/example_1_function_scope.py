"""
Приклад 1: function scope (default) — нова фікстура для кожного тесту.

Лічильник setup_calls рахує, скільки разів виконався код фікстури.
При function scope він виконується заново перед КОЖНИМ тестом,
тому кожен тест бачить свіжий екземпляр і максимальну ізоляцію.

Запуск: pytest example_1_function_scope.py -v
"""

import pytest


# Лічильник викликів setup — у межах цього файлу (детерміновано).
setup_calls = {"n": 0}


@pytest.fixture  # scope="function" за замовчуванням
def fresh_data():
    """Створюється заново для кожного тесту."""
    setup_calls["n"] += 1
    return {"value": 0, "created_on_call": setup_calls["n"]}


def test_first(fresh_data):
    """Перший тест — setup виконався вперше."""
    assert fresh_data["created_on_call"] == 1
    # Змінюємо дані — це НЕ вплине на інші тести (у кожного свій екземпляр).
    fresh_data["value"] = 100
    assert fresh_data["value"] == 100


def test_second(fresh_data):
    """Другий тест — setup виконався вдруге, дані свіжі."""
    assert fresh_data["created_on_call"] == 2
    # value знову 0 — зміни з test_first сюди не потрапили.
    assert fresh_data["value"] == 0


def test_third(fresh_data):
    """Третій тест — setup виконався втретє."""
    assert fresh_data["created_on_call"] == 3
    assert fresh_data["value"] == 0


def test_setup_ran_three_times():
    """Після 3 тестів код function-фікстури виконався рівно 3 рази."""
    assert setup_calls["n"] == 3
