# Lesson 14: Mutable vs Immutable

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розрізняти mutable та immutable типи
- ✅ Розуміти наслідки мутабельності при передачі в функції
- ✅ Уникати побічних ефектів (side effects) у тестах
- ✅ Розуміти проблему mutable default arguments
- ✅ Обирати правильний тип для конкретної задачі

---

## 📋 Передумови

Ви вже знаєте:
- list, tuple, dict, set (Lesson 9-13)
- Як працюють змінні в Python

---

## 📖 Теорія

### 1. Класифікація типів

| Mutable (змінюваний) | Immutable (незмінюваний) |
|----------------------|------------------------|
| `list` | `int` |
| `dict` | `float` |
| `set` | `str` |
| | `tuple` |
| | `bool` |
| | `frozenset` |

**Mutable** — можна змінити вміст об'єкта після створення.
**Immutable** — для "зміни" створюється новий об'єкт.

---

### 2. Як це працює

```python
# Immutable — "зміна" створює новий об'єкт
x = 10
y = x
x = 20
# y все ще 10 — y вказує на старий об'єкт

name = "Alice"
upper_name = name.upper()
# name все ще "Alice" — upper() створив новий рядок

# Mutable — зміна впливає на всіх, хто посилається
items = [1, 2, 3]
other = items      # other і items — це ТОЙ САМИЙ список
items.append(4)
# other тепер [1, 2, 3, 4] — сюрприз!
```

---

### 3. Проблема: побічні ефекти (side effects)

```python
def add_admin_role(user):
    """❌ Змінює оригінальний словник!"""
    user["role"] = "admin"
    return user

original = {"name": "Alice", "role": "user"}
result = add_admin_role(original)

# original тепер {"name": "Alice", "role": "admin"}
# Оригінал змінився! Це side effect.
```

**Чому це небезпечно в тестах:**

```python
USER = {"name": "Alice", "role": "user"}

def test_first():
    """Цей тест змінює USER."""
    USER["role"] = "admin"
    assert USER["role"] == "admin"

def test_second():
    """❌ Цей тест отримає зіпсований USER!"""
    assert USER["role"] == "user"  # FAIL! role вже "admin"
```

---

### 4. Рішення: не мутувати, створювати нове

```python
def add_admin_role(user):
    """✅ Створює новий словник, не змінює оригінал."""
    return {**user, "role": "admin"}

original = {"name": "Alice", "role": "user"}
result = add_admin_role(original)

# original все ще {"name": "Alice", "role": "user"} ✅
# result = {"name": "Alice", "role": "admin"}
```

Для списків:

```python
# ❌ Змінює оригінал
def add_item(items, item):
    items.append(item)
    return items

# ✅ Створює новий список
def add_item(items, item):
    return [*items, item]
```

---

### 5. Проблема: mutable default arguments

```python
# ❌ НЕБЕЗПЕЧНО — default list спільний між викликами
def add_user(name, users=[]):
    users.append(name)
    return users

result1 = add_user("Alice")  # ["Alice"]
result2 = add_user("Bob")    # ["Alice", "Bob"] — СЮРПРИЗ!

# ✅ ПРАВИЛЬНО — None як default
def add_user(name, users=None):
    if users is None:
        users = []
    users.append(name)
    return users
```

Це одна з найвідоміших пасток Python.

---

### 6. У тестах: кожен тест — свіжі дані

```python
import pytest


def get_fresh_user():
    """Фабрика — кожен виклик створює новий словник."""
    return {"name": "Alice", "role": "user", "active": True}


def test_modify_role():
    user = get_fresh_user()
    user["role"] = "admin"
    assert user["role"] == "admin"


def test_original_intact():
    user = get_fresh_user()
    assert user["role"] == "user"  # ✅ свіжі дані — все ок
```

---

### 7. Таблиця рішень

| Задача | Mutable | Immutable |
|--------|---------|-----------|
| Тестові дані що не змінюються | | tuple, frozenset |
| Конфіг | | tuple/namedtuple |
| Список що росте | list | |
| Ключ словника | | str, int, tuple |
| Передача у функцію без side effects | | створити копію |

---

## ⚠️ Типові помилки

### Спільна змінна між тестами

```python
# ❌ Всі тести працюють з одним списком
ITEMS = [1, 2, 3]

def test_a():
    ITEMS.append(4)  # мутує спільну змінну

def test_b():
    assert len(ITEMS) == 3  # FAIL — вже 4 елементи
```

### Mutable default argument

```python
# ❌ Баг — список зберігається між викликами
def process(data=[]):
    data.append("done")
    return data

# ✅ Використовуйте None
def process(data=None):
    if data is None:
        data = []
    data.append("done")
    return data
```

### Присвоєння замість копіювання

```python
# ❌ copy та original — це один об'єкт
original = [1, 2, 3]
copy = original

# ✅ Створіть справжню копію
copy = original.copy()
copy = list(original)
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-15-copying-data` — shallow copy vs deep copy