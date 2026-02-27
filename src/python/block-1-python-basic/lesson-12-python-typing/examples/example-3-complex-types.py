"""
Lesson 12: Example 3 - Complex Type Annotations
"""
from typing import List, Dict, Optional, Callable
# Складні типи
def process_users(
    users: List[Dict[str, any]]
) -> Dict[str, List[str]]:
    """Групувати користувачів за статусом."""
    result: Dict[str, List[str]] = {"active": [], "inactive": []}
    for user in users:
        status = user.get("status", "inactive")
        result[status].append(user["name"])
    return result
# Callable - функція як параметр
def apply_operation(
    numbers: List[int],
    operation: Callable[[int], int]
) -> List[int]:
    """Застосувати операцію до кожного числа."""
    return [operation(n) for n in numbers]
def double(x: int) -> int:
    return x * 2
# Демо
users = [
    {"name": "Alice", "status": "active"},
  """
Lesson 12: Example 3 - Complex Type Annotations
"""
from typing import List, Dict, Optional, Callable
# Складні типи
def process_users(
   rsLe ["""
from typing import List, Dict, Optional, Crsfrdo# Складні типи
def process_users(
   redef process_usercat > /Users/ivan.dazhuk/workspace/automation-training/src/python/block-1-python-basic/lesson-12-python-typing/exercises/EXERCISES.md << 'EOF'
# Lesson 12: Python Typing - Exercises
## Exercise 1: Basic type hints (EASY)
Add type hints to simple functions
## Exercise 2: List, Dict, Tuple types (EASY)
Use typing module for collections
## Exercise 3: Optional types (MEDIUM)
Handle functions that can return None
## Exercise 4: Union types (MEDIUM)
Functions accepting multiple types
## Exercise 5: Complex annotations (HARD)
Nested types and Callable
## Exercise 6: mypy validation (HARD)
Run mypy and fix all type errors
See examples for patterns and best practices.
