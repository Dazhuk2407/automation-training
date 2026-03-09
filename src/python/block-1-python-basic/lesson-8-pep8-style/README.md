# Lesson 8: PEP 8 and Code Formatting

## 🎯 Результати навчання

- ✅ Розуміти правила PEP 8
- ✅ Писати код в стилі PEP 8
- ✅ Використовувати інструменти форматування (`black`, `isort`, `flake8`, `pylint`)
- ✅ Автоматизувати перевірку стилю

---

## 📖 Теорія: PEP 8

### 1. Що таке PEP 8?

PEP 8 (Python Enhancement Proposal 8) - офіційний посібник стилю для Python.

```python
# ✅ ПРАВИЛЬНО - PEP 8 compliant
def calculate_sum(numbers):
    """Обчислити суму списку."""
    total = sum(numbers)
    return total

# ❌ НЕПРАВИЛЬНО - не слідує PEP 8
def CalculateSum(numbers):
    total=sum(numbers)
    return total
```

### 2. Правила відступів

```python
# ✅ 4 пробіли на рівень (не Tab!)
def function():
    if condition:
        for item in items:
            process(item)

# ❌ Неправильно - мішані Tab та пробіли
def function():
	if condition:
	  process()
```

### 3. Довжина рядків

```python
# ✅ Максимум 79 символів для коду
# Максимум 72 символи для коментарів
def long_function_name(
    variable_one,
    variable_two,
    variable_three
):
    """Функція з довгим іменем."""
    pass

# ❌ Один довгий рядок (>79 символів)
def long_function_name(variable_one, variable_two, variable_three):
    pass
```

### 4. Пробіли навколо операторів

```python
# ✅ ПРАВИЛЬНО - пробіли навколо операторів
x = y + 1
result = a * b + c
dict_arg = {'key': 'value'}
func(arg1, arg2)

# ❌ НЕПРАВИЛЬНО - без пробілів
x=y+1
result=a*b+c
dict_arg={'key':'value'}
func( arg1 , arg2 )
```

### 5. Назвування

```python
# ✅ ПРАВИЛЬНО
def calculate_area(length, width):
    """Розрахувати площу."""
    MAX_SIZE = 100
    CONSTANT_VALUE = 5
    local_variable = length * width
    return local_variable

class DataProcessor:
    """Процесор даних."""
    pass

# ❌ НЕПРАВИЛЬНО
def CalculateArea(Length, Width):
    maxSize = 100
    local_variable_name_with_underscores = 5
    return Length * Width

class data_processor:
    pass
```

### 6. Імпорти

```python
# ✅ ПРАВИЛЬНО - впорядковані та розділені
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from mymodule import function1, function2

# ❌ НЕПРАВИЛЬНО - невпорядковані
import pandas as pd
import os
from pathlib import Path
import sys
import numpy as np
from mymodule import function1
```

### 7. Коментарі та Docstrings

```python
# ✅ ПРАВИЛЬНО
def function():
    """
    Корисний docstring з описом.
    
    Args:
        param1: Опис параметра
        
    Returns:
        Опис повернення
    """
    # Коментар пояснює складну логіку
    x = calculate()
    return x

# ❌ НЕПРАВИЛЬНО
def function():
    #No space after hash
    x = calculate() # inline comment with no space
    return x
```

### 8. Порожні рядки

```python
# ✅ ПРАВИЛЬНО
import sys

CONSTANT = 10


def function_one():
    """Перша функція."""
    pass


def function_two():
    """Друга функція."""
    pass


class MyClass:
    """Мій клас."""
    
    def method_one(self):
        pass
    
    def method_two(self):
        pass

# ❌ НЕПРАВИЛЬНО - забагато/замало порожніх рядків
import sys
CONSTANT = 10
def function_one():
    pass
def function_two():
    pass
class MyClass:
    def method_one(self):
        pass
    def method_two(self):
        pass
```

---

## 🛠️ Інструменти форматування

### 1. Black - автоматичний форматор

```bash
# Встановлення
pip install black

# Форматування файлу
black myfile.py

# Форматування всієї папки
black .

# Перевірка без змін
black --check myfile.py

# Black використовує стандартну довжину рядка 88
black --line-length 88 myfile.py
```

**Результат:**
```python
# Before
x=1+2*3
func(arg1,arg2,arg3)

# After (black format)
x = 1 + 2 * 3
func(arg1, arg2, arg3)
```


### 2. isort - сортування імпортів

`isort` автоматично впорядковує імпорти відповідно до PEP 8.

```bash
# Встановлення
pip install isort

# Сортування імпортів у файлі
isort myfile.py

# Сортування імпортів у всьому проєкті
isort .

# Перевірка без змін
isort --check-only .
```

**Результат:**
```python
# Before
import pandas as pd
import os
from pathlib import Path
import sys

# After
import os
import sys
from pathlib import Path

import pandas as pd
```

### 3. Flake8 - лінтер (перевіряє стиль)

```bash
# Встановлення
pip install flake8

# Перевірка файлу
flake8 myfile.py

# Перевірка всієї папки
flake8 .

# Вивід з номерами рядків
flake8 myfile.py --statistics
```

**Результат:**
```
myfile.py:1:1: E302 expected 2 blank lines, found 1
myfile.py:5:9: W293 blank line contains whitespace
myfile.py:10:1: E303 too many blank lines (3)
```

### 4. Pylint - детальна перевірка якості

```bash
# Встановлення
pip install pylint

# Перевірка файлу
pylint myfile.py

# Визначення оцінки якості
pylint myfile.py --score=yes

# Вивід у форматі JSON
pylint myfile.py --output-format=json
```

**Результат:**
```
Your code has been rated at 9.50/10 (оцінка якості коду)
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`
