"""
Автоматична перевірка вправ — Lesson 10: Tuples
Запуск: pytest test_exercises.py -v
"""

import ast
import os

import pytest


EXERCISES_DIR = os.path.dirname(os.path.abspath(__file__))

EXERCISE_FILES = [
    "exercise_1_basics.py",
    "exercise_2_unpacking.py",
    "exercise_3_functions.py",
    "exercise_4_test_data.py",
]

EXPECTED_TEST_COUNTS = {
    "exercise_1_basics.py": 6,
    "exercise_2_unpacking.py": 5,
    "exercise_3_functions.py": 4,
    "exercise_4_test_data.py": 4,
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


class TestFilesExist:
    @pytest.mark.parametrize("filename", EXERCISE_FILES)
    def test_file_exists(self, filename):
        assert os.path.isfile(_filepath(filename)), f"Створіть {filename}"


class TestTestCounts:
    @pytest.mark.parametrize("filename,expected", EXPECTED_TEST_COUNTS.items())
    def test_enough_tests(self, filename, expected):
        filepath = _filepath(filename)
        if not os.path.isfile(filepath):
            pytest.skip(f"{filename} не знайдено")
        funcs = _get_test_functions(filepath)
        assert len(funcs) >= expected, (
            f"{filename}: потрібно {expected} тестів, знайдено {len(funcs)}"
        )


class TestAssertsWritten:
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
            f"{filename}: без assert: " + ", ".join(f"{f}()" for f in missing)
        )


class TestStudentTestsPass:
    @pytest.mark.parametrize("filename", EXERCISE_FILES)
    def test_exercises_pass(self, filename):
        filepath = _filepath(filename)
        if not os.path.isfile(filepath):
            pytest.skip(f"{filename} не знайдено")
        exit_code = pytest.main([filepath, "-v", "--tb=short", "-q", "--no-header"])
        assert exit_code == 0, f"Тести у {filename} не проходять"