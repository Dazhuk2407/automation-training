"""
Lesson 12: Example 1 - Basic Type Hints
Демонстрація type hints для функцій та змінних
"""
from typing import List, Dict, Tuple


def add(x: int, y: int) -> int:
    """Додати два числа."""
    return x + y


def greet(name: str) -> str:
    """Привітати користувача."""
    return f"Hello, {name}!"


def calculate_average(numbers: List[float]) -> float:
    """Розрахувати середнє значення."""
    return sum(numbers) / len(numbers)


def demonstrate_variable_hints():
    """Змінні з type hints."""
    name: str = "Alice"
    age: int = 25
    grades: List[int] = [85, 90, 78]
    user: Dict[str, str] = {"name": "Bob", "email": "bob@example.com"}
    coords: Tuple[float, float] = (10.5, 20.3)

    print(f"name: {name} ({type(name).__name__})")
    print(f"age: {age} ({type(age).__name__})")
    print(f"grades: {grades}")
    print(f"user: {user}")
    print(f"coords: {coords}")


if __name__ == "__main__":
    print("=== Функції з type hints ===")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"greet('Alice') = {greet('Alice')}")
    print(f"calculate_average([85, 90, 78]) = {calculate_average([85.0, 90.0, 78.0])}")

    print("\n=== Змінні з type hints ===")
    demonstrate_variable_hints()