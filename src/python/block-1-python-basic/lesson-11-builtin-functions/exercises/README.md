# Вправи - Lesson 12: Built-in functions

## Завдання 1: print() функція

```python
# Вивести текст різними способами
print("Hello, World!")

print("A", "B", "C")  # З простором

print("A", "B", "C", sep="-")  # З розділювачем

print("First", end=" ")
print("Second")  # Без нового рядка

# Форматування
name = "Alice"
age = 25
print(f"{name} is {age} years old")
```

## Завдання 2: input() функція

```python
# Програма для збору інформації
name = input("Enter your name: ")
age = input("Enter your age: ")

# Конвертація
age_int = int(age)

print(f"Hello {name}, you are {age_int} years old")
```

## Завдання 3: dir() функція

```python
# Дослідити методи списку
my_list = [1, 2, 3]

# Вивести всі методи
all_methods = dir(my_list)
print(f"Total methods: {len(all_methods)}")

# Лише публічні методи
public_methods = [m for m in dir(my_list) if not m.startswith('_')]
print("Public methods:", public_methods)
```

## Завдання 4: id() функція

```python
# Порівняти ID об'єктів
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")

print(f"a is b: {a is b}")  # True
print(f"a is c: {a is c}")  # False
```

## Завдання 5: Комплексна програма

```python
# Програма розрахунку BMI
print("=== BMI Calculator ===")

name = input("Name: ")
height = float(input("Height (m): "))
weight = float(input("Weight (kg): "))

bmi = weight / (height ** 2)

print(f"Hello {name}!")
print(f"Your BMI: {bmi:.2f}")
```

---

**✅ Коли вбудовані функції працюють - переходьте до Lesson 13**
