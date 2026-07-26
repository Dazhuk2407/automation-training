"""
Приклад 1: Безумовний пропуск через @pytest.mark.skip.

Показує суміш звичайних (passing) тестів і пропущених.
Пропущені тести — НЕ падіння: exit code лишається 0.

Запуск: pytest example_1_mark_skip.py -v
        pytest example_1_mark_skip.py -rs   # показати причини пропусків
"""

import pytest


def test_addition():
    """Звичайний тест — виконується і проходить."""
    assert 2 + 2 == 4


def test_string_upper():
    """Звичайний тест — виконується і проходить."""
    assert "pytest".upper() == "PYTEST"


@pytest.mark.skip(reason="фіча ще не реалізована")
def test_new_feature():
    """Пропущено завжди — тіло не виконається."""
    assert new_feature() == 42  # noqa: F821 — функції ще не існує, і це ок


@pytest.mark.skip(reason="блокує баг #1234, чекаємо фікс")
def test_known_broken():
    """Пропущено завжди — навіть свідомо хибний assert не впаде."""
    assert False  # не виконається — тест пропущено


def test_list_sorting():
    """Ще один звичайний тест — виконується і проходить."""
    assert sorted([3, 1, 2]) == [1, 2, 3]
