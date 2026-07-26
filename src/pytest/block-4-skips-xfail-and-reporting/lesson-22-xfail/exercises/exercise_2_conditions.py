"""
Вправа 2: Умовний xfail.

У кожному тесті assert вже написаний і ПРОХОДИТЬ. Ваше завдання —
ДОПИСАТИ декоратор умовного xfail над функцією за підказкою в TODO.

Синтаксис умовного xfail:
    @pytest.mark.xfail(condition, reason="...")
- Якщо condition == True  → маркер активний (очікуємо падіння).
- Якщо condition == False → маркер ігнорується, тест звичайний.

Оскільки asserts тут проходять, підсумок буде 0 failed у будь-якому разі
(passed або xpassed залежно від умови вашої платформи).

Запуск: pytest exercise_2_conditions.py -rxX -v
Очікуваний підсумок: 0 failed.
"""

import sys

import pytest


# TODO: додайте @pytest.mark.xfail(sys.platform == "win32", reason="не працює на Windows")
def test_windows_only_bug():
    """Умовний xfail за платформою."""
    assert sys.platform is not None


# TODO: додайте @pytest.mark.xfail(sys.version_info < (3, 8), reason="потрібен Python 3.8+")
def test_python_version_bug():
    """Умовний xfail за версією Python."""
    assert isinstance("py", str)


# TODO: додайте @pytest.mark.xfail(sys.platform == "darwin", reason="bug #5 на macOS")
def test_macos_bug():
    """Умовний xfail для macOS."""
    assert 1 + 1 == 2


# TODO: додайте @pytest.mark.xfail(False, reason="умова ще не настала")
def test_disabled_condition():
    """Умова False → маркер ігнорується, звичайний passing-тест."""
    assert len([1, 2, 3]) == 3


# TODO: додайте @pytest.mark.xfail(sys.maxsize > 2**32, reason="лише на 64-біт")
def test_arch_bug():
    """Умовний xfail за архітектурою."""
    assert isinstance(sys.maxsize, int)
