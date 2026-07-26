"""
Вправа 2: module scope і спільний мутабельний стан.

Фікстура bucket має scope="module" — це ОДИН список на весь файл.
Тести виконуються по порядку і додають елементи в той самий список.
Замініть pass на assert, які відображають, що стан НАКОПИЧУЄТЬСЯ між тестами.

Підказка: це наочно показує небезпеку широкого scope з мутабельними даними.

Запуск: pytest exercise_2_shared_state.py -v
"""

import pytest


@pytest.fixture(scope="module")
def bucket():
    """Один список на весь модуль — спільний для всіх тестів."""
    return []


def test_starts_empty(bucket):
    """Перший тест бачить порожній список."""
    # TODO: замініть pass на: assert bucket == []
    pass


def test_add_one(bucket):
    """Додаємо елемент — довжина стає 1."""
    bucket.append("a")
    # TODO: замініть pass на: assert len(bucket) == 1
    pass


def test_state_persists(bucket):
    """Стан ЗБЕРІГСЯ з попереднього тесту — "a" усе ще тут."""
    # TODO: замініть pass на: assert bucket == ["a"]
    pass


def test_add_second(bucket):
    """Додаємо ще один — тепер елементів 2 (стан накопичився)."""
    bucket.append("b")
    # TODO: замініть pass на: assert bucket == ["a", "b"]
    pass


def test_not_reset(bucket):
    """module-фікстура НЕ скидається між тестами — довжина досі 2."""
    # TODO: замініть pass на: assert len(bucket) == 2
    pass
