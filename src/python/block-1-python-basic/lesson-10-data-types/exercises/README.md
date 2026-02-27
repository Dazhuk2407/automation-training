# Вправи - Lesson 11: Data types

## Завдання 1: Створіть всі типи даних

```python
# Напишіть змінні усіх 5 типів:
my_string = ...
my_int = ...
my_float = ...
my_bool = ...
my_none = ...

# Перевірте типи
for var in [my_string, my_int, my_float, my_bool, my_none]:
    print(type(var))
```

## Завдання 2: Перевірте типи

```python
# Використайте isinstance()
print(isinstance(25, int))
print(isinstance("hello", str))
print(isinstance(3.14, float))
print(isinstance(True, bool))
print(isinstance(None, type(None)))
```

## Завдання 3: Конвертуйте типи

```python
# String в int
string_num = "123"
num = int(string_num)
print(f"Converted: {num}, Type: {type(num)}")

# Int в string
number = 42
string = str(number)
print(f"String: {string}, Type: {type(string)}")

# String в float
float_str = "3.14"
float_num = float(float_str)
print(f"Float: {float_num}")

# Number в bool
print(bool(1))    # True
print(bool(0))    # False
```

## Завдання 4: Знайдіть помилки

```python
# ❌ Це викликає помилку - чому?
x = int("abc")

# Виправте конвертацію
try:
    x = int("abc")
except ValueError:
    print("Cannot convert to int")
```

## Завдання 5: Напишіть функцію

```python
def process_data(value):
    """Конвертувати та вивести тип."""
    # Перетворіть value в різні типи
    # Виведіть які вийшли типи
    pass
```

---

**✅ Коли конвертація типів працює - переходьте до Lesson 12**
