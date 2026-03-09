"""
Lesson 7: Example 1 - File Structure and Comments

Цей модуль демонструє правильну структуру Python файлу:
1. Docstring модуля (цей текст)
2. Imports (бібліотеки)
3. Constants (константи)
4. Classes (класи)
5. Functions (функції)
6. Main block (головний код)
"""

# === ІМПОРТИ ===
from datetime import datetime


# === КОНСТАНТИ ===
MAX_RETRIES = 3
APP_VERSION = "1.0.0"


# === КЛАСИ ===
class Person:
    """Клас для представлення людини."""

    def __init__(self, name: str, age: int):
        """
        Ініціалізація об'єкта Person.

        Args:
            name: Ім'я людини
            age: Вік людини
        """
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        """Повертає рядкове представлення об'єкта для debugging."""
        return f"Person(name='{self.name}', age={self.age})"


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
    """
    Обчислити вік на основі року народження.

    Args:
        birth_year: Рік народження

    Returns:
        Вік у роках
    """
    current_year = datetime.now().year
    return current_year - birth_year


def main() -> None:
    """Головна функція програми."""
    # Привітання
    print(greet("Alice"))

    # Розрахунок віку
    age = calculate_age(2000)
    print(f"Age: {age}")

    # Створення об'єкта
    person = Person("Bob", 30)
    print(f"Person: {person}")


# === ГОЛОВНИЙ КОД ===
if __name__ == "__main__":
    main()

