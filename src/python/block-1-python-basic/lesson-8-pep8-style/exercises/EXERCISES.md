# Вправи - Lesson 8: PEP 8 and Code Formatting

## 🏋️ Завдання 1: Виправити назви змінних та функцій (EASY)

Створіть файл `exercise-1-fix-naming.py`:

```python
"""
Вправа 1: Виправити назви згідно PEP 8
"""

# ❌ Неправильні назви - виправте!
def CalculateArea(Length, Width):
    """Розрахувати площу."""
    MaxSize = 100
    Area = Length * Width
    return Area


class user_profile:
    """Профіль користувача."""
    
    def __init__(self, UserName, UserAge):
        self.UserName = UserName
        self.UserAge = UserAge


# TODO: Переписати з правильними назвами за PEP 8:
# - Функції: snake_case
# - Класи: PascalCase
# - Константи: UPPER_SNAKE_CASE
# - Змінні: snake_case
```

**Очікуваний результат:**
- `calculate_area(length, width)`
- `UserProfile` клас
- `MAX_SIZE` константа

---

## 🏋️ Завдання 2: Виправити пробіли навколо операторів (EASY)

Створіть файл `exercise-2-fix-spacing.py`:

```python
"""
Вправа 2: Виправити пробільність
"""

# ❌ Неправильне форматування - виправте!
def calculate(x,y,z):
    result=x+y*z
    return result

def process_data(items,multiplier=2,offset=0):
    total=sum(items)*multiplier+offset
    return total

data={'name':'John','age':30,'city':'Kyiv'}
numbers=[1,2,3,4,5]

# TODO: Додати правильні пробіли:
# - Після ком у параметрах
# - Навколо операторів =, +, *, -
# - Після : у словниках
```

**Перевірка:**
```bash
python exercise-2-fix-spacing.py
# Має запуститися без синтаксичних помилок
```

---

## 🏋️ Завдання 3: Впорядкувати імпорти (MEDIUM)

Створіть файл `exercise-3-fix-imports.py`:

```python
"""
Вправа 3: Впорядкувати імпорти за PEP 8
"""

# ❌ Неправильний порядок імпортів
import json
from pathlib import Path
import sys
import os
from datetime import datetime
import re

# TODO: Впорядкувати за групами:
# 1. Стандартна бібліотека (os, sys, json, re)
# 2. Сторонні пакети (якщо є)
# 3. Локальні модулі

# Правильний порядок:
# import os
# import sys
# ...
```

**Правила:**
- Стандартна бібліотека спочатку
- Алфавітний порядок
- Порожній рядок між групами

---

## 🏋️ Завдання 4: Додати docstrings (MEDIUM)

Створіть файл `exercise-4-add-docstrings.py`:

```python
"""
Вправа 4: Додати docstrings за PEP 8
"""

def process_list(items, multiplier):
    # TODO: Додати docstring з описом Args та Returns
    result = [x * multiplier for x in items]
    return result


def filter_active_users(users):
    # TODO: Додати docstring
    return [u for u in users if u.get('active', False)]


class DataProcessor:
    # TODO: Додати docstring класу
    
    def __init__(self, data):
        # TODO: Додати docstring методу
        self.data = data
    
    def process(self):
        # TODO: Додати docstring методу
        return [x * 2 for x in self.data]
```

**Формат docstring:**
```python
"""
Короткий опис в одному рядку.
    
Args:
    param1: Опис параметра
    param2: Опис параметра
    
Returns:
    Опис повернення
"""
```

---

## 🏋️ Завдання 5: Форматування з black (MEDIUM)

Створіть файл `exercise-5-format-with-black.py`:

```python
"""
Вправа 5: Запустити black на цьому файлі
"""

# ❌ Код до форматування
def ugly_function(param1,param2,param3,param4,param5,param6):
    if param1 and param2:result=param3+param4*param5-param6;return result
    else:return 0

def another_ugly_function(data,config={'type':'json','compress':True,'format':'utf-8'}):
    for item in data:
        if item['status']=='active' and item['value']>100:processed=item['value']*2;print(processed)

# TODO: 
# 1. Встановити black: pip install black
# 2. Запустити: black exercise-5-format-with-black.py
# 3. Порівняти код ДО та ПІСЛЯ
```

**Команди:**
```bash
# Перевірка без змін
black --check exercise-5-format-with-black.py

# Форматування
black exercise-5-format-with-black.py

# Перевірка після форматування
black --check exercise-5-format-with-black.py
```

---

## 🏋️ Завдання 6: Виправити помилки flake8 (HARD)

Створіть файл `exercise-6-fix-flake8-errors.py`:

```python
"""
Вправа 6: Виправити всі помилки flake8
"""

import sys
import os
def function():
    x=1+2
    unused=10
    
    
    
    return x

def another_function(a,b,c):
    result=a+b+c;return result

class myClass:
    def method(self,param):
        return param*2

# TODO:
# 1. Встановити flake8: pip install flake8
# 2. Запустити: flake8 exercise-6-fix-flake8-errors.py
# 3. Виправити ВСІ помилки
# 4. Запустити знову: flake8 exercise-6-fix-flake8-errors.py
# 5. Результат має бути: "All checks passed"
```

**Типові помилки:**
- E302: недостатньо порожніх рядків
- E303: забагато порожніх рядків
- E225: без пробілів навколо операторів
- E701: множинні інструкції на одному рядку
- W0612: невикористана змінна

---

## 🏋️ Завдання 7: Повна переробка коду (HARD)

Створіть файл `exercise-7-refactor-code.py`:

```python
"""
Вправа 7: Повна переробка коду за PEP 8
"""

# ❌ ПОГАНИЙ КОД - повністю переробіть!
import json
import sys
def Process(DataList,FilterType='all',SortBy='name'):
    Result=[]
    for Item in DataList:
        if FilterType=='active':
            if Item['status']=='active':Result.append(Item)
        elif FilterType=='inactive':
            if Item['status']!='active':Result.append(Item)
        else:Result.append(Item)
    if SortBy=='name':Result.sort(key=lambda x:x['name'])
    elif SortBy=='age':Result.sort(key=lambda x:x.get('age',0))
    return Result

class user_manager:
    def __init__(self,Users):
        self.Users=Users
    def AddUser(self,Name,Age,Status='active'):
        NewUser={'name':Name,'age':Age,'status':Status}
        self.Users.append(NewUser)
    def GetActiveUsers(self):
        return Process(self.Users,'active','name')

# TODO: Переписати дотримуючись УСІХ правил PEP 8:
# ✅ Правильні назви (snake_case, PascalCase)
# ✅ Пробіли навколо операторів
# ✅ Docstrings для модуля, функцій, класів
# ✅ Порожні рядки (2 між функціями)
# ✅ Довжина рядків (<79 символів)
# ✅ Коментарі (де потрібно)
```

**Критерії оцінювання:**
- [ ] Код запускається без помилок
- [ ] `flake8` не знаходить помилок
- [ ] `pylint` дає рейтинг 9+/10
- [ ] `black` не вносить змін
- [ ] Усі функції/класи мають docstrings

---

## ✅ Перевірка вправ

### Автоматична перевірка:

```bash
# Перевірка форматування
black --check exercise-*.py

# Перевірка стилю
flake8 exercise-*.py

# Детальна перевірка
pylint exercise-*.py --score=yes
```

### Запуск тестів:

```bash
pytest test_exercises.py -v
```

---

**Готові до наступного уроку?** Якщо виконали 5+ вправ та всі тести проходять - так! 🚀

