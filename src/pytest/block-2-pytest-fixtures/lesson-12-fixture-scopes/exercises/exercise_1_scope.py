"""
Вправа 1: function scope (default).

Фікстура вже написана. Замініть pass на правильний assert, спираючись на те,
що function-фікстура створюється ЗАНОВО для кожного тесту.

Підказка: лічильник counter["n"] збільшується щоразу, коли виконується setup.

Запуск: pytest exercise_1_scope.py -v
"""

import pytest


counter = {"n": 0}


@pytest.fixture  # function scope за замовчуванням
def number():
    """Створюється заново перед кожним тестом."""
    counter["n"] += 1
    return counter["n"]


def test_first(number):
    """Перший тест: setup виконався вперше — number має дорівнювати 1."""
    # TODO: замініть pass на: assert number == 1
    pass


def test_second(number):
    """Другий тест: function-фікстура створена заново — number == 2."""
    # TODO: замініть pass на: assert number == 2
    pass


def test_third(number):
    """Третій тест: знову нова фікстура — number == 3."""
    # TODO: замініть pass на: assert number == 3
    pass


def test_isolation(number):
    """Кожен тест отримує СВІЙ екземпляр — number int і більший за 0."""
    # TODO: замініть pass на: assert isinstance(number, int) and number > 0
    pass


def test_setup_count():
    """Після 4 тестів код function-фікстури виконався 4 рази."""
    # TODO: замініть pass на: assert counter["n"] == 4
    pass
