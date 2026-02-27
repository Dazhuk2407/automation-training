# Lesson 11: Built-in Functions

## 🎯 Learning Outcomes

- ✅ Використовувати 15+ вбудованих функцій Python
- ✅ Розуміти print(), input(), len(), range(), type()
- ✅ Працювати з математичними функціями (sum, min, max, abs, round)
- ✅ Використовувати sorted(), enumerate(), zip()
- ✅ Розуміти isinstance(), help(), dir()

---

## 📖 Теорія

Python має 69 вбудованих функцій. Ми вивчимо 15 найважливіших.

### 1. Вивід та Введення

#### print() - вивід на екран

```python
# Простий вивід
print("Hello, World!")

# Кілька аргументів
print("Hello", "World", "!")  # Hello World !

# Розділювач sep
print("A", "B", "C", sep="-")  # A-B-C

# Кінцевий символ end
print("Hello", end=" ")
print("World")  # Hello World (в одному рядку)

# Форматування
name = "Alice"
age = 25
print(f"{name} is {age} years old")
```

#### input() - введення з клавіатури

```python
# Читати рядок
name = input("Enter your name: ")
print(f"Hello, {name}!")

# input() ЗАВЖДИ повертає string
age_str = input("Enter age: ")
age = int(age_str)  # Конвертувати в число
```

---

### 2. Інформація про Об'єкти

#### type() - тип об'єкта

```python
print(type(42))         # <class 'int'>
print(type("hello"))    # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
```

#### isinstance() - перевірка типу

```python
isinstance(42, int)        # True
isinstance("hello", str)   # True
isinstance([1, 2], list)   # True

# Перевірка кількох типів
isinstance(42, (int, float))  # True
```

#### dir() - список атрибутів

```python
# Показати всі методи об'єкта
lst = [1, 2, 3]
print(dir(lst))  # [..., 'append', 'clear', 'copy', ...]

# Фільтрувати приватні
public = [m for m in dir(lst) if not m.startswith('_')]
```

#### id() - ідентифікатор об'єкта

```python
x = [1, 2, 3]
print(id(x))  # 140234... (унікальний ID в пам'яті)

# Перевірка чи два об'єкти однакові
a = [1, 2]
b = a
c = [1, 2]

print(id(a) == id(b))  # True (один об'єкт)
print(id(a) == id(c))  # False (різні об'єкти)
```

#### help() - документація

```python
help(len)     # Показує документацію функції
help(list)    # Показує документацію класу
help(str.upper)  # Показує документацію методу
```

---

### 3. Робота з Колекціями

#### len() - довжина

```python
len("hello")        # 5
len([1, 2, 3])      # 3
len({"a": 1})       # 1
len(range(10))      # 10
```

#### range() - послідовність чисел

```python
# range(stop)
list(range(5))           # [0, 1, 2, 3, 4]

# range(start, stop)
list(range(2, 7))        # [2, 3, 4, 5, 6]

# range(start, stop, step)
list(range(0, 10, 2))    # [0, 2, 4, 6, 8]
list(range(10, 0, -1))   # [10, 9, 8, ..., 1]

# Використання в циклі
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

#### enumerate() - індекс + значення

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Початковий індекс
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry
```

#### zip() - об'єднати послідовності

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old

# Створити словник
dict(zip(names, ages))  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

---

### 4. Математичні Функції

#### sum() - сума

```python
sum([1, 2, 3, 4, 5])        # 15
sum([1, 2, 3], 10)          # 16 (початкове значення 10)
sum(range(1, 101))          # 5050 (сума від 1 до 100)
```

#### min() - мінімум

```python
min([5, 2, 9, 1, 7])        # 1
min(5, 2, 9, 1, 7)          # 1 (аргументи)
min("hello")                # 'e' (мінімальний символ)

# З ключем
min(['apple', 'pie', 'zoo'], key=len)  # 'pie'
```

#### max() - максимум

