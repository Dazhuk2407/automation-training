# Lesson 7: Basic Python Syntax

## 🎯 Learning Outcomes (Що ви вмітимете після уроку)

- ✅ Розуміти структуру Python файлу
- ✅ Писати та використовувати коментарі
- ✅ Оголошувати змінні та присвоювати значення
- ✅ Використовувати базові оператори (арифметичні, порівняння, логічні)
- ✅ Розпізнавати типові синтаксичні помилки

---

## 📚 Корисні посилання

- [Python Tutorial - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)

---

## 📖 Теорія

### 1. Структура Python файлу

**Стандартний порядок елементів у Python модулі:**

1. **Docstring модуля** - опис файлу
2. **Imports** - імпорти бібліотек
3. **Constants** - константи (UPPER_CASE)
4. **Classes** - класи
5. **Functions** - функції
6. **Main block** - головний код (`if __name__ == "__main__":`)

```python
"""
Docstring - опис модуля.
Це ЗАВЖДИ перший рядок файлу.
"""

# === IMPORTS ===
import sys
from datetime import datetime

# === CONSTANTS ===
MAX_ATTEMPTS = 3
DEFAULT_NAME = "User"

# === CLASSES ===
class Person:
    """Клас для представлення людини."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# === FUNCTIONS ===
def greet(name: str) -> str:
    """Функція для привітання."""
    return f"Hello, {name}!"


def calculate_age(birth_year: int) -> int:
    """Обчислити вік на основі року народження."""
    current_year = datetime.now().year
    return current_year - birth_year

# === MAIN ===
if __name__ == "__main__":
    # Головний код виконується тільки при прямому запуску
    person = Person("Alice", 25)
    print(greet(person.name))
    print(f"Age: {calculate_age(1998)}")
```

**Чому саме такий порядок?**
- 📖 **Docstring** на початку - щоб `help(module)` працював
- 📦 **Imports** вгорі - легко бачити залежності
- 🔢 **Constants** перед класами - використовуються всюди
- 🏗️ **Classes** перед функціями - більш високорівневі абстракції
- ⚙️ **Functions** після класів - часто використовують класи
- 🚀 **Main** в кінці - викликає все вище написане

---

### 2. Коментарі та Docstrings

#### Коментарі (#)
```python
# Однорядковий коментар - починається з #
# Ігнорується інтерпретатором Python

x = 10  # Інлайн коментар - після коду

# Багаторядковий коментар можна зробити так:
# Перший рядок коментаря
# Другий рядок коментаря
# Третій рядок коментаря
```

#### Docstrings (""")
```python
"""
Docstring модуля.
Це НЕ коментар - це string literal!
Використовується для документування коду.
"""

def calculate(x, y):
    """
    Це docstring функції.
    Доступний через help(calculate) або calculate.__doc__
    
    Args:
        x (int): Перше число
        y (int): Друге число
        
    Returns:
        int: Сума чисел
        
    Examples:
        >>> calculate(2, 3)
        5
    """
    result = x + y  # Це коментар
    return result


class Calculator:
    """
    Docstring класу.
    Описує призначення класу.
    """
    pass
```

**Різниця між коментарями та docstrings:**
- `#` коментарі - ігноруються інтерпретатором, для пояснень
- `"""` docstrings - зберігаються в `__doc__`, для документації

---

### 3. Змінні та присвоювання

```python
# Оголошення змінних
name = "Alice"           # string
age = 25                # int
height = 5.7            # float
is_student = True       # bool
result = None           # NoneType

# Множинне присвоювання
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

#### Оператори присвоювання
```python
x = 10

x += 5   # x = x + 5  →  x = 15
x -= 3   # x = x - 3  →  x = 12
x *= 2   # x = x * 2  →  x = 24
x /= 4   # x = x / 4  →  x = 6.0
x //= 2  # x = x // 2 →  x = 3.0
x %= 2   # x = x % 2  →  x = 1.0
x **= 3  # x = x ** 3 →  x = 1.0
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

# Практичний приклад
age = 25
has_license = True

can_drive = age >= 18 and has_license  # True
print(can_drive)
```

#### Оператори належності
```python
# in, not in - перевірка наявності елемента
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # True
print("orange" in fruits)     # False
print("orange" not in fruits) # True

text = "Hello, World!"
print("Hello" in text)        # True
```

#### Оператори ідентичності
```python
# is, is not - перевірка ідентичності об'єктів
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)   # True (однакові значення)
print(x is y)   # False (різні об'єкти в пам'яті)
print(x is z)   # True (той самий об'єкт)

# Особливий випадок з None
result = None
print(result is None)      # True ✅ (правильно)
print(result == None)      # True ❌ (працює, але не рекомендується)
```

**Пріоритет операторів (від вищого до нижчого):**
1. `**` (піднесення в степень)
2. `*`, `/`, `//`, `%` (множення, ділення)
3. `+`, `-` (додавання, віднімання)
4. `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` (порівняння)
5. `not` (логічне НІ)
6. `and` (логічне І)
7. `or` (логічне АБО)

```python
# Приклад пріоритету
result = 2 + 3 * 4  # 14, не 20 (спочатку множення)
result = (2 + 3) * 4  # 20 (дужки змінюють пріоритет)
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
x = 10  # Оголошуємо змінну
if x > 5
    print("x greater than 5")  # SyntaxError: invalid syntax

# ✅ Правильно
if x > 5:
    print("x greater than 5")


# ❌ Помилка 3: Неправильна назва змінної
2invalid_name = 10  # SyntaxError: invalid syntax

# ✅ Правильно
invalid_name_2 = 10


# ❌ Помилка 4: Змішування лапок
text = "Hello' World  # SyntaxError: unterminated string literal

# ✅ Правильно
text = "Hello World"
text = 'Hello World'
text = """Hello World"""


# ❌ Помилка 5: Використання невизначеної змінної
print(undefined_variable)  # NameError: name 'undefined_variable' is not defined

# ✅ Правильно
defined_variable = "Hello"
print(defined_variable)


# ❌ Помилка 6: Ділення на нуль
result = 10 / 0  # ZeroDivisionError: division by zero

# ✅ Правильно (з перевіркою)
divisor = 0
if divisor != 0:
    result = 10 / divisor
else:
    print("Cannot divide by zero!")
```

---

## 💡 Приклади

Див. папку `examples/`
