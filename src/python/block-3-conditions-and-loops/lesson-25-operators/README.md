# Lesson 25: Python Operators

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Використовувати всі типи операторів Python
- ✅ Розуміти пріоритет операторів
- ✅ Використовувати membership та identity оператори
- ✅ Уникати типових помилок з операторами у тестах

---

## 📋 Передумови

Ви вже знаєте:
- Базові типи Python (Block 1-2)
- if/else та логічні оператори (Lesson 18)

---

## 📖 Теорія

### 1. Арифметичні оператори

```python
a, b = 10, 3

a + b    # 13   додавання
a - b    # 7    віднімання
a * b    # 30   множення
a / b    # 3.33 ділення (float)
a // b   # 3    ціле ділення
a % b    # 1    остача
a ** b   # 1000 степінь
```

---

### 2. Оператори порівняння

```python
5 == 5    # True   рівність
5 != 3    # True   нерівність
5 > 3     # True   більше
5 < 10    # True   менше
5 >= 5    # True   більше або дорівнює
5 <= 5    # True   менше або дорівнює
```

**Ланцюжки порівнянь:**

```python
# Pythonic
1 < x < 10     # True якщо x між 1 і 10
a <= b <= c     # True якщо a <= b <= c

# Те саме через and
1 < x and x < 10
```

---

### 3. Логічні оператори

```python
True and True    # True
True and False   # False
True or False    # True
False or False   # False
not True         # False
not False        # True
```

**Пріоритет:** `not` > `and` > `or`

```python
# Це:
a or b and c
# Означає:
a or (b and c)
```

---

### 4. Membership оператори (in, not in)

```python
# Для колекцій
3 in [1, 2, 3]          # True
"key" in {"key": "val"} # True (перевіряє ключі)
"a" not in "hello"      # True

# Для рядків — шукає підрядок
"test" in "pytest"       # True
"abc" in "abcdef"        # True
```

---

### 5. Identity оператори (is, is not)

```python
# is перевіряє ідентичність об'єкта (той самий об'єкт у пам'яті)
a = [1, 2, 3]
b = a
c = [1, 2, 3]

a is b      # True — той самий об'єкт
a is c      # False — різні об'єкти (хоч значення рівні)
a == c      # True — значення рівні

# Головне використання — перевірка None
value = None
value is None      # ✅ правильно
value == None      # ⚠️ працює, але не pythonic
```

---

### 6. Присвоєння з операцією

```python
x = 10
x += 5    # x = x + 5  → 15
x -= 3    # x = x - 3  → 12
x *= 2    # x = x * 2  → 24
x //= 5   # x = x // 5 → 4
x **= 2   # x = x ** 2 → 16
```

---

### 7. Зведена таблиця

| Категорія | Оператори | Приклад |
|-----------|-----------|---------|
| Арифметичні | `+` `-` `*` `/` `//` `%` `**` | `10 // 3 → 3` |
| Порівняння | `==` `!=` `<` `>` `<=` `>=` | `5 >= 5 → True` |
| Логічні | `and` `or` `not` | `True and False → False` |
| Membership | `in` `not in` | `3 in [1,2,3] → True` |
| Identity | `is` `is not` | `x is None` |
| Присвоєння | `+=` `-=` `*=` `//=` | `x += 5` |

---

## ⚠️ Типові помилки

### `==` замість `is` для None

```python
# ⚠️ Працює, але не pythonic
if value == None:
    pass

# ✅ Правильно
if value is None:
    pass
```

### `is` замість `==` для значень

```python
# ❌ Може не працювати для великих чисел
a = 1000
b = 1000
a is b    # може бути False!

# ✅ Для порівняння значень — завжди ==
a == b    # True
```

### Пріоритет and/or без дужок

```python
# ❌ Неочевидний результат
if admin or moderator and active:
    pass  # == admin or (moderator and active)

# ✅ Явні дужки
if (admin or moderator) and active:
    pass
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Вітаємо! Ви завершили Block 3: Conditions and Loops.**