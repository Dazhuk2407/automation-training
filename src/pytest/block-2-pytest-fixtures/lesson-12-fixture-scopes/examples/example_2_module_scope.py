"""
Приклад 2: module scope — одна фікстура на весь файл.

Лічильник setup_calls показує, що код module-фікстури виконується
РІВНО ОДИН РАЗ на весь файл. Усі тести отримують той самий екземпляр,
тому setup не викликається знову між тестами.

Запуск: pytest example_2_module_scope.py -v
"""

import pytest


setup_calls = {"n": 0}


@pytest.fixture(scope="module")
def shared():
    """Створюється один раз на весь модуль."""
    setup_calls["n"] += 1
    return setup_calls["n"]


def test_a(shared):
    """Перший тест ініціює setup — shared == 1."""
    assert shared == 1


def test_b(shared):
    """Той самий екземпляр — setup НЕ викликався знову."""
    assert shared == 1


def test_c(shared):
    """Знову той самий екземпляр на весь файл."""
    assert shared == 1


def test_setup_ran_once():
    """Код module-фікстури виконався рівно 1 раз на весь файл."""
    assert setup_calls["n"] == 1
