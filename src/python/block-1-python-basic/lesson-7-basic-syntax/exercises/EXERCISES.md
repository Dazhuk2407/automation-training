# Вправи - Lesson 7: Basic Python Syntax

## 🏋️ Завдання 1: Структурований файл (EASY)

Створіть файл `exercise_1_structure.py` з такою структурою:

```python
"""
Опис модуля - що робить цей скрипт?
"""

# Константи
APP_NAME = "My App"

# Функція
def calculate(x, y):
    """Додати два числа."""
    return x + y

# Головний код
if __name__ == "__main__":
    result = calculate(5, 3)
    print(f"{APP_NAME}: {result}")
```

**Перевірка:**
```bash
python exercise_1_structure.py
# Output: My App: 8
```

---

## 🏋️ Завдання 2: Коментарі та Docstrings (EASY)

Створіть файл `exercise_2_comments.py`:

```python
# TODO: Додайте docstring модуля
# TODO: Напишіть функцію з docstring

def greet(name):
    # TODO: Додайте docstring з Args та Returns
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Привітайте користувача
    print(greet("Alice"))
```

**Вимоги:**
- Модуль має docstring
- Функція має docstring з Args та Returns
- Коментарі пояснюють код

---

## 🏋️ Завдання 3: Змінні всіх типів (EASY)

Створіть файл `exercise_3_variables.py`:

```python
"""Демонстрація всіх типів змінних."""

# TODO: Оголосіть змінні кожного типу
# string, int, float, bool, None

# TODO: Виведіть змінні та їхні типи в форматі:
# name: Alice, type: <class 'str'>

```

**Вимоги:**
- 5 змінних різних типів
- Вивід у форматі: `variable: value, type: type`

**Тестування:**
```bash
python exercise_3_variables.py
```

---

## 🏋️ Завдання 4: Множинне присвоювання (MEDIUM)

Створіть файл `exercise_4_multiple_assignment.py`:

```python
"""Вправа на множинне присвоювання та swap."""

# TODO: Присвойте три змінні одночасно
# x, y, z = ...

# TODO: Виведіть їхні значення

# TODO: Замініть значення x та y (swap)

# TODO: Виведіть нові значення
```

**Вимоги:**
- Присвоєння: x, y, z = 10, 20, 30
- Swap: a, b = b, a
- Вивід до та після

**Очікуваний результат:**
```
Before swap: x=10, y=20, z=30
After swap: x=20, y=10, z=30
```

---

## 🏋️ Завдання 5: Оператори (MEDIUM)

Створіть файл `exercise_5_operators.py`:

```python
"""Практика всіх операторів."""

x, y = 10, 3

# TODO: Виведіть результати арифметичних операцій
# +, -, *, /, //, %, **

# TODO: Виведіть результати операцій порівняння
# ==, !=, >, <, >=, <=

# TODO: Виведіть результати логічних операцій
# Встановіть a=True, b=False
# Виведіть: a and b, a or b, not a
```

**Формат виводу:**
```
=== ARITHMETIC ===
10 + 3 = 13
10 - 3 = 7
...
=== COMPARISON ===
10 == 3 = False
...
=== LOGICAL ===
True and False = False
...
```

---

## 🏋️ Завдання 6: Виправлення синтаксичних помилок (MEDIUM)

Створіть файл `exercise_6_syntax_errors.py` та виправте помилки:

```python
"""Файл з синтаксичними помилками - виправте їх!"""

# ❌ Помилка 1: Неправильний відступ
def bad_function()
print("No indent")

# ❌ Помилка 2: Забув двокрапку
if x > 5
    print("Greater")

# ❌ Помилка 3: Неправильна назва змінної
2invalid = 10

# ❌ Помилка 4: Змішування лапок
text = "Hello' World

# TODO: Виправте всі помилки та запустіть
```

**Перевірка:**
```bash
python exercise_6_syntax_errors.py
# Має запуститися без помилок
```

---

## 🏋️ Завдання 7: Комплексна програма (HARD)

Створіть файл `exercise_7_complete_program.py` з:

```python
"""
Програма для розрахунку параметрів прямокутника.
Користувач вводить довжину та ширину.
Програма розраховує площу, периметр та діагональ.
"""

import math

# TODO: Напишіть функцію calculate_rectangle_area(length, width)
def calculate_rectangle_area(length, width):
    """Розрахувати площу прямокутника."""
    # TODO: Реалізація

# TODO: Напишіть функцію calculate_rectangle_perimeter(length, width)
def calculate_rectangle_perimeter(length, width):
    """Розрахувати периметр прямокутника."""
    # TODO: Реалізація

# TODO: Напишіть функцію calculate_rectangle_diagonal(length, width)
#  Для діагоналі використайте `math.sqrt(length**2 + width**2)`
def calculate_rectangle_diagonal(length, width):
    """Розрахувати діагональ прямокутника за формулою: sqrt(a² + b²)"""
    # TODO: Реалізація

if __name__ == "__main__":
    # Введення даних
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    
    # TODO: Розрахунки та вивід
```

**Очікуваний результат:**
```
Enter length: 5
Enter width: 3
Area: 15.0
Perimeter: 16.0
Diagonal: 5.83
```

---

## ✅ Критерії оцінювання

- ✅ Код запускається без помилок
- ✅ Структура файлу правильна
- ✅ Змінні мають описові імена
- ✅ Коментарі пояснюють складні частини
- ✅ Результати відповідають очікуванням

---
