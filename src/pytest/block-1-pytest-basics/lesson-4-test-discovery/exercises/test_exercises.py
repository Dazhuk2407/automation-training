"""
Автоматична перевірка вправ — Lesson 4: Test Discovery

Перевіряє що студент створив структуру, написав тести
та виправив naming.

Запуск: pytest test_exercises.py -v
"""

import importlib.util
import ast
import os
import sys

import pytest


EXERCISES_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(EXERCISES_DIR, "my_project")


def _project_path(*parts):
    return os.path.join(PROJECT_DIR, *parts)


def _load_module(module_name, filepath):
    if not os.path.isfile(filepath):
        pytest.skip(f"Файл {filepath} не знайдено")
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _get_test_functions(filepath):
    with open(filepath, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    return [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    ]


def _get_test_classes(filepath):
    with open(filepath, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    return [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef) and node.name.startswith("Test")
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
# Структура проєкту (Вправа 2)
# ============================================================

class TestStructure:
    """Перевірка структури проєкту."""

    def test_project_exists(self):
        """Папка my_project/ існує."""
        assert os.path.isdir(PROJECT_DIR), (
            "Створіть папку my_project/ в директорії exercises/"
        )

    def test_src_math_utils_exists(self):
        """Файл src/math_utils.py існує."""
        assert os.path.isfile(_project_path("src", "math_utils.py")), (
            "Створіть src/math_utils.py в my_project/"
        )

    def test_tests_file_exists(self):
        """Файл tests/test_math_utils.py існує."""
        assert os.path.isfile(_project_path("tests", "test_math_utils.py")), (
            "Створіть tests/test_math_utils.py в my_project/"
        )


# ============================================================
# Код у src/math_utils.py (Вправа 2)
# ============================================================

class TestMathUtilsModule:
    """Перевірка функцій у math_utils.py."""

    def setup_method(self):
        self.module = _load_module(
            "math_utils", _project_path("src", "math_utils.py")
        )

    def test_square_exists(self):
        """Функція square існує."""
        assert hasattr(self.module, "square")

    def test_is_positive_exists(self):
        """Функція is_positive існує."""
        assert hasattr(self.module, "is_positive")

    def test_absolute_exists(self):
        """Функція absolute існує."""
        assert hasattr(self.module, "absolute")

    def test_square_works(self):
        """square(3) повертає 9."""
        assert self.module.square(3) == 9

    def test_square_zero(self):
        """square(0) повертає 0."""
        assert self.module.square(0) == 0

    def test_square_negative(self):
        """square(-4) повертає 16."""
        assert self.module.square(-4) == 16

    def test_is_positive_works(self):
        """is_positive(5) повертає True."""
        assert self.module.is_positive(5) is True

    def test_is_positive_negative(self):
        """is_positive(-3) повертає False."""
        assert self.module.is_positive(-3) is False

    def test_absolute_works(self):
        """absolute(-7) повертає 7."""
        assert self.module.absolute(-7) == 7


# ============================================================
# Тести студента (Вправи 2-3)
# ============================================================

class TestStudentTests:
    """Перевірка якості тестів студента."""

    def setup_method(self):
        self.test_path = _project_path("tests", "test_math_utils.py")
        if not os.path.isfile(self.test_path):
            pytest.skip("tests/test_math_utils.py не знайдено")

    def test_has_test_functions(self):
        """Є мінімум 3 тестові функції."""
        funcs = _get_test_functions(self.test_path)
        assert len(funcs) >= 3, (
            f"Потрібно мінімум 3 test_ функції, знайдено {len(funcs)}"
        )

    def test_has_test_class(self):
        """Є клас TestSquare (Вправа 3)."""
        classes = _get_test_classes(self.test_path)
        assert "TestSquare" in classes, (
            "Додайте клас TestSquare з тестами (Вправа 3)"
        )

    def test_class_has_methods(self):
        """TestSquare має мінімум 3 test_ методи."""
        with open(self.test_path, encoding="utf-8") as f:
            tree = ast.parse(f.read())

        methods = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == "TestSquare":
                for item in node.body:
                    if (isinstance(item, ast.FunctionDef)
                            and item.name.startswith("test_")):
                        methods.append(item.name)

        assert len(methods) >= 3, (
            f"TestSquare потребує мінімум 3 test_ методи, знайдено {len(methods)}"
        )

    def test_all_have_asserts(self):
        """Всі тести містять assert."""
        funcs = _get_test_functions(self.test_path)
        for func_name in funcs:
            assert _function_has_assert(self.test_path, func_name), (
                f"{func_name}() не містить assert — замініть pass"
            )

    def test_student_tests_pass(self):
        """Тести студента проходять."""
        original_path = sys.path.copy()
        sys.path.insert(0, PROJECT_DIR)
        try:
            exit_code = pytest.main([
                self.test_path, "-v", "--tb=short", "-q", "--no-header"
            ])
            assert exit_code == 0, (
                "Тести у test_math_utils.py не проходять"
            )
        finally:
            sys.path = original_path


# ============================================================
# Вправа 6: Виправлена назва файлу
# ============================================================

class TestFixedNaming:
    """Перевірка вправи 6: виправлена назва файлу."""

    def test_fixed_file_exists(self):
        """Файл test_math_checks.py існує (виправлена назва)."""
        assert os.path.isfile(
            _project_path("tests", "test_math_checks.py")
        ), (
            "Перейменуйте math_checks.py → test_math_checks.py (Вправа 6)"
        )

    def test_fixed_file_has_tests(self):
        """test_math_checks.py містить test_ функції."""
        filepath = _project_path("tests", "test_math_checks.py")
        if not os.path.isfile(filepath):
            pytest.skip("test_math_checks.py не знайдено")

        funcs = _get_test_functions(filepath)
        assert len(funcs) >= 1, (
            "test_math_checks.py має містити хоча б одну test_ функцію"
        )