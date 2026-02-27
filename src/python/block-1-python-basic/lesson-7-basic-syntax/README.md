# Lesson 7: Basic Python Syntax

## 🎯 Learning Outcomes (Що ви вмітимете після уроку)

- ✅ Розуміти структуру Python файлу
- ✅ Писати та використовувати коментарі
- ✅ Оголошувати змінні та присвоювати значення
- ✅ Використовувати базові оператори (арифметичні, порівняння, логічні)
- ✅ Розпізнавати типові синтаксичні помилки

---

## 📖 Теорія

### 1. Структура Python файлу

```python
"""
Docstring - опис модуля.
Це перший рядок файлу.
"""

# Імпорти
import sys
from datetime import datetime

# Константи
MAX_ATTEMPTS = 3
DEFAULT_NAME = "User"

# Функції
def greet(name):
    """Функція для привітання."""
    return f"Hello, {name}!"

# Класи
class Person:
    """Клас для представлення людини."""
    pass

# Головний код
if __name__ == "__main__":
    print(greet("Alice"))
```

---

### 2. Коментарі

```python
# Однорядковий коментар - починається з #

"""
Багаторядковий коментар або docstring
Використовується для опису модуля, функції або класу
"""

def calculate(x, y):
    """
    Це docstring функції.
    Видно через help(calculate)
    
    Args:
        x: Перше число
        y: Друге число
        
    Returns:
        Сума чисел
    """
    # Коментар всередині функції
    result = x + y  # Інлайн коментар
    return result
```

---

### 3. Змінні та присвоювання

```python
# Оголошення змінних
name = "Alice"           # string
age = 25                # int
height = 5.7            # float
is_student = True       # bool
result = None           # NoneType

# Множественне присвоювання
x, y, z = 1, 2, 3

# Swap змінних
a, b = 10, 20
a, b = b, a  # a=20, b=10

# Правила назвування змінних
valid_name = "OK"       # ✅ lowercase_with_underscores
_private = "OK"         # ✅ приватна змінна
CONSTANT = "OK"         # ✅ константа UPPERCASE
# invalidName = "Bad"   # ❌ camelCase в Python не прийнято
```

---

### 4. Оператори

#### Арифметичні оператори
```python
x, y = 10, 3

print(x + y)   # 13 (додавання)
print(x - y)   # 7 (віднімання)
print(x * y)   # 30 (множення)
print(x / y)   # 3.333... (ділення)
print(x // y)  # 3 (ціле ділення)
print(x % y)   # 1 (остача)
print(x ** y)  # 1000 (піднесення в степень)
```

#### Оператори порівняння
```python
x, y = 10, 5

print(x == y)  # False (рівність)
print(x != y)  # True (не рівність)
print(x > y)   # True (більше)
print(x < y)   # False (менше)
print(x >= y)  # True (більше або рівно)
print(x <= y)  # False (менше або рівно)
```

#### Логічні оператори
```python
x, y = True, False

print(x and y)  # False (обидва мають бути True)
print(x or y)   # True (хоча б один True)
print(not x)    # False (негація)
```

---

### 5. Типові синтаксичні помилки

```python
# ❌ Помилка 1: Неправильний відступ
def bad_function():
print("No indent")  # IndentationError

# ✅ Правильно
def good_function():
    print("With indent")


# ❌ Помилка 2: Забули двокрапку
if x > 5
    print("x greater than 5")  # SyntaxError

# ✅ Правильно
if x > 5:
    print("x greater than 5")


# ❌ Помилка 3: Неправильна назва змінної
2invalid_name = 10  # SyntaxError

# ✅ Правильно
invalid_name_2 = 10


# ❌ Помилка 4: Змішування лапок
text = "Hello' World  # SyntaxError

# ✅ Правильно
text = "Hello World"
text = 'Hello World'
text = """Hello World"""
```

---

## 💡 Приклади

Див. папку `examples/`
