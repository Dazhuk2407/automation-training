"""
Автоматична перевірка вправ — Lesson 0: Знайомство з Pytest

Цей файл перевіряє що студент правильно написав тести у вправах.
Запуск: pytest test_exercises.py -v
"""

import importlib.util
import ast
import os

import pytest


EXERCISES_DIR = os.path.dirname(__file__)


# --- Helpers ---

def _load_module(filename):
    """Завантажити модуль студента за назвою файлу."""
    filepath = os.path.join(EXERCISES_DIR, filename)
    if not os.path.exists(filepath):
        pytest.skip(f"File {filename} not found")

    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""), filepath
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _get_test_functions(filepath):
    """Отримати список тестових функцій з файлу через AST."""
    with open(filepath, encoding="utf-8") as f:
        tree = ast.parse(f.read())

    return [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    ]


def _function_has_assert(filepath, func_name):
    """Перевірити що функція містить assert (не просто pass)."""
    with open(filepath, encoding="utf-8") as f:
        tree = ast.parse(f.read())

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            for child in ast.walk(node):
                if isinstance(child, ast.Assert):
                    return True
                # pytest.raises теж є валідною перевіркою
                if isinstance(child, ast.With):
                    for item in child.items:
                        if isinstance(item.context_expr, ast.Call):
                            call = item.context_expr
                            if isinstance(call.func, ast.Attribute):
                                if call.func.attr == "raises":
                                    return True
    return False


# ============================================================
# Exercise 1: is_even / is_odd
# ============================================================

class TestExercise1:
    """Перевірка вправи 1: is_even / is_odd."""

    def setup_method(self):
        self.module = _load_module("exercise_1_even_odd.py")

    def test_functions_exist(self):
        """Функції is_even та is_odd існують."""
        assert hasattr(self.module, "is_even")
        assert hasattr(self.module, "is_odd")

    def test_is_even_works(self):
        """is_even повертає правильні результати."""
        assert self.module.is_even(2) is True
        assert self.module.is_even(3) is False
        assert self.module.is_even(0) is True

    def test_is_odd_works(self):
        """is_odd повертає правильні результати."""
        assert self.module.is_odd(7) is True
        assert self.module.is_odd(4) is False

    def test_student_tests_have_asserts(self):
        """Студент написав assert у кожному тесті (не залишив pass)."""
        filepath = os.path.join(EXERCISES_DIR, "exercise_1_even_odd.py")
        test_funcs = _get_test_functions(filepath)
        assert len(test_funcs) >= 5, (
            f"Очікується мінімум 5 тестових функцій, знайдено {len(test_funcs)}"
        )

        for func_name in test_funcs:
            assert _function_has_assert(filepath, func_name), (
                f"Функція {func_name}() не містить assert — допишіть перевірку"
            )

    def test_student_tests_pass(self):
        """Тести студента проходять коректно."""
        exit_code = pytest.main([
            os.path.join(EXERCISES_DIR, "exercise_1_even_odd.py"),
            "-v", "--tb=short", "-q"
        ])
        assert exit_code == 0, "Тести у exercise_1_even_odd.py не проходять"


# ============================================================
# Exercise 2: reverse_string / is_palindrome
# ============================================================

class TestExercise2:
    """Перевірка вправи 2: reverse_string / is_palindrome."""

    def setup_method(self):
        self.module = _load_module("exercise_2_string_utils.py")

    def test_functions_exist(self):
        """Функції reverse_string та is_palindrome існують."""
        assert hasattr(self.module, "reverse_string")
        assert hasattr(self.module, "is_palindrome")

    def test_reverse_string_works(self):
        """reverse_string повертає правильні результати."""
        assert self.module.reverse_string("hello") == "olleh"
        assert self.module.reverse_string("") == ""

    def test_is_palindrome_works(self):
        """is_palindrome повертає правильні результати."""
        assert self.module.is_palindrome("racecar") is True
        assert self.module.is_palindrome("hello") is False
        assert self.module.is_palindrome("Madam") is True

    def test_student_tests_have_asserts(self):
        """Студент написав assert у кожному тесті."""
        filepath = os.path.join(EXERCISES_DIR, "exercise_2_string_utils.py")
        test_funcs = _get_test_functions(filepath)
        assert len(test_funcs) >= 5, (
            f"Очікується мінімум 5 тестових функцій, знайдено {len(test_funcs)}"
        )

        for func_name in test_funcs:
            assert _function_has_assert(filepath, func_name), (
                f"Функція {func_name}() не містить assert — допишіть перевірку"
            )

    def test_student_tests_pass(self):
        """Тести студента проходять коректно."""
        exit_code = pytest.main([
            os.path.join(EXERCISES_DIR, "exercise_2_string_utils.py"),
            "-v", "--tb=short", "-q"
        ])
        assert exit_code == 0, "Тести у exercise_2_string_utils.py не проходять"


# ============================================================
# Exercise 3: calculator with exceptions
# ============================================================

class TestExercise3:
    """Перевірка вправи 3: калькулятор з винятками."""

    def setup_method(self):
        self.module = _load_module("exercise_3_calculator.py")

    def test_functions_exist(self):
        """Функції add, subtract, divide існують."""
        assert hasattr(self.module, "add")
        assert hasattr(self.module, "subtract")
        assert hasattr(self.module, "divide")

    def test_add_works(self):
        """add повертає правильні результати."""
        assert self.module.add(2, 3) == 5
        assert self.module.add(-1, 1) == 0

    def test_subtract_works(self):
        """subtract повертає правильні результати."""
        assert self.module.subtract(10, 3) == 7

    def test_divide_works(self):
        """divide повертає правильні результати."""
        assert self.module.divide(10, 2) == 5.0

    def test_divide_by_zero_raises(self):
        """divide(x, 0) кидає ValueError."""
        with pytest.raises(ValueError):
            self.module.divide(10, 0)

    def test_student_tests_have_asserts(self):
        """Студент написав assert або pytest.raises у кожному тесті."""
        filepath = os.path.join(EXERCISES_DIR, "exercise_3_calculator.py")
        test_funcs = _get_test_functions(filepath)
        assert len(test_funcs) >= 5, (
            f"Очікується мінімум 5 тестових функцій, знайдено {len(test_funcs)}"
        )

        for func_name in test_funcs:
            assert _function_has_assert(filepath, func_name), (
                f"Функція {func_name}() не містить assert або pytest.raises"
            )

    def test_student_tests_pass(self):
        """Тести студента проходять коректно."""
        exit_code = pytest.main([
            os.path.join(EXERCISES_DIR, "exercise_3_calculator.py"),
            "-v", "--tb=short", "-q"
        ])
        assert exit_code == 0, "Тести у exercise_3_calculator.py не проходять"