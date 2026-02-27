"""
Lesson 12: Example 1 - Basic Type Hints
"""
from typing import List, Dict, Tuple
# Функції з type hints
def add(x: int, y: int) -> int:
    return x + y
def greet(name: str) -> str:
    return f"Hello, {name}!"
def calculate_average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)
# Змінні з type hints
name: str = "Alice"
age: int = 25
grades: List[int] = [85, 90, 78]
user: Dict[str, str] = {"name": "Bob", "email": "bob@example.com"}
coords: Tuple[float, float] = (10.5, 20.3)
# Демо
print("add(5, 3) =", add(5, 3))
print("greet('Alice') =", greet('Alice'))
print("calculate_average([85, 90, 78]) =", calculate_average([85.0, 90.0, 78.0]))
