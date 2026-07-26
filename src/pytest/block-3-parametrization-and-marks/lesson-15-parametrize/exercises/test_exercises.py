"""
Автоматична перевірка вправ — Lesson 15: Parametrize

Запуск: pytest test_exercises.py -v
"""

import ast
import os

import pytest


EXERCISES_DIR = os.path.dirname(os.path.abspath(__file__))

EXERCISE_FILES = [
    "exercise_1_parametrize.py",
    "exercise_2_cases.py",
    "exercise_3_fix_params.py",
]

# Рахуємо ФУНКЦІЇ test_, а не розгорнуті параметризовані кейси.
EXPECTED_TEST_COUNTS = {
    "exercise_1_parametrize.py": 5,
    "exercise_2_cases.py": 5,
    "exercise_3_fix_params.py": 3,
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


def _function_has_assert_or_raises(filepath, func_name):
    """Перевірити що функція містить assert або pytest.raises."""
    with open(filepath, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            for child in ast.walk(node):
                if isinstance(child, ast.Assert):
                    return True
                if isinstance(child, ast.With):
                    for item in child.items:
                        if isinstance(item.context_expr, ast.Call):
                            call = item.context_expr
                            if isinstance(call.func, ast.Attribute):
                                if call.func.attr == "raises":
                                    return True
    return False


# ============================================================
# Наявність файлів
# ============================================================

class TestFilesExist:
    """Всі файли вправ існують."""

    @pytest.mark.parametrize("filename", EXERCISE_FILES)
    def test_file_exists(self, filename):
        assert os.path.isfile(_filepath(filename)), (
            f"Створіть файл {filename}"
        )


# ============================================================
# Кількість тестів
# ============================================================

class TestTestCounts:
    """Кожен файл містить достатньо тест-функцій."""

    @pytest.mark.parametrize("filename,expected", EXPECTED_TEST_COUNTS.items())
    def test_enough_tests(self, filename, expected):
        filepath = _filepath(filename)
        if not os.path.isfile(filepath):
            pytest.skip(f"{filename} не знайдено")
        funcs = _get_test_functions(filepath)
        assert len(funcs) >= expected, (
            f"{filename}: потрібно мінімум {expected} тест-функцій, "
            f"знайдено {len(funcs)}"
        )


# ============================================================
# Assert написано (не залишено pass)
# ============================================================

class TestAssertsWritten:
    """Студент замінив pass на assert/pytest.raises."""

    @pytest.mark.parametrize("filename", EXERCISE_FILES)
    def test_all_have_asserts(self, filename):
        filepath = _filepath(filename)
        if not os.path.isfile(filepath):
            pytest.skip(f"{filename} не знайдено")
        funcs = _get_test_functions(filepath)
        missing = [
            f for f in funcs
            if not _function_has_assert_or_raises(filepath, f)
        ]
        assert not missing, (
            f"{filename}: функції без assert: "
            + ", ".join(f"{f}()" for f in missing)
            + " — замініть pass"
        )


# ============================================================
# Тести проходять
# ============================================================

class TestStudentTestsPass:
    """Тести студента проходять."""

    @pytest.mark.parametrize("filename", EXERCISE_FILES)
    def test_exercises_pass(self, filename):
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
