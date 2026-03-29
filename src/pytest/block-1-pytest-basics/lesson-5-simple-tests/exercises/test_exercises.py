"""
Автоматична перевірка вправ — Lesson 5: Прості тести для базових типів

Запуск: pytest test_exercises.py -v
"""

import ast
import os

import pytest


EXERCISES_DIR = os.path.dirname(os.path.abspath(__file__))

EXERCISE_FILES = [
    "exercise_1_numbers.py",
    "exercise_2_strings.py",
    "exercise_3_collections.py",
    "exercise_4_float.py",
    "exercise_5_edge_cases.py",
]

EXPECTED_TEST_COUNTS = {
    "exercise_1_numbers.py": 6,
    "exercise_2_strings.py": 6,
    "exercise_3_collections.py": 8,
    "exercise_4_float.py": 3,
    "exercise_5_edge_cases.py": 6,
}


def _filepath(filename):
    return os.path.join(EXERCISES_DIR, filename)


def _get_test_functions(filepath):
    with open(filepath, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    return [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    ]


def _function_has_assert(filepath, func_name):
    with open(filepath, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            for child in ast.walk(node):
                if isinstance(child, ast.Assert):
                    return True
    return False


# ============================================================
# Перевірка наявності файлів
# ============================================================

class TestFilesExist:
    """Перевірка що всі файли вправ існують."""

    @pytest.mark.parametrize("filename", EXERCISE_FILES)
    def test_file_exists(self, filename):
        """Файл вправи існує."""
        assert os.path.isfile(_filepath(filename)), (
            f"Створіть файл {filename}"
        )


# ============================================================
# Перевірка кількості тестів
# ============================================================

class TestTestCounts:
    """Перевірка що в кожному файлі достатньо тестів."""

    @pytest.mark.parametrize("filename,expected", EXPECTED_TEST_COUNTS.items())
    def test_enough_tests(self, filename, expected):
        """Файл містить достатньо test_ функцій."""
        filepath = _filepath(filename)
        if not os.path.isfile(filepath):
            pytest.skip(f"{filename} не знайдено")

        funcs = _get_test_functions(filepath)
        assert len(funcs) >= expected, (
            f"{filename}: потрібно мінімум {expected} тестів, "
            f"знайдено {len(funcs)}"
        )


# ============================================================
# Перевірка що assert написано (не залишено pass)
# ============================================================

class TestAssertsWritten:
    """Перевірка що студент замінив pass на assert."""

    @pytest.mark.parametrize("filename", EXERCISE_FILES)
    def test_all_have_asserts(self, filename):
        """Кожна test_ функція містить assert."""
        filepath = _filepath(filename)
        if not os.path.isfile(filepath):
            pytest.skip(f"{filename} не знайдено")

        funcs = _get_test_functions(filepath)
        missing = [
            f for f in funcs
            if not _function_has_assert(filepath, f)
        ]
        assert not missing, (
            f"{filename}: функції без assert: "
            + ", ".join(f"{f}()" for f in missing)
            + " — замініть pass на assert"
        )


# ============================================================
# Запуск тестів студента
# ============================================================

class TestStudentTestsPass:
    """Перевірка що тести студента проходять."""

    @pytest.mark.parametrize("filename", EXERCISE_FILES)
    def test_exercises_pass(self, filename):
        """Тести у файлі проходять коректно."""
        filepath = _filepath(filename)
        if not os.path.isfile(filepath):
            pytest.skip(f"{filename} не знайдено")

        exit_code = pytest.main([
            filepath, "-v", "--tb=short", "-q", "--no-header"
        ])
        assert exit_code == 0, (
            f"Тести у {filename} не проходять. "
            f"Запустіть: pytest {filename} -v"
        )