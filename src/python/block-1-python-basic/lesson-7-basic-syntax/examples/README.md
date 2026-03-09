# Приклади - Lesson 7: Basic Python syntax

## Простий скрипт

```python
"""
Простий приклад структури Python файлу.
"""

# Імпорти
import sys
from datetime import datetime


# Константи
GREETING = "Hello"
MAX_ATTEMPTS = 3


# Функція
def greet_user(name: str) -> str:
    """Привіти користувача по імені."""
    return f"{GREETING}, {name}!"


# Клас
class Counter:
    """Лічильник для підрахунку."""
    
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Збільшити лічильник."""
        self.count += 1
        return self.count


# Головна функція
def main():
    """Головна точка входу."""
    print(greet_user("Alice"))
    
    counter = Counter()
    for i in range(3):
        print(f"Count: {counter.increment()}")


# Цей блок виконується тільки при прямому запуску
if __name__ == "__main__":
    main()
```

## Коментарі vs Docstrings

```python
# Це однорядковий коментар
x = 5  # Інлайн коментар

"""
Це docstring - опис модуля.
Може бути багатьма рядків.
"""

def my_function():
    """Це docstring функції - видно через help()."""
    pass
```
