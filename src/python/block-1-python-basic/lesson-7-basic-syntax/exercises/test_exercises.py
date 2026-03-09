"""
Pytest тести для перевірки вправ Lesson 7.
Запуск з кореня проєкту:
pytest exercises/test_exercises.py -v
"""

import pytest
from pathlib import Path


class TestExercise1FileStructure:
    """Тести для завдання 1 - структура файлу"""

    def test_exercise_1_exists(self):
        """Файл exercise_1_structure.py має існувати"""
        file_path = Path(__file__).parent / "exercise_1_structure.py"
        assert file_path.exists(), "exercise_1_structure.py не знайдено"

    def test_exercise_1_has_docstring(self):
        """Файл має мати docstring"""
        file_path = Path(__file__).parent / "exercise_1_structure.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        assert '"""' in content or "'''" in content, "Файл повинен мати docstring"

    def test_exercise_1_has_function(self):
        """Файл має мати функцію"""
        file_path = Path(__file__).parent / "exercise_1_structure.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        assert 'def ' in content, "Файл повинен мати функцію"

    def test_exercise_1_has_main_block(self):
        """Файл має мати if __name__ == '__main__'"""
        file_path = Path(__file__).parent / "exercise_1_structure.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        assert '__main__' in content, "Файл повинен мати if __name__ == '__main__'"


class TestExercise2Comments:
    """Тести для завдання 2 - коментарі та docstrings"""

    def test_exercise_2_exists(self):
        """Файл exercise_2_comments.py має існувати"""
        file_path = Path(__file__).parent / "exercise_2_comments.py"
        assert file_path.exists(), "exercise_2_comments.py не знайдено"

    def test_exercise_2_has_module_docstring(self):
        """Файл має мати docstring модуля"""
        file_path = Path(__file__).parent / "exercise_2_comments.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        assert '"""' in content or "'''" in content, "Файл повинен мати docstring модуля"

    def test_exercise_2_has_function_docstring(self):
        """Функція має мати docstring з Args та Returns"""
        file_path = Path(__file__).parent / "exercise_2_comments.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        assert "Args:" in content, "Функція повинна мати секцію Args"
        assert "Returns:" in content, "Функція повинна мати секцію Returns"


class TestExercise3Variables:
    """Тести для завдання 3 - змінні всіх типів"""

    def test_exercise_3_exists(self):
        """Файл exercise_3_variables.py має існувати"""
        file_path = Path(__file__).parent / "exercise_3_variables.py"
        assert file_path.exists(), "exercise_3_variables.py не знайдено"

    def test_exercise_3_has_all_types(self):
        """Файл має мати змінні всіх типів"""
        file_path = Path(__file__).parent / "exercise_3_variables.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Перевіримо що є присвоювання для різних типів
        has_string = '"' in content or "'" in content
        has_int = any(c.isdigit() for c in content)
        has_float = any(token in content for token in ['0.0', '1.0', '2.5', '3.14'])
        has_bool = 'True' in content or 'False' in content
        has_none = 'None' in content

        assert has_string, "Повинна бути змінна типу str"
        assert has_int, "Повинна бути змінна типу int"
        assert has_float, "Повинна бути змінна типу float"
        assert has_bool, "Повинна бути змінна типу bool"
        assert has_none, "Повинна бути змінна типу None"


class TestExercise4MultipleAssignment:
    """Тести для завдання 4 - множинне присвоювання"""

    def test_exercise_4_exists(self):
        """Файл exercise_4_multiple_assignment.py має існувати"""
        file_path = Path(__file__).parent / "exercise_4_multiple_assignment.py"
        assert file_path.exists(), "exercise_4_multiple_assignment.py не знайдено"

    def test_exercise_4_has_multiple_assignment(self):
        """Файл має мати множинне присвоювання"""
        file_path = Path(__file__).parent / "exercise_4_multiple_assignment.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        has_multiple_assignment = (
                'x, y, z =' in content or
                'a, b =' in content or
                'x, y =' in content
        )
        assert has_multiple_assignment, "Повинне бути множинне присвоювання"


class TestExercise5Operators:
    """Тести для завдання 5 - оператори"""

    def test_exercise_5_exists(self):
        """Файл exercise_5_operators.py має існувати"""
        file_path = Path(__file__).parent / "exercise_5_operators.py"
        assert file_path.exists(), "exercise_5_operators.py не знайдено"

    def test_exercise_5_has_arithmetic_operations(self):
        """Файл повинен мати арифметичні операції"""
        file_path = Path(__file__).parent / "exercise_5_operators.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        operators = ['+', '-', '*', '/', '//', '%', '**']
        has_operators = sum(1 for op in operators if op in content) >= 3
        assert has_operators, "Повинні бути арифметичні операції"

    def test_exercise_5_has_comparison_and_logical_operations(self):
        """Файл повинен мати оператори порівняння та логічні оператори"""
        file_path = Path(__file__).parent / "exercise_5_operators.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        comparison_ops = ['==', '!=', '>', '<', '>=', '<=']
        logical_ops = ['and', 'or', 'not']

        has_comparison = any(op in content for op in comparison_ops)
        has_logical = any(op in content for op in logical_ops)

        assert has_comparison, "Повинні бути оператори порівняння"
        assert has_logical, "Повинні бути логічні оператори"


class TestExercise6SyntaxErrors:
    """Тести для завдання 6 - виправлення синтаксичних помилок"""

    def test_exercise_6_exists(self):
        """Файл exercise_6_syntax_errors.py має існувати"""
        file_path = Path(__file__).parent / "exercise_6_syntax_errors.py"
        assert file_path.exists(), "exercise_6_syntax_errors.py не знайдено"

    def test_exercise_6_is_valid_python(self):
        """Файл повинен бути синтаксично правильним Python кодом"""
        file_path = Path(__file__).parent / "exercise_6_syntax_errors.py"
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                compile(f.read(), str(file_path), 'exec')
        except SyntaxError as e:
            pytest.fail(f"Файл має синтаксичні помилки: {e}")


class TestExercise7CompleteProgram:
    """Тести для завдання 7 - комплексна програма"""

    def test_exercise_7_exists(self):
        """Файл exercise_7_complete_program.py має існувати"""
        file_path = Path(__file__).parent / "exercise_7_complete_program.py"
        assert file_path.exists(), "exercise_7_complete_program.py не знайдено"

    def test_exercise_7_has_all_functions(self):
        """Файл повинен мати всі три функції"""
        file_path = Path(__file__).parent / "exercise_7_complete_program.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        functions = [
            'calculate_rectangle_area',
            'calculate_rectangle_perimeter',
            'calculate_rectangle_diagonal'
        ]

        for func in functions:
            assert func in content, f"Функція {func} не знайдена"

    def test_exercise_7_has_docstrings(self):
        """Функції повинні мати docstrings"""
        file_path = Path(__file__).parent / "exercise_7_complete_program.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Перевіримо кількість docstrings
        docstring_count = content.count('"""')
        assert docstring_count >= 6, "Модуль та функції повинні мати docstrings"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

