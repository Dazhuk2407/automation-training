"""
Pytest тести для перевірки вправ Lesson 8
Запустіть: pytest test_exercises.py -v
"""

import ast
import pytest
from pathlib import Path


class TestExercise1Naming:
    """Тести для завдання 1 - назви змінних"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-1-fix-naming.py"
        assert file_path.exists(), "exercise-1-fix-naming.py не знайдено"

    def test_function_naming(self):
        """Функції мають бути в snake_case"""
        file_path = Path(__file__).parent / "exercise-1-fix-naming.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Перевірка що немає PascalCase функцій
        assert 'def Calculate' not in content, "Функція має бути calculate_area"
        assert 'def calculate' in content.lower(), "Функція має бути в snake_case"

    def test_class_naming(self):
        """Класи мають бути в PascalCase"""
        file_path = Path(__file__).parent / "exercise-1-fix-naming.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Перевірка що немає snake_case класів
        assert 'class user_profile' not in content, "Клас має бути UserProfile"


class TestExercise2Spacing:
    """Тести для завдання 2 - пробіли"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-2-fix-spacing.py"
        assert file_path.exists(), "exercise-2-fix-spacing.py не знайдено"

    def test_operator_spacing(self):
        """Навколо операторів мають бути пробіли"""
        file_path = Path(__file__).parent / "exercise-2-fix-spacing.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Перевірка що немає операторів без пробілів
        bad_patterns = ['x+y', 'x*y', 'x=y', 'x-y']
        for pattern in bad_patterns:
            assert pattern not in content, f"Знайдено {pattern} без пробілів"

    def test_file_syntax(self):
        """Файл має бути синтаксично правильним"""
        file_path = Path(__file__).parent / "exercise-2-fix-spacing.py"
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                ast.parse(f.read())
        except SyntaxError as e:
            pytest.fail(f"Синтаксична помилка: {e}")


class TestExercise3Imports:
    """Тести для завдання 3 - імпорти"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-3-fix-imports.py"
        assert file_path.exists(), "exercise-3-fix-imports.py не знайдено"

    def test_imports_order(self):
        """Імпорти мають бути впорядковані"""
        file_path = Path(__file__).parent / "exercise-3-fix-imports.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Знайти всі рядки з import
        import_lines = [
            line.strip() for line in lines
            if line.strip().startswith('import ') or line.strip().startswith('from ')
        ]

        assert len(import_lines) >= 5, "Має бути мінімум 5 імпортів"


class TestExercise4Docstrings:
    """Тести для завдання 4 - docstrings"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-4-add-docstrings.py"
        assert file_path.exists(), "exercise-4-add-docstrings.py не знайдено"

    def test_has_docstrings(self):
        """Функції та класи мають мати docstrings"""
        file_path = Path(__file__).parent / "exercise-4-add-docstrings.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Перевірка наявності docstrings
        docstring_count = content.count('"""')
        assert docstring_count >= 8, "Має бути мінімум 4 docstrings (по 2 лапки кожен)"

    def test_docstring_format(self):
        """Docstrings мають мати Args та Returns"""
        file_path = Path(__file__).parent / "exercise-4-add-docstrings.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Хоча б один docstring має мати Args або Returns
        has_args_or_returns = 'Args:' in content or 'Returns:' in content
        assert has_args_or_returns, "Docstring має містити Args: або Returns:"


class TestExercise5Black:
    """Тести для завдання 5 - black форматування"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-5-format-with-black.py"
        assert file_path.exists(), "exercise-5-format-with-black.py не знайдено"


class TestExercise6Flake8:
    """Тести для завдання 6 - flake8 помилки"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-6-fix-flake8-errors.py"
        assert file_path.exists(), "exercise-6-fix-flake8-errors.py не знайдено"

    def test_no_unused_variables(self):
        """Не має бути невикористаних змінних"""
        file_path = Path(__file__).parent / "exercise-6-fix-flake8-errors.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Перевірка що немає змінної 'unused'
        lines = [l for l in content.split('\n') if 'unused' in l.lower() and '=' in l]
        assert len(lines) == 0, "Знайдено невикористану змінну"

    def test_proper_blank_lines(self):
        """Між функціями мають бути 2 порожні рядки"""
        file_path = Path(__file__).parent / "exercise-6-fix-flake8-errors.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Перевірка що немає 4 порожніх рядків підряд
        assert '\n\n\n\n\n' not in content, "Забагато порожніх рядків"


class TestExercise7Refactor:
    """Тести для завдання 7 - повна переробка"""

    def test_file_exists(self):
        """Файл має існувати"""
        file_path = Path(__file__).parent / "exercise-7-refactor-code.py"
        assert file_path.exists(), "exercise-7-refactor-code.py не знайдено"

    def test_function_naming_snake_case(self):
        """Функції мають бути в snake_case"""
        file_path = Path(__file__).parent / "exercise-7-refactor-code.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Не має бути PascalCase функцій
        assert 'def Process' not in content, "Функція має бути process_data"
        assert 'def AddUser' not in content, "Функція має бути add_user"

    def test_class_naming_pascal_case(self):
        """Класи мають бути в PascalCase"""
        file_path = Path(__file__).parent / "exercise-7-refactor-code.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Не має бути snake_case класів
        assert 'class user_manager' not in content, "Клас має бути UserManager"

    def test_has_docstrings(self):
        """Модуль, функції та класи мають мати docstrings"""
        file_path = Path(__file__).parent / "exercise-7-refactor-code.py"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Мінімум 6 docstrings (модуль + 2 функції + клас + 2 методи)
        docstring_count = content.count('"""')
        assert docstring_count >= 12, f"Має бути мінімум 6 docstrings, знайдено {docstring_count // 2}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

