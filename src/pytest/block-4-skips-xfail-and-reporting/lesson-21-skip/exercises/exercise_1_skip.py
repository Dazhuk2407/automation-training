"""
Вправа 1: Безумовний пропуск через @pytest.mark.skip.

Для деяких тестів потрібно ДОПИСАТИ assert.
Для деяких — ДОДАТИ декоратор @pytest.mark.skip(reason="...").
Дивіться завдання у EXERCISES.md.

Після виконання: 0 failures (частина тестів буде SKIPPED — це нормально).

Запуск: pytest exercise_1_skip.py -v
"""

import pytest  # noqa: F401 — знадобиться для @pytest.mark.skip


def test_addition():
    """Звичайний тест: 2 + 2 == 4."""
    # TODO: замініть pass на: assert 2 + 2 == 4
    pass


def test_string_length():
    """Звичайний тест: довжина 'pytest' == 6."""
    # TODO: замініть pass на: assert len("pytest") == 6
    pass


def test_not_ready_feature():
    """Фіча ще не готова — цей тест треба ПРОПУСТИТИ.

    TODO: додайте над функцією декоратор:
        @pytest.mark.skip(reason="фіча ще не реалізована")
    Тіло лишіть як є — воно не виконається.
    """
    assert unknown_feature() == 42  # noqa: F821 — функції ще не існує


def test_list_reverse():
    """Звичайний тест: розворот списку."""
    # TODO: замініть pass на: assert list(reversed([1, 2, 3])) == [3, 2, 1]
    pass


def test_blocked_by_bug():
    """Тест заблоковано відомим багом — ПРОПУСТІТЬ його.

    TODO: додайте над функцією декоратор:
        @pytest.mark.skip(reason="блокує баг #4321")
    """
    assert False  # не виконається після додавання skip
