"""
Lesson 12: Example 2 - Optional and Union
"""
from typing import Optional, Union, List
# Optional - може бути None
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)
# Union - кілька типів
def square(number: Union[int, float]) -> Union[int, float]:
    return number ** 2
def process_data(data: Union[str, List[str]]) -> List[str]:
    if isinstance(data, str):
        return [data]
    return data
# Демо
print("find_user(1) =", find_user(1))
print("find_user(99) =", find_user(99))
print("\nsquare(5) =", square(5))
print("square(2.5) =", square(2.5))
print("\nprocess_data('hello') =", process_data('hello'))
print("process_data(['a','b']) =", process_data(['a', 'b']))
