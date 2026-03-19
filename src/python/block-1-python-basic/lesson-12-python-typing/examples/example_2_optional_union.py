"""
Lesson 12: Example 2 - Optional and Union
Демонстрація Optional (може бути None) та Union (кілька типів)
"""
from typing import Optional, Union, List


def find_user(user_id: int) -> Optional[str]:
    """Знайти користувача. Повертає ім'я або None."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)


def square(number: Union[int, float]) -> Union[int, float]:
    """Піднести до квадрату. Приймає int або float."""
    return number ** 2


def process_data(data: Union[str, List[str]]) -> List[str]:
    """Нормалізувати до списку рядків."""
    if isinstance(data, str):
        return [data]
    return data


if __name__ == "__main__":
    print("=== Optional ===")
    print(f"find_user(1) = {find_user(1)}")
    print(f"find_user(99) = {find_user(99)}")

    print("\n=== Union ===")
    print(f"square(5) = {square(5)}")
    print(f"square(2.5) = {square(2.5)}")

    print(f"\nprocess_data('hello') = {process_data('hello')}")
    print(f"process_data(['a','b']) = {process_data(['a', 'b'])}")