# Приклади - Lesson 13: Python typing

## Динамічна типізація

```python
"""
Приклади динамічної типізації Python.
"""

# Python сам визначає тип
x = 5
print(f"x = {x}, type = {type(x)}")  # int

x = "hello"
print(f"x = {x}, type = {type(x)}")  # str

x = 3.14
print(f"x = {x}, type = {type(x)}")  # float
```

## Type Hints для функцій

```python
from typing import List, Dict, Optional

# Функція з type hints
def add(x: int, y: int) -> int:
    """Додати два числа."""
    return x + y

result = add(5, 3)
print(f"Result: {result}")


# Функція повертаючи список
def create_list(count: int) -> List[int]:
    """Створити список чисел."""
    return list(range(count))

numbers = create_list(5)
print(f"Numbers: {numbers}")


# Функція з Optional
def find_user(user_id: int) -> Optional[str]:
    """Знайти користувача або None."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

user = find_user(1)
print(f"User: {user}")
```

## Type Hints для змінних

```python
from typing import List, Dict, Tuple, Set

# Базові типи
name: str = "Alice"
age: int = 25
height: float = 5.7
is_active: bool = True
result: Optional[str] = None

# Контейнери
numbers: List[int] = [1, 2, 3, 4, 5]
ages: Dict[str, int] = {"Alice": 25, "Bob": 30}
coordinates: Tuple[float, float] = (10.5, 20.3)
unique_ids: Set[int] = {1, 2, 3, 4, 5}

print(f"Name: {name}")
print(f"Numbers: {numbers}")
print(f"Ages: {ages}")
```

## Комплексна функція

```python
from typing import List, Dict

def process_users(users: List[Dict[str, str]]) -> Dict[str, int]:
    """Обробити користувачів та повернути їхID."""
    result: Dict[str, int] = {}
    
    for i, user in enumerate(users):
        result[user["name"]] = i + 1
    
    return result

users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
]

user_ids = process_users(users)
print(f"User IDs: {user_ids}")
```
