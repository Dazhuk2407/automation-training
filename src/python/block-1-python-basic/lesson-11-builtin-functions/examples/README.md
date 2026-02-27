# Приклади - Lesson 12: Built-in functions

## print() функція

```python
"""
Приклади print() функції.
"""

# Простий вивід
print("Hello, World!")

# Кілька аргументів
print("Python", "is", "awesome")  # Python is awesome

# Розділювач sep
print("A", "B", "C", sep=" - ")   # A - B - C
print("A", "B", "C", sep="")      # ABC

# Кінцевий символ end
print("First", end=" ")
print("Second")  # First Second

print("No newline", end="!!!\n")  # No newline!!!


# Форматування
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")
```

## input() функція

```python
# Читати введення
name = input("What is your name? ")
print(f"Hello, {name}!")

# input() повертає string
age_str = input("Enter your age: ")
age = int(age_str)
print(f"You are {age} years old")

# Конвертація на льоту
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")
```

## dir() функція

```python
# Показати методи списку
my_list = [1, 2, 3]
print(dir(my_list))

# Фільтрувати приватні методи
methods = [m for m in dir(my_list) if not m.startswith('_')]
print(methods)  # append, clear, copy, count, extend, ...

# Методи рядка
my_string = "hello"
print(dir(my_string))
```

## id() функція

```python
# Отримати ID
x = 42
print(f"ID of x: {id(x)}")

# Порівняння ID
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"ID of a: {id(a)}")
print(f"ID of b: {id(b)}")
print(f"ID of c: {id(c)}")

print(f"a == b: {a == b}")    # True (значення одинакові)
print(f"a is b: {a is b}")    # True (один і той же об'єкт)
print(f"a == c: {a == c}")    # True (значення одинакові)
print(f"a is c: {a is c}")    # False (різні об'єкти)
```
