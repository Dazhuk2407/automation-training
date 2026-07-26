"""
Вправа 2: Умовний пропуск через @pytest.mark.skipif.

Для деяких тестів потрібно ДОПИСАТИ assert.
Для деяких — ДОДАТИ декоратор @pytest.mark.skipif(condition, reason="...").
Дивіться завдання у EXERCISES.md.

Після виконання: 0 failures (частина тестів може бути SKIPPED — це нормально).

Запуск: pytest exercise_2_skipif.py -v
"""

import os  # noqa: F401 — знадобиться для умови skipif
import sys  # noqa: F401 — знадобиться для умови skipif

import pytest  # noqa: F401 — знадобиться для @pytest.mark.skipif


def test_multiplication():
    """Звичайний тест: 3 * 4 == 12."""
    # TODO: замініть pass на: assert 3 * 4 == 12
    pass


def test_python_version_check():
    """Тест для нової версії Python — ПРОПУСТИ якщо версія < 3.12.

    TODO: додайте над функцією декоратор:
        @pytest.mark.skipif(sys.version_info < (3, 12), reason="потрібен Python 3.12+")
    І замініть pass на: assert sys.version_info >= (3, 12)
    """
    pass


def test_windows_only():
    """Тест лише для Windows — ПРОПУСТИ на не-Windows платформах.

    TODO: додайте над функцією декоратор:
        @pytest.mark.skipif(sys.platform != "win32", reason="тест лише для Windows")
    І замініть pass на: assert sys.platform == "win32"
    """
    pass


def test_string_join():
    """Звичайний тест: об'єднання рядків."""
    # TODO: замініть pass на: assert "-".join(["a", "b", "c"]) == "a-b-c"
    pass


def test_env_variable():
    """Тест потребує змінну оточення CI — ПРОПУСТИ якщо її немає.

    TODO: додайте над функцією декоратор:
        @pytest.mark.skipif(os.getenv("CI") is None, reason="змінна CI не задана")
    І замініть pass на: assert os.getenv("CI")
    """
    pass
