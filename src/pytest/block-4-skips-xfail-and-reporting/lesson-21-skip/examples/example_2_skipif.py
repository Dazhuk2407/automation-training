"""
Приклад 2: Умовний пропуск через @pytest.mark.skipif.

Умова обчислюється під час збору тестів. True -> пропуск, False -> виконання.
Незалежно від того, пропущено тест чи ні, падінь немає (exit code 0).

Запуск: pytest example_2_skipif.py -v
        pytest example_2_skipif.py -rs
"""

import os
import sys

import pytest


def test_basic_math():
    """Звичайний тест — виконується завжди."""
    assert 10 / 2 == 5


@pytest.mark.skipif(
    sys.version_info < (3, 12),
    reason="потрібен Python 3.12+",
)
def test_new_python_feature():
    """Пропускається на старих версіях Python."""
    assert sys.version_info >= (3, 12)


@pytest.mark.skipif(
    sys.platform == "win32",
    reason="POSIX-шляхи не застосовні на Windows",
)
def test_posix_path():
    """Пропускається на Windows, виконується на Linux/macOS."""
    assert os.sep == "/"


@pytest.mark.skipif(
    os.getenv("DB_URL") is None,
    reason="немає підключення до БД (DB_URL не задано)",
)
def test_db_connection():
    """Пропускається якщо змінна оточення DB_URL відсутня."""
    assert os.getenv("DB_URL")


def test_membership():
    """Звичайний тест — виконується завжди."""
    assert "py" in "pytest"
