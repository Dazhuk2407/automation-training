"""
Pytest тести для перевірки вправ Lesson 11
Запустіть: pytest test_exercises.py -v
"""

import importlib.util
import pytest
from pathlib import Path

EXERCISES_DIR = Path(__file__).parent


def _import_exercise(module_name):
    """Імпортувати модуль вправи. Повертає None якщо файлу немає."""
    file_path = EXERCISES_DIR / f"{module_name}.py"
    if not file_path.exists():
        return None
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestExercise1InfoFunctions:
    """Тести для завдання 1 — len, type, isinstance"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_1_info_functions.py").exists(), \
            "exercise_1_info_functions.py не знайдено"

    def test_string_info(self):
        mod = _import_exercise("exercise_1_info_functions")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.get_object_info("hello")
        assert result['length'] == 5
        assert result['type_name'] == 'str'
        assert result['is_numeric'] is False

    def test_int_info(self):
        mod = _import_exercise("exercise_1_info_functions")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.get_object_info(42)
        assert result['length'] is None
        assert result['type_name'] == 'int'
        assert result['is_numeric'] is True

    def test_list_info(self):
        mod = _import_exercise("exercise_1_info_functions")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.get_object_info([1, 2, 3])
        assert result['length'] == 3
        assert result['type_name'] == 'list'


class TestExercise2Sequences:
    """Тести для завдання 2 — range, enumerate"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_2_sequences.py").exists(), \
            "exercise_2_sequences.py не знайдено"

    def test_even_numbers(self):
        mod = _import_exercise("exercise_2_sequences")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.even_numbers(10) == [0, 2, 4, 6, 8, 10]
        assert mod.even_numbers(5) == [0, 2, 4]
        assert mod.even_numbers(0) == [0]

    def test_numbered_items(self):
        mod = _import_exercise("exercise_2_sequences")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.numbered_items(['apple', 'banana'])
        assert result == ['1. apple', '2. banana']


class TestExercise3MathFunctions:
    """Тести для завдання 3 — sum, min, max, abs, round"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_3_math_functions.py").exists(), \
            "exercise_3_math_functions.py не знайдено"

    def test_analyze_numbers(self):
        mod = _import_exercise("exercise_3_math_functions")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.analyze_numbers([10, 20, 30])
        assert result['sum'] == 60
        assert result['min'] == 10
        assert result['max'] == 30
        assert result['average'] == 20.0
        assert result['range'] == 20

    def test_absolute_values(self):
        mod = _import_exercise("exercise_3_math_functions")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.absolute_values([-5.7, 3.2, -1.8])
        assert result == [5.7, 3.2, 1.8]


class TestExercise4SortAndZip:
    """Тести для завдання 4 — sorted, zip"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_4_sort_and_zip.py").exists(), \
            "exercise_4_sort_and_zip.py не знайдено"

    def test_sort_words(self):
        mod = _import_exercise("exercise_4_sort_and_zip")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.sort_words(['banana', 'apple', 'cherry'])
        assert result['alphabetical'] == ['apple', 'banana', 'cherry']
        assert result['reversed'] == ['cherry', 'banana', 'apple']
        assert result['by_length'] == ['apple', 'banana', 'cherry']

    def test_make_dict(self):
        mod = _import_exercise("exercise_4_sort_and_zip")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.make_dict(['a', 'b'], [1, 2])
        assert result == {'a': 1, 'b': 2}


class TestExercise5AllAny:
    """Тести для завдання 5 — all, any"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_5_all_any.py").exists(), \
            "exercise_5_all_any.py не знайдено"

    def test_check_numbers_all_even(self):
        mod = _import_exercise("exercise_5_all_any")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.check_numbers([2, 4, 6])
        assert result['all_even'] is True
        assert result['all_positive'] is True
        assert result['any_negative'] is False

    def test_check_numbers_mixed(self):
        mod = _import_exercise("exercise_5_all_any")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.check_numbers([2, -3, 6, 101])
        assert result['all_even'] is False
        assert result['any_negative'] is True
        assert result['any_greater_than_100'] is True

    def test_check_passwords(self):
        mod = _import_exercise("exercise_5_all_any")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.check_passwords(["abc", "password123"])
        assert result['all_long_enough'] is False
        assert result['any_has_digit'] is True


class TestExercise6Statistics:
    """Тести для завдання 6 — калькулятор статистики"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_6_statistics.py").exists(), \
            "exercise_6_statistics.py не знайдено"

    def test_calculate_statistics(self):
        mod = _import_exercise("exercise_6_statistics")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.calculate_statistics([10, 20, 30])
        assert result['count'] == 3
        assert result['total'] == 60
        assert result['average'] == 20.0
        assert result['minimum'] == 10
        assert result['maximum'] == 30

    def test_has_print_report(self):
        mod = _import_exercise("exercise_6_statistics")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert hasattr(mod, 'print_report'), "Має містити функцію print_report"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])