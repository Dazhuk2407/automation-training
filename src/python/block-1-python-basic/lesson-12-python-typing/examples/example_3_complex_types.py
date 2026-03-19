"""
Lesson 12: Example 3 - Complex Type Annotations
Демонстрація Callable, вкладених типів та Dict[str, Any]
"""
from typing import List, Dict, Any, Callable


def process_users(
    users: List[Dict[str, Any]]
) -> Dict[str, List[str]]:
    """Групувати користувачів за статусом."""
    result: Dict[str, List[str]] = {"active": [], "inactive": []}
    for user in users:
        status = user.get("status", "inactive")
        result[status].append(user["name"])
    return result


def apply_operation(
    numbers: List[int],
    operation: Callable[[int], int]
) -> List[int]:
    """Застосувати операцію до кожного числа."""
    return [operation(n) for n in numbers]


def double(x: int) -> int:
    """Подвоїти число."""
    return x * 2


if __name__ == "__main__":
    print("=== Вкладені типи ===")
    users = [
        {"name": "Alice", "status": "active"},
        {"name": "Bob", "status": "inactive"},
        {"name": "Charlie", "status": "active"},
    ]
    grouped = process_users(users)
    print(f"Active: {grouped['active']}")
    print(f"Inactive: {grouped['inactive']}")

    print("\n=== Callable ===")
    numbers = [1, 2, 3, 4, 5]
    doubled = apply_operation(numbers, double)
    print(f"Original: {numbers}")
    print(f"Doubled: {doubled}")