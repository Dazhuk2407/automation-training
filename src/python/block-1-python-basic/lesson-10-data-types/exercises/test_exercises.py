"""
Pytest тести для перевірки вправ Lesson 10
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


class TestExercise1AllTypes:
    """Тести для завдання 1 — всі основні типи"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_1_all_types.py").exists(), \
            "exercise_1_all_types.py не знайдено"

    def test_get_all_types_returns_dict(self):
        mod = _import_exercise("exercise_1_all_types")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.get_all_types()
        assert isinstance(result, dict), "get_all_types() має повертати dict"

    def test_all_five_types_present(self):
        mod = _import_exercise("exercise_1_all_types")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.get_all_types()
        assert isinstance(result['str'], str), "Значення 'str' має бути типу str"
        assert isinstance(result['int'], int), "Значення 'int' має бути типу int"
        assert isinstance(result['float'], float), "Значення 'float' має бути типу float"
        assert isinstance(result['bool'], bool), "Значення 'bool' має бути типу bool"
        assert result['none'] is None, "Значення 'none' має бути None"


class TestExercise2TypeConversion:
    """Тести для завдання 2 — конверсія типів"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_2_type_conversion.py").exists(), \
            "exercise_2_type_conversion.py не знайдено"

    def test_convert_to_int(self):
        mod = _import_exercise("exercise_2_type_conversion")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.convert_to_int("42") == 42
        assert mod.convert_to_int(3.14) == 3

    def test_convert_to_float(self):
        mod = _import_exercise("exercise_2_type_conversion")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.convert_to_float("3.14") == 3.14
        assert mod.convert_to_float(42) == 42.0

    def test_convert_to_str(self):
        mod = _import_exercise("exercise_2_type_conversion")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.convert_to_str(42) == "42"
        assert mod.convert_to_str(True) == "True"

    def test_convert_to_bool(self):
        mod = _import_exercise("exercise_2_type_conversion")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.convert_to_bool(1) is True
        assert mod.convert_to_bool(0) is False
        assert mod.convert_to_bool("") is False
        assert mod.convert_to_bool("hello") is True


class TestExercise3TruthyFalsy:
    """Тести для завдання 3 — truthy/falsy"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_3_truthy_falsy.py").exists(), \
            "exercise_3_truthy_falsy.py не знайдено"

    def test_falsy_values(self):
        mod = _import_exercise("exercise_3_truthy_falsy")
        if mod is None:
            pytest.skip("Файл ще не створено")
        for val in [0, 0.0, "", [], None, False]:
            assert mod.is_truthy(val) is False, f"is_truthy({val!r}) має бути False"

    def test_truthy_values(self):
        mod = _import_exercise("exercise_3_truthy_falsy")
        if mod is None:
            pytest.skip("Файл ще не створено")
        for val in [1, -1, 3.14, "hello", "False", [0], True]:
            assert mod.is_truthy(val) is True, f"is_truthy({val!r}) має бути True"


class TestExercise4SafeConvert:
    """Тести для завдання 4 — safe_int()"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_4_safe_convert.py").exists(), \
            "exercise_4_safe_convert.py не знайдено"

    def test_valid_conversion(self):
        mod = _import_exercise("exercise_4_safe_convert")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.safe_int("42") == 42
        assert mod.safe_int("100", default=-1) == 100

    def test_invalid_string(self):
        mod = _import_exercise("exercise_4_safe_convert")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.safe_int("abc") == 0
        assert mod.safe_int("abc", default=-1) == -1

    def test_none_value(self):
        mod = _import_exercise("exercise_4_safe_convert")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.safe_int(None) == 0

    def test_custom_default(self):
        mod = _import_exercise("exercise_4_safe_convert")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.safe_int("??", default=99) == 99


class TestExercise5Calculator:
    """Тести для завдання 5 — калькулятор"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_5_calculator.py").exists(), \
            "exercise_5_calculator.py не знайдено"

    def test_add_numbers(self):
        mod = _import_exercise("exercise_5_calculator")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.add_values(10, 20) == 30.0

    def test_add_strings(self):
        mod = _import_exercise("exercise_5_calculator")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.add_values("10", "20") == 30.0
        assert mod.add_values("3.5", 2) == 5.5

    def test_invalid_returns_none(self):
        mod = _import_exercise("exercise_5_calculator")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.add_values("abc", 5) is None
        assert mod.add_values(None, 5) is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])