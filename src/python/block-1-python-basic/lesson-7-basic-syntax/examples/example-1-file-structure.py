"""
Lesson 7: Example 1 - File Structure and Comments
Демонстрація структури Python файлу та коментарів
"""

# === ІМПОРТИ ===
import sys
from datetime import datetime

# === КОНСТАНТИ ===
MAX_RETRIES = 3
APP_VERSION = "1.0.0"

# === ФУНКЦІЇ ===
def greet(name: str) -> str:
    """
    Привітати користувача.

    Args:
        name: Ім'я користувача

    Returns:
        Рядок привітання
    """
    return f"Hello, {name}!"


def calculate_age(birth_year: int) -> int:
    """Обчислити вік на основі року народження."""
    current_year = datetime.now().year
    return current_year - birth_year


# === КЛАСИ ===
class Person:
    """Клас для представлення людини."""

    def __init__(self, name: str, age: int):
        self.name = name  # Ім'я людини
        self.age = age    # Вік людини


# === ГОЛОВНИЙ КОД ===
if __name__ == "__main__":
    # Привітання
    print(greet("Alice"))

    # Розрахунок віку
    age = calculate_age(2000)
    print(f"Age: {age}")

    # Створення об'єкта
    person = Person("Bob", 30)
    print(f"Person: {person.name}, {person.age} years old")

