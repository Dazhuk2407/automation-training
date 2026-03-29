"""
Автоматична перевірка вправ — Lesson 2: Структура pytest проєкту

Перевіряє що студент створив правильну структуру проєкту.
Запуск: pytest test_exercises.py -v
"""

import os
import configparser

import pytest


EXERCISES_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(EXERCISES_DIR, "my_project")


def _project_path(*parts):
    """Побудувати шлях відносно my_project/."""
    return os.path.join(PROJECT_DIR, *parts)


# ============================================================
# Exercise 1: Структура папок
# ============================================================

class TestExercise1:
    """Перевірка вправи 1: базова структура проєкту."""

    def test_project_dir_exists(self):
        """Папка my_project/ існує."""
        assert os.path.isdir(PROJECT_DIR), (
            "Створіть папку my_project/ в директорії exercises/"
        )

    def test_src_dir_exists(self):
        """Папка my_project/src/ існує."""
        assert os.path.isdir(_project_path("src")), (
            "Створіть папку src/ в my_project/"
        )

    def test_tests_dir_exists(self):
        """Папка my_project/tests/ існує."""
        assert os.path.isdir(_project_path("tests")), (
            "Створіть папку tests/ в my_project/"
        )

    def test_src_init_exists(self):
        """Файл my_project/src/__init__.py існує."""
        assert os.path.isfile(_project_path("src", "__init__.py")), (
            "Створіть __init__.py в src/"
        )

    def test_tests_init_exists(self):
        """Файл my_project/tests/__init__.py існує."""
        assert os.path.isfile(_project_path("tests", "__init__.py")), (
            "Створіть __init__.py в tests/"
        )

    def test_requirements_exists(self):
        """Файл my_project/requirements.txt існує."""
        assert os.path.isfile(_project_path("requirements.txt")), (
            "Створіть requirements.txt в my_project/"
        )


# ============================================================
# Exercise 2: pytest.ini
# ============================================================

class TestExercise2:
    """Перевірка вправи 2: конфігурація pytest."""

    def test_pytest_ini_exists(self):
        """Файл my_project/pytest.ini існує."""
        assert os.path.isfile(_project_path("pytest.ini")), (
            "Створіть pytest.ini в my_project/"
        )

    def test_pytest_ini_has_section(self):
        """pytest.ini містить секцію [pytest]."""
        ini_path = _project_path("pytest.ini")
        if not os.path.isfile(ini_path):
            pytest.skip("pytest.ini не знайдено")

        config = configparser.ConfigParser()
        config.read(ini_path, encoding="utf-8")
        assert "pytest" in config.sections(), (
            "pytest.ini повинен містити секцію [pytest]"
        )

    def test_pytest_ini_has_testpaths(self):
        """pytest.ini містить testpaths = tests."""
        ini_path = _project_path("pytest.ini")
        if not os.path.isfile(ini_path):
            pytest.skip("pytest.ini не знайдено")

        config = configparser.ConfigParser()
        config.read(ini_path, encoding="utf-8")
        assert config.get("pytest", "testpaths", fallback=None) == "tests", (
            "Додайте testpaths = tests у секцію [pytest]"
        )


# ============================================================
# Exercise 3: conftest.py
# ============================================================

class TestExercise3:
    """Перевірка вправи 3: conftest.py."""

    def test_conftest_exists(self):
        """Файл my_project/tests/conftest.py існує."""
        assert os.path.isfile(_project_path("tests", "conftest.py")), (
            "Створіть conftest.py в tests/"
        )

    def test_conftest_is_not_empty(self):
        """conftest.py не порожній (містить docstring)."""
        conftest_path = _project_path("tests", "conftest.py")
        if not os.path.isfile(conftest_path):
            pytest.skip("conftest.py не знайдено")

        with open(conftest_path, encoding="utf-8") as f:
            content = f.read().strip()

        assert len(content) > 0, (
            "conftest.py порожній — додайте docstring з описом"
        )