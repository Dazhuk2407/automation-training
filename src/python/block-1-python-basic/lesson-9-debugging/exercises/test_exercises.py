"""
Pytest тести для перевірки вправ Lesson 9
Запустіть: pytest test_exercises.py -v
"""

import importlib.util
import pytest
from pathlib import Path

EXERCISES_DIR = Path(__file__).parent


def _import_exercise(module_name):
    """Імпортувати модуль вправи. Повертає модуль або None якщо файлу немає."""
    file_path = EXERCISES_DIR / f"{module_name}.py"
    if not file_path.exists():
        return None
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestExercise1PrintDebug:
    """Тести для завдання 1 - print debugging"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_1_print_debug.py").exists(), \
            "exercise_1_print_debug.py не знайдено"

    def test_perimeter_calculation(self):
        """Периметр має розраховуватись правильно"""
        mod = _import_exercise("exercise_1_print_debug")
        if mod is None:
            pytest.skip("Файл ще не створено")

        result = mod.calculate_rectangle_perimeter(10, 5)
        assert result == 30, f"Очікувалось 30, отримано {result}"

    def test_area_calculation(self):
        """Площа має розраховуватись правильно"""
        mod = _import_exercise("exercise_1_print_debug")
        if mod is None:
            pytest.skip("Файл ще не створено")

        result = mod.calculate_rectangle_area(10, 5)
        assert result == 50, f"Очікувалось 50, отримано {result}"


class TestExercise2Breakpoints:
    """Тести для завдання 2 - breakpoints"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_2_breakpoints.py").exists(), \
            "exercise_2_breakpoints.py не знайдено"


class TestExercise3FixTypeError:
    """Тести для завдання 3 - type error"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_3_fix_type_error.py").exists(), \
            "exercise_3_fix_type_error.py не знайдено"

    def test_handles_string_prices(self):
        """Функція має обробляти ціни як strings"""
        mod = _import_exercise("exercise_3_fix_type_error")
        if mod is None:
            pytest.skip("Файл ще не створено")

        items = [
            {'name': 'A', 'price': 100},
            {'name': 'B', 'price': '50'},
            {'name': 'C', 'price': 80}
        ]
        result = mod.calculate_total(items)
        assert result == 230, f"Очікувалось 230, отримано {result}"


class TestExercise4DebugConditions:
    """Тести для завдання 4 - умови"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_4_debug_conditions.py").exists(), \
            "exercise_4_debug_conditions.py не знайдено"

    def test_age_65_is_senior(self):
        """Вік 65 має бути Senior"""
        mod = _import_exercise("exercise_4_debug_conditions")
        if mod is None:
            pytest.skip("Файл ще не створено")

        result = mod.categorize_age(65)
        assert result == "Senior", f"Вік 65 має бути Senior, отримано {result}"

    def test_age_64_is_adult(self):
        """Вік 64 має бути Adult"""
        mod = _import_exercise("exercise_4_debug_conditions")
        if mod is None:
            pytest.skip("Файл ще не створено")

        result = mod.categorize_age(64)
        assert result == "Adult", f"Вік 64 має бути Adult, отримано {result}"


class TestExercise5ComplexDebug:
    """Тести для завдання 5 - складна функція"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_5_complex_debug.py").exists(), \
            "exercise_5_complex_debug.py не знайдено"

    def test_handles_missing_grade(self):
        """Функція має обробляти відсутність оцінки (default=0)"""
        mod = _import_exercise("exercise_5_complex_debug")
        if mod is None:
            pytest.skip("Файл ще не створено")

        students = [
            {'name': 'Alice', 'grade': 85},
            {'name': 'Bob'},
        ]
        result = mod.process_student_grades(students)
        assert result['total_students'] == 2
        assert 'Bob' in result['failing']

    def test_grade_60_is_passing(self):
        """Оцінка 60 має бути passing"""
        mod = _import_exercise("exercise_5_complex_debug")
        if mod is None:
            pytest.skip("Файл ще не створено")

        students = [{'name': 'Bob', 'grade': 60}]
        result = mod.process_student_grades(students)
        assert 'Bob' in result['passing'], "Оцінка 60 має бути passing"

    def test_empty_list(self):
        """Порожній список не має викликати ZeroDivisionError"""
        mod = _import_exercise("exercise_5_complex_debug")
        if mod is None:
            pytest.skip("Файл ще не створено")

        result = mod.process_student_grades([])
        assert result['total_students'] == 0
        assert result['average_grade'] == 0


class TestExercise6DebugOrders:
    """Тести для завдання 6 - обробка замовлень"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_6_debug_orders.py").exists(), \
            "exercise_6_debug_orders.py не знайдено"

    def test_handles_missing_quantity(self):
        """Функція має обробляти відсутній quantity (default=1)"""
        mod = _import_exercise("exercise_6_debug_orders")
        if mod is None:
            pytest.skip("Файл ще не створено")

        order = [{'name': 'Book', 'price': 25}]
        result = mod.process_order(order)
        assert result['subtotal'] == 25

    def test_discount_calculation(self):
        """Знижка має рахуватися у відсотках"""
        mod = _import_exercise("exercise_6_debug_orders")
        if mod is None:
            pytest.skip("Файл ще не створено")

        order = [{'name': 'Item', 'price': 200, 'quantity': 1}]
        result = mod.process_order(order, discount_percent=10)
        assert result['discount'] == 20.0, f"Знижка 10% від 200 = 20, отримано {result['discount']}"

    def test_total_is_positive(self):
        """Total має бути subtotal - discount (додатне число)"""
        mod = _import_exercise("exercise_6_debug_orders")
        if mod is None:
            pytest.skip("Файл ще не створено")

        order = [{'name': 'Item', 'price': 200, 'quantity': 1}]
        result = mod.process_order(order, discount_percent=10)
        assert result['total'] == 180.0, f"200 - 20 = 180, отримано {result['total']}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])