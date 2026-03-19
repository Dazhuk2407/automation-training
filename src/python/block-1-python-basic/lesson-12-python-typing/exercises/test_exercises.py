"""
Pytest тести для перевірки вправ Lesson 12
Запустіть: pytest test_exercises.py -v
"""

import importlib.util
import inspect
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


class TestExercise1BasicTypeHints:
    """Тести для завдання 1 — базові type hints"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_1_basic_type_hints.py").exists(), \
            "exercise_1_basic_type_hints.py не знайдено"

    def test_add(self):
        mod = _import_exercise("exercise_1_basic_type_hints")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.add(5, 3) == 8

    def test_concat(self):
        mod = _import_exercise("exercise_1_basic_type_hints")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.concat("Hello", "World") == "Hello World"

    def test_is_adult(self):
        mod = _import_exercise("exercise_1_basic_type_hints")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.is_adult(25) is True
        assert mod.is_adult(10) is False

    def test_repeat_text(self):
        mod = _import_exercise("exercise_1_basic_type_hints")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.repeat_text("ha", 3) == "hahaha"

    def test_all_functions_have_annotations(self):
        mod = _import_exercise("exercise_1_basic_type_hints")
        if mod is None:
            pytest.skip("Файл ще не створено")
        for name in ['add', 'concat', 'is_adult', 'repeat_text']:
            func = getattr(mod, name)
            hints = getattr(func, '__annotations__', {})
            assert 'return' in hints, f"{name}() має мати return type hint"
            params = [k for k in hints if k != 'return']
            assert len(params) > 0, f"{name}() має мати type hints для параметрів"


class TestExercise2ContainerTypes:
    """Тести для завдання 2 — List, Dict, Tuple, Set"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_2_container_types.py").exists(), \
            "exercise_2_container_types.py не знайдено"

    def test_get_even_numbers(self):
        mod = _import_exercise("exercise_2_container_types")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_count_words(self):
        mod = _import_exercise("exercise_2_container_types")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.count_words("hello world hello")
        assert result['hello'] == 2
        assert result['world'] == 1

    def test_get_min_max(self):
        mod = _import_exercise("exercise_2_container_types")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.get_min_max([5, 2, 9, 1, 7]) == (1, 9)

    def test_get_unique_words(self):
        mod = _import_exercise("exercise_2_container_types")
        if mod is None:
            pytest.skip("Файл ще не створено")
        result = mod.get_unique_words("Hello hello World")
        assert result == {"hello", "world"}


class TestExercise3OptionalTypes:
    """Тести для завдання 3 — Optional"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_3_optional_types.py").exists(), \
            "exercise_3_optional_types.py не знайдено"

    def test_find_first_negative_found(self):
        mod = _import_exercise("exercise_3_optional_types")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.find_first_negative([1, 2, -3, 4]) == -3

    def test_find_first_negative_not_found(self):
        mod = _import_exercise("exercise_3_optional_types")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.find_first_negative([1, 2, 3]) is None

    def test_safe_divide(self):
        mod = _import_exercise("exercise_3_optional_types")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.safe_divide(10, 0) is None
        assert abs(mod.safe_divide(10, 3) - 3.333) < 0.01

    def test_find_user(self):
        mod = _import_exercise("exercise_3_optional_types")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.find_user(["Alice", "Bob"], "Bob") == 1
        assert mod.find_user(["Alice", "Bob"], "Charlie") is None


class TestExercise4UnionAndAny:
    """Тести для завдання 4 — Union та Any"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_4_union_and_any.py").exists(), \
            "exercise_4_union_and_any.py не знайдено"

    def test_format_value_int(self):
        mod = _import_exercise("exercise_4_union_and_any")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.format_value(42) == "Value: 42"

    def test_format_value_str(self):
        mod = _import_exercise("exercise_4_union_and_any")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.format_value("hello") == "Text: hello"

    def test_get_config_value(self):
        mod = _import_exercise("exercise_4_union_and_any")
        if mod is None:
            pytest.skip("Файл ще не створено")
        config = {"name": "App", "version": 1.0}
        assert mod.get_config_value(config, "name") == "App"
        assert mod.get_config_value(config, "missing") is None


class TestExercise5CallableAndNested:
    """Тести для завдання 5 — Callable та вкладені типи"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_5_callable_and_nested.py").exists(), \
            "exercise_5_callable_and_nested.py не знайдено"

    def test_apply_to_all(self):
        mod = _import_exercise("exercise_5_callable_and_nested")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.apply_to_all([1, 2, 3], mod.triple) == [3, 6, 9]
        assert mod.apply_to_all([10, 20], lambda x: x + 1) == [11, 21]

    def test_extract_names(self):
        mod = _import_exercise("exercise_5_callable_and_nested")
        if mod is None:
            pytest.skip("Файл ще не створено")
        users = [{"name": "Alice", "role": "admin"}, {"name": "Bob", "role": "user"}]
        assert mod.extract_names(users) == ["Alice", "Bob"]


class TestExercise6MypyValidation:
    """Тести для завдання 6 — mypy validation"""

    def test_file_exists(self):
        assert (EXERCISES_DIR / "exercise_6_mypy_validation.py").exists(), \
            "exercise_6_mypy_validation.py не знайдено"

    def test_sum_numbers(self):
        mod = _import_exercise("exercise_6_mypy_validation")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.sum_numbers([1, 2, 3]) == 6

    def test_find_longest(self):
        mod = _import_exercise("exercise_6_mypy_validation")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.find_longest(["hi", "hello", "hey"]) == "hello"
        assert mod.find_longest([]) is None

    def test_format_greeting(self):
        mod = _import_exercise("exercise_6_mypy_validation")
        if mod is None:
            pytest.skip("Файл ще не створено")
        assert mod.format_greeting("Alice", 25) == "Hello Alice, you are 25 years old"

    def test_has_annotations(self):
        mod = _import_exercise("exercise_6_mypy_validation")
        if mod is None:
            pytest.skip("Файл ще не створено")
        for name in ['sum_numbers', 'find_longest', 'format_greeting']:
            func = getattr(mod, name)
            hints = getattr(func, '__annotations__', {})
            assert 'return' in hints, f"{name}() має мати return type hint"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