```python
max([5, 2, 9, 1, 7])        # 9
max(5, 2, 9, 1, 7)          # 9
max("hello")                # 'o'

# З ключем
max(['apple', 'pie', 'zoo'], key=len)  # 'apple'
```

#### abs() - абсолютне значення

```python
abs(-10)      # 10
abs(10)       # 10
abs(-3.14)    # 3.14
```

#### round() - округлення

```python
round(3.14159)          # 3
round(3.14159, 2)       # 3.14 (2 знаки після коми)
round(3.5)              # 4 (до найближчого парного)
round(2.5)              # 2 (до найближчого парного)
```

#### pow() - піднесення до степеня

```python
pow(2, 3)       # 8 (2³)
pow(2, 3, 5)    # 3 ((2³) % 5)
2 ** 3          # 8 (альтернативний синтаксис)
```

---

### 5. Робота зі Списками та Рядками

#### sorted() - сортування

```python
# Список
sorted([3, 1, 4, 1, 5])     # [1, 1, 3, 4, 5]
sorted([3, 1, 4], reverse=True)  # [4, 3, 1]

# Рядок
sorted("hello")             # ['e', 'h', 'l', 'l', 'o']

# З ключем
words = ['apple', 'pie', 'zoo', 'a']
sorted(words, key=len)      # ['a', 'pie', 'zoo', 'apple']

# Різниця між sorted() та .sort()
lst = [3, 1, 2]
sorted(lst)    # Повертає новий список [1, 2, 3]
lst.sort()     # Змінює сам список (in-place)
```

#### reversed() - реверс

```python
list(reversed([1, 2, 3]))       # [3, 2, 1]
list(reversed("hello"))         # ['o', 'l', 'l', 'e', 'h']

# Використання в циклі
for item in reversed([1, 2, 3]):
    print(item)  # 3, 2, 1
```

#### all() - всі True?

```python
all([True, True, True])         # True
all([True, False, True])        # False
all([1, 2, 3])                  # True (всі truthy)
all([1, 0, 3])                  # False (0 є falsy)

# Перевірка умови для всіх елементів
numbers = [2, 4, 6, 8]
all(n % 2 == 0 for n in numbers)  # True (всі парні)
```

#### any() - хоч один True?

```python
any([False, False, True])       # True
any([False, False, False])      # False
any([0, 0, 1])                  # True

# Перевірка умови для будь-якого елемента
numbers = [1, 3, 5, 8]
any(n % 2 == 0 for n in numbers)  # True (є парні)
```

---

### 6. Таблиця Функцій

| Функція | Опис | Приклад |
|---------|------|---------|
| `print()` | Вивід | `print("Hello")` |
| `input()` | Введення | `name = input("Name: ")` |
| `len()` | Довжина | `len([1, 2, 3])` → 3 |
| `type()` | Тип | `type(42)` → int |
| `isinstance()` | Перевірка типу | `isinstance(42, int)` → True |
| `range()` | Послідовність | `range(5)` → 0,1,2,3,4 |
| `enumerate()` | Індекс + значення | `enumerate(['a','b'])` |
| `zip()` | Об'єднати | `zip([1,2], ['a','b'])` |
| `sum()` | Сума | `sum([1,2,3])` → 6 |
| `min()` | Мінімум | `min([1,2,3])` → 1 |
| `max()` | Максимум | `max([1,2,3])` → 3 |
| `abs()` | Модуль | `abs(-10)` → 10 |
| `round()` | Округлення | `round(3.14, 1)` → 3.1 |
| `sorted()` | Сортування | `sorted([3,1,2])` → [1,2,3] |
| `all()` | Всі True? | `all([1,1,1])` → True |
| `any()` | Хоч один True? | `any([0,0,1])` → True |

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`
methods = [m for m in dir(lst) if not m.startswith('_')]
print(methods)
```

## id() - Ідентифікатор

```python
# Отримати ID об'єкта
x = 42
print(id(x))  # 140234... (унікальний ID)

# Порівняти ID
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a) == id(b))  # False (різні об'єкти)
```

## Приклади

Див. папку `examples/`

## Вправи

Див. папку `exercises/`
