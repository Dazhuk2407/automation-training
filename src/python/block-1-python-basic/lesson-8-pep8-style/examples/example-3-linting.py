"""
Lesson 8: Example 3 - Помилки flake8 та pylint
Демонстрація типових помилок які знаходять лінтери
"""

import os
import sys  # E401: multiple imports on one line (якщо на одному рядку)

# E302: expected 2 blank lines, found 1
def function_with_errors():
    """Функція з типовими помилками."""
    unused_variable = 10  # W0612: unused variable (pylint)
    x=1+2  # E225: missing whitespace around operator

    # W291: trailing whitespace (пробіл в кінці рядка)
    y = 3 + 4

    return x  # unused_variable не використовується


# E303: too many blank lines (4)




def another_function():
    """Ще одна функція."""
    # E501: line too long (>79 characters) - наступний рядок
    very_long_variable_name = "This is a very long string that exceeds the recommended line length of 79 characters according to PEP 8"
    return very_long_variable_name


# === ПРАВИЛЬНИЙ КОД (БЕЗ ПОМИЛОК) ===


def good_function():
    """Функція без помилок."""
    result = 1 + 2
    processed = result * 3
    return processed


def calculate_area(length, width):
    """
    Розрахувати площу прямокутника.

    Args:
        length: Довжина
        width: Ширина

    Returns:
        Площа
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")

    area = length * width
    return area


class DataValidator:
    """Валідатор даних."""

    def __init__(self, data):
        """Ініціалізація валідатора."""
        self.data = data
        self.errors = []

    def validate(self):
        """Валідувати дані."""
        if not self.data:
            self.errors.append("Data is empty")
            return False

        if not isinstance(self.data, (list, dict)):
            self.errors.append("Data must be list or dict")
            return False

        return True


# === ДЕМОНСТРАЦІЯ ===


if __name__ == "__main__":
    print("=" * 70)
    print("ТИПОВІ ПОМИЛКИ FLAKE8/PYLINT")
    print("=" * 70)

    print("\n❌ Помилки у цьому файлі:")
    print("  E225: x=1+2 (без пробілів навколо оператора)")
    print("  E302: недостатньо порожніх рядків перед функцією")
    print("  E303: забагато порожніх рядків")
    print("  E501: рядок довший за 79 символів")
    print("  W0612: невикористана змінна (pylint)")
    print("  W291: пробіл в кінці рядка")

    print("\n✅ Як перевірити:")
    print("  flake8 example-3-linting.py")
    print("  pylint example-3-linting.py")

    print("\n✅ Як виправити:")
    print("  1. Вручну виправити помилки")
    print("  2. Використати black: black example-3-linting.py")
    print("  3. Використати autopep8: autopep8 --in-place example-3-linting.py")

    # Демонстрація правильного коду
    print("\n" + "=" * 70)
    print("ДЕМОНСТРАЦІЯ ПРАВИЛЬНОГО КОДУ")
    print("=" * 70)

    area = calculate_area(10, 5)
    print(f"\nПлоща прямокутника: {area}")

    validator = DataValidator([1, 2, 3])
    is_valid = validator.validate()
    print(f"Дані валідні: {is_valid}")

    print("\n" + "=" * 70)
    print("РЕЙТИНГ ЯКОСТІ КОДУ")
    print("=" * 70)
    print("Запустіть: pylint example-3-linting.py --score=yes")
    print("Очікуваний рейтинг: 5-7/10 (через навмисні помилки)")

