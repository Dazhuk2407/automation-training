# Lesson 9: Lists (Списки)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати списки та звертатися до елементів за індексом
- ✅ Використовувати slicing для вибору частини списку
- ✅ Змінювати списки через append, extend, pop, remove
- ✅ Сортувати та фільтрувати дані у списках
- ✅ Використовувати списки як тестові дані у pytest

---

## 📋 Передумови

Ви вже знаєте:
- Базові типи Python: int, str, float, bool (Block 1, Lesson 10)
- Вбудовані функції: len, sorted, enumerate (Block 1, Lesson 11)
- Як запускати pytest

---

## 📖 Теорія

### 1. Створення списку

Список — впорядкована колекція, яка може містити будь-які елементи:

```python
# Порожній список
empty = []

# Список чисел
status_codes = [200, 301, 404, 500]

# Список рядків
endpoints = ["/api/users", "/api/auth", "/api/products"]

# Змішаний список (рідко, але можна)
mixed = [200, "OK", True]
```

---

### 2. Доступ за індексом

Індексація починається з 0. Від'ємний індекс — з кінця:

```python
status_codes = [200, 301, 404, 500]

status_codes[0]    # 200 (перший)
status_codes[2]    # 404 (третій)
status_codes[-1]   # 500 (останній)
status_codes[-2]   # 404 (передостанній)
```

---

### 3. Slicing (зрізи)

`list[start:stop:step]` — stop не включається:

```python
codes = [200, 301, 302, 404, 500, 502, 503]

codes[0:3]     # [200, 301, 302] — перші 3
codes[:3]      # [200, 301, 302] — те саме
codes[3:]      # [404, 500, 502, 503] — з 4-го до кінця
codes[-2:]     # [502, 503] — останні 2
codes[::2]     # [200, 302, 500, 503] — кожен другий
codes[::-1]    # [503, 502, 500, 404, 302, 301, 200] — реверс
```

---

### 4. Зміна списку (мутація)

Списки — **mutable** (змінювані):

```python
users = ["Alice", "Bob"]

# Додати один елемент
users.append("Charlie")       # ["Alice", "Bob", "Charlie"]

# Додати кілька елементів
users.extend(["Diana", "Eve"])  # [..., "Diana", "Eve"]

# Вставити за індексом
users.insert(0, "Admin")       # ["Admin", "Alice", ...]

# Видалити за значенням
users.remove("Bob")            # видалить першого "Bob"

# Видалити за індексом і повернути
last = users.pop()             # видалить та поверне останній
first = users.pop(0)           # видалить та поверне перший

# Очистити
users.clear()                  # []
```

---

### 5. Пошук та перевірка

```python
endpoints = ["/api/users", "/api/auth", "/api/products"]

# Перевірка належності
"/api/users" in endpoints      # True
"/api/admin" not in endpoints  # True

# Індекс елемента
endpoints.index("/api/auth")   # 1

# Кількість входжень
codes = [200, 200, 404, 200]
codes.count(200)               # 3

# Довжина
len(endpoints)                 # 3
```

---

### 6. Сортування

```python
response_times = [150, 30, 200, 45, 180]

# sorted() — повертає НОВИЙ список (оригінал не змінюється)
sorted_times = sorted(response_times)           # [30, 45, 150, 180, 200]
sorted_desc = sorted(response_times, reverse=True)  # [200, 180, 150, 45, 30]

# .sort() — змінює список НА МІСЦІ (нічого не повертає)
response_times.sort()          # response_times тепер [30, 45, 150, 180, 200]
```

**Важливо:** `sorted()` повертає новий список, `.sort()` змінює існуючий і повертає `None`.

---

### 7. Списки в тестах

```python
import pytest


def get_active_users():
    """Імітація API — повертає список активних користувачів."""
    return [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
        {"name": "Charlie", "role": "user"},
    ]


def test_users_count():
    users = get_active_users()
    assert len(users) == 3


def test_first_user_is_admin():
    users = get_active_users()
    assert users[0]["role"] == "admin"


def test_all_users_have_name():
    users = get_active_users()
    for user in users:
        assert "name" in user
```

---

## ⚠️ Типові помилки

### IndexError — вихід за межі

```python
items = [1, 2, 3]
# items[5]  # IndexError: list index out of range

# Безпечно: перевірте довжину
if len(items) > 5:
    value = items[5]
```

### Плутанина між sorted() та .sort()

```python
data = [3, 1, 2]

# ❌ result буде None!
result = data.sort()
print(result)  # None

# ✅ Правильно
result = sorted(data)
print(result)  # [1, 2, 3]
```

### Видалення під час ітерації

```python
# ❌ Змінюється список під час циклу — пропустить елементи
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)

# ✅ Створіть новий список
items = [1, 2, 3, 4, 5]
odd_items = [item for item in items if item % 2 != 0]
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-10-tuples` — незмінні колекції