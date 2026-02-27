# Приклади - Lesson 11: Data types

## Створення змінних всіх типів

```python
"""
Приклади всіх основних типів даних Python.
"""

# 1. String - текст
name = "Alice"
greeting = "Hello, World!"
multiline = """This is
a multiline
string"""

print(f"String: {name}, Type: {type(name)}")


# 2. Integer - ціле число
age = 25
count = -10
zero = 0

print(f"Integer: {age}, Type: {type(age)}")


# 3. Float - число з комою
price = 19.99
temperature = -5.5
pi = 3.14159

print(f"Float: {price}, Type: {type(price)}")


# 4. Boolean - істина/неправда
is_active = True
is_empty = False

print(f"Boolean: {is_active}, Type: {type(is_active)}")


# 5. None - відсутність значення
result = None

print(f"None: {result}, Type: {type(result)}")
```

## Перевірка та конвертація типів

```python
# Перевірка типу
print(isinstance(25, int))          # True
print(isinstance("hello", str))     # True
print(type(3.14) == float)          # True


# Конвертація типів
string_number = "42"
number = int(string_number)
print(f"Converted: {number}, Type: {type(number)}")


# String в float
string_float = "3.14"
float_num = float(string_float)
print(f"Float: {float_num}")


# Number в string
num = 42
string_num = str(num)
print(f"String: {string_num}, Type: {type(string_num)}")


# У boolean
print(bool(1))         # True
print(bool(0))         # False
print(bool("text"))    # True
print(bool(""))        # False
```
