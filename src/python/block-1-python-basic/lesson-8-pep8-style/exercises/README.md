# Вправи - Lesson 8: PEP 8

## Завдання 1: Напишіть PEP 8 код

Створіть файл, що слідує всім правилам PEP 8:

```python
"""
Опис модуля.
"""

# Константи
MAX_SIZE = 100

# Функція
def my_function(x, y):
    """Опис функції."""
    result = x + y
    return result

# Клас
class MyClass:
    """Опис класу."""
    
    def __init__(self):
        self.value = 0

# Головний код
if __name__ == "__main__":
    obj = MyClass()
    print(my_function(5, 3))
```

## Завдання 2: Виправте код

Візьміть неправильний код:

```python
def BadFunction(x,y,z = 1):
    return x+y+z
```

Виправте на PEP 8:

```python
def bad_function(x, y, z=1):
    return x + y + z
```

## Завдання 3: Встановіть інструменти

```bash
pip install black pycodestyle
```

## Завдання 4: Перевірте код

```bash
# Перевірити
pycodestyle your_file.py

# Автоматично форматувати
black your_file.py
```

---

**✅ Коли код слідує PEP 8 - переходьте до Lesson 9**
