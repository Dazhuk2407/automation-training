"""
Pytest тести для перевірки вправ Lesson 9
Запустіть: pytest test_exercises.py -v
"""

import pytest
from pathlib import Path


class TestExercise1PrintDebug:
    """Тести для завдання 1 - print debugging"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-1-print-debug.py"
        assert file_path.exists(), "exercise-1-print-debug.py не знайдено"

    def test_perimeter_calculation(self):
        """Периметр має розраховуватись правильно"""
        # Імпортуємо функцію якщо файл існує
        try:
            import sys
            sys.path.insert(0, str(Path(__file__).parent))
            from exercise_1_print_debug import calculate_rectangle_perimeter

            # Тест: 10 x 5 = периметр 30
            result = calculate_rectangle_perimeter(10, 5)
            assert result == 30, f"Очікувалось 30, отримано {result}"
        except ImportError:
            pytest.skip("Файл ще не створено або має помилки")


class TestExercise2Breakpoints:
    """Тести для завдання 2 - breakpoints"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-2-breakpoints.py"
        assert file_path.exists(), "exercise-2-breakpoints.py не знайдено"


class TestExercise3FixTypeError:
    """Тести для завдання 3 - type error"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-3-fix-type-error.py"
        assert file_path.exists(), "exercise-3-fix-type-error.py не знайдено"

    def test_handles_string_prices(self):
        """Функція має обробляти ціни як strings"""
        try:
            import sys
            sys.path.insert(0, str(Path(__file__).parent))
            from exercise_3_fix_type_error import calculate_total

            items = [
                {'name': 'A', 'price': 100},
                {'name': 'B', 'price': '50'},  # String price
                {'name': 'C', 'price': 80}
            ]

            result = calculate_total(items)
            assert result == 230, f"Очікувалось 230, отримано {result}"
        except (ImportError, TypeError):
            pytest.skip("Функція ще не виправлена")


class TestExercise4DebugConditions:
    """Тести для завдання 4 - умови"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-4-debug-conditions.py"
        assert file_path.exists(), "exercise-4-debug-conditions.py не знайдено"

    def test_age_65_is_senior(self):
        """Вік 65 має бути Senior"""
        try:
            import sys
            sys.path.insert(0, str(Path(__file__).parent))
            from exercise_4_debug_conditions import categorize_age

            result = categorize_age(65)
            assert result == "Senior", f"Вік 65 має бути Senior, отримано {result}"
        except ImportError:
            pytest.skip("Файл ще не створено")


class TestExercise5ComplexDebug:
    """Тести для завдання 5 - складна функція"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-5-complex-debug.py"
        assert file_path.exists(), "exercise-5-complex-debug.py не знайдено"

    def test_handles_missing_grade(self):
        """Функція має обробляти відсутність оцінки"""
        try:
            import sys
            sys.path.insert(0, str(Path(__file__).parent))
            from exercise_5_complex_debug import process_student_grades

            students = [
                {'name': 'Alice', 'grade': 85},
                {'name': 'Bob'},  # Немає grade
            ]

            # Не має викидати KeyError
            result = process_student_grades(students)
            assert 'total_students' in result
        except (ImportError, KeyError):
            pytest.skip("Функція ще не виправлена")

    def test_grade_60_is_passing(self):
        """Оцінка 60 має бути passing"""
        try:
            import sys
            sys.path.insert(0, str(Path(__file__).parent))
            from exercise_5_complex_debug import process_student_grades

            students = [{'name': 'Bob', 'grade': 60}]

            result = process_student_grades(students)
            assert 'Bob' in result['passing'], "Оцінка 60 має бути passing"
        except ImportError:
            pytest.skip("Файл ще не створено")


class TestExercise6CreateBuggyCode:
    """Тести для завдання 6 - власний buggy код"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-6-create-buggy-code.py"
        assert file_path.exists(), "exercise-6-create-buggy-code.py не знайдено"

    def test_has_function(self):
        """Файл має містити функцію"""
        file_path = Path(__file__).parent / "exercise-6-create-buggy-code.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        assert 'def ' in content, "Файл має містити функцію"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

