# Вправи - Lesson 13: Python typing

## Завдання 1: Type hints для функцій

```python
# Напишіть функції з type hints

# 1. Функція яка додає числа
def add(x: int, y: int) -> int:
    return x + y

# 2. Функція яка поверттає рядок
def greet(name: str) -> str:
    return f"Hello, {name}!"

# 3. Функція з multiple параметрами
def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)

# Запустіть функції
print(add(5, 3))
print(greet("Alice"))
print(calculate_bmi(70, 1.75))
```

## Завдання 2: Type hints для змінних

```python
from typing import List, Dict, Optional

# Напишіть змінні з type hints

# Базові типи
name: str = "Alice"
age: int = 25
height: float = 5.7
active: bool = True

# Контейнери
numbers: List[int] = [1, 2, 3]
user_ages: Dict[str, int] = {"Alice": 25, "Bob": 30}
optional_value: Optional[str] = None

print(f"Name: {name}")
print(f"Numbers: {numbers}")
print(f"User ages: {user_ages}")
```

## Завдання 3: Комплексна функція

```python
from typing import List, Dict

def summarize_users(
    users: List[Dict[str, str]]
) -> Dict[str, str]:
    """Обробити користувачів."""
    result: Dict[str, str] = {}
    
    for user in users:
        result[user["name"]] = user["email"]
    
    return result

# Тестування
users_data = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
]

result = summarize_users(users_data)
print(result)
```

## Завдання 4: Mypy type checker

```bash
# Встановіть mypy
pip install mypy

# Перевірте ваш файл
mypy your_file.py
```

## Завдання 5: Розумійте помилки

```python
# ❌ Неправильно - тип не відповідає
x: int = "hello"  # Type error

# ✅ Правильно
x: str = "hello"  # OK
y: int = 42       # OK
```

---

**✅ Завершили Lesson 13 - Цей розділ (Block 1) закінчено!** 🎉

## Що ви вивчили у Block 1: Python Basics

✅ Lesson 1: Install Python and prepare your working environment
✅ Lesson 2: Install and set up an IDE (PyCharm or VS Code)
✅ Lesson 3: Running Python code from terminal and IDE
✅ Lesson 4: Create and use a virtual environment (venv)
✅ Lesson 5: Install packages with pip
✅ Lesson 6: Working with requirements.txt (install, freeze, update)
✅ Lesson 7: Basic Python syntax
✅ Lesson 8: PEP 8 (indentation, formatting, comments)
✅ Lesson 9: Code formatting and indentation
✅ Lesson 10: Basic debugging in IDE (breakpoints, step execution, variable inspection)
✅ Lesson 11: Variables, basic data types, and type conversion
✅ Lesson 12: Built-in functions (print, input, dir, id)
✅ Lesson 13: Understanding how Python typing works

## Що дальше?

Переходьте до **Block 2: Python Advanced** для вивчення:
- Умовних конструкцій (if/elif/else)
- Циклів (for/while)
- Функцій та параметрів
- Списків, словників, множин
- Класів та об'єктів
- Модулів та пакетів

Успіхів! 🚀
