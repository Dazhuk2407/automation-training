"""
Автоматична перевірка вправ — Lesson 3: Перший тест у проєкті

Перевіряє що студент створив правильну структуру,
написав код та тести, і все працює.

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
    """Побудувати шлях відносно my_project/."""
    return os.path.join(PROJECT_DIR, *parts)


def _load_module(module_name, filepath):
    """Завантажити Python модуль з файлу."""
    if not os.path.isfile(filepath):
        pytest.skip(f"Файл {filepath} не знайдено")

    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _get_test_functions(filepath):
    """Отримати список test_ функцій з файлу через AST."""
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
    return False


# ============================================================
# Структура проєкту
# ============================================================

class TestStructure:
    """Перевірка структури проєкту."""

    def test_project_dir_exists(self):
        """Папка my_project/ існує."""
        assert os.path.isdir(PROJECT_DIR), (
            "Створіть папку my_project/ в директорії exercises/"
        )

    def test_src_calculator_exists(self):
        """Файл my_project/src/calculator.py існує."""
        assert os.path.isfile(_project_path("src", "calculator.py")), (
            "Створіть src/calculator.py в my_project/"
        )

    def test_tests_test_calculator_exists(self):
        """Файл my_project/tests/test_calculator.py існує."""
        assert os.path.isfile(_project_path("tests", "test_calculator.py")), (
            "Створіть tests/test_calculator.py в my_project/"
        )

    def test_src_init_exists(self):
        """Файл my_project/src/__init__.py існує."""
        assert os.path.isfile(_project_path("src", "__init__.py")), (
            "Створіть src/__init__.py (порожній файл)"
        )

    def test_tests_init_exists(self):
        """Файл my_project/tests/__init__.py існує."""
        assert os.path.isfile(_project_path("tests", "__init__.py")), (
            "Створіть tests/__init__.py (порожній файл)"
        )


# ============================================================
# Код у src/calculator.py
# ============================================================

class TestCalculatorModule:
    """Перевірка що функції в calculator.py працюють правильно."""

    def setup_method(self):
        calc_path = _project_path("src", "calculator.py")
        self.module = _load_module("calculator", calc_path)

    def test_add_exists(self):
        """Функція add існує."""
        assert hasattr(self.module, "add"), (
            "Додайте функцію add(a, b) в src/calculator.py"
        )

    def test_subtract_exists(self):
        """Функція subtract існує."""
        assert hasattr(self.module, "subtract"), (
            "Додайте функцію subtract(a, b) в src/calculator.py"
        )

    def test_multiply_exists(self):
        """Функція multiply існує (Вправа 3)."""
        assert hasattr(self.module, "multiply"), (
            "Додайте функцію multiply(a, b) в src/calculator.py (Вправа 3)"
        )

    def test_add_works(self):
        """add(2, 3) повертає 5."""
        assert self.module.add(2, 3) == 5

    def test_add_zeros(self):
        """add(0, 0) повертає 0."""
        assert self.module.add(0, 0) == 0

    def test_add_negative(self):
        """add(-1, -1) повертає -2."""
        assert self.module.add(-1, -1) == -2

    def test_subtract_works(self):
        """subtract(10, 4) повертає 6."""
        assert self.module.subtract(10, 4) == 6

    def test_subtract_from_zero(self):
        """subtract(0, 5) повертає -5."""
        assert self.module.subtract(0, 5) == -5

    def test_multiply_works(self):
        """multiply(3, 4) повертає 12."""
        assert self.module.multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        """multiply(100, 0) повертає 0."""
        assert self.module.multiply(100, 0) == 0


# ============================================================
# Тести студента
# ============================================================

class TestStudentTests:
    """Перевірка що студент написав тести правильно."""

    def setup_method(self):
        self.test_path = _project_path("tests", "test_calculator.py")
        if not os.path.isfile(self.test_path):
            pytest.skip("tests/test_calculator.py не знайдено")

    def test_has_enough_tests(self):
        """Студент написав мінімум 7 тестових функцій."""
        funcs = _get_test_functions(self.test_path)
        assert len(funcs) >= 7, (
            f"Очікується мінімум 7 test_ функцій, знайдено {len(funcs)}. "
            "Виконайте вправи 1-3."
        )

    def test_all_tests_have_asserts(self):
        """Кожен тест містить assert (не залишено pass)."""
        funcs = _get_test_functions(self.test_path)
        for func_name in funcs:
            assert _function_has_assert(self.test_path, func_name), (
                f"Функція {func_name}() не містить assert — "
                "замініть pass на assert"
            )

    def test_student_tests_pass(self):
        """Тести студента проходять коректно."""
        # Додаємо my_project у sys.path щоб імпорти працювали
        original_path = sys.path.copy()
        sys.path.insert(0, PROJECT_DIR)
        try:
            exit_code = pytest.main([
                self.test_path,
                "-v", "--tb=short", "-q", "--no-header"
            ])
            assert exit_code == 0, (
                "Тести у tests/test_calculator.py не проходять. "
                "Запустіть pytest -v з папки my_project/ щоб побачити помилки."
            )
        finally:
            sys.path = original_path