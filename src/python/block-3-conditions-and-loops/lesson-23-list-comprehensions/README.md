# Lesson 23: List Comprehensions

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Замінити for + append на list comprehension
- ✅ Фільтрувати дані через comprehension з if
- ✅ Використовувати dict та set comprehensions
- ✅ Розуміти коли comprehension доречний, а коли ні

---

## 📋 Передумови

Ви вже знаєте:
- for цикли та збір результатів (Lesson 20)
- Колекції: list, dict, set (Block 2)

---

## 📖 Теорія

### 1. Базовий list comprehension

Синтаксис: `[expression for item in iterable]`

```python
# for + append
squares = []
for n in range(1, 6):
    squares.append(n ** 2)

# List comprehension — те саме, але коротше
squares = [n ** 2 for n in range(1, 6)]
# [1, 4, 9, 16, 25]
```

---

### 2. З фільтрацією (if)

`[expression for item in iterable if condition]`

```python
# Тільки парні
evens = [n for n in range(10) if n % 2 == 0]
# [0, 2, 4, 6, 8]

# Тільки коди помилок
codes = [200, 301, 404, 500, 201]
errors = [c for c in codes if c >= 400]
# [404, 500]

# Активні користувачі
users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True},
]
active_names = [u["name"] for u in users if u["active"]]
# ["Alice", "Charlie"]
```

---

### 3. З трансформацією та умовою

```python
# Трансформація + фільтр
emails = [u["email"].lower() for u in users if u.get("email")]

# if/else всередині expression (тернарний)
labels = ["OK" if c < 400 else "ERROR" for c in [200, 404, 500]]
# ["OK", "ERROR", "ERROR"]
```

**Зверніть увагу на позицію if:**
- `[x for x in items if condition]` — **фільтр** (пропустити елементи)
- `[a if condition else b for x in items]` — **трансформація** (змінити значення)

---

### 4. Dict comprehension

```python
# Словник з двох списків
keys = ["name", "role"]
values = ["Alice", "admin"]
user = {k: v for k, v in zip(keys, values)}
# {"name": "Alice", "role": "admin"}

# Інвертувати словник
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

# Фільтр словника
config = {"host": "localhost", "port": 8080, "debug": True, "verbose": False}
truthy_config = {k: v for k, v in config.items() if v}
# {"host": "localhost", "port": 8080, "debug": True}
```

---

### 5. Set comprehension

```python
# Унікальні домени з email
emails = ["alice@gmail.com", "bob@yahoo.com", "charlie@gmail.com"]
domains = {email.split("@")[1] for email in emails}
# {"gmail.com", "yahoo.com"}
```

---

### 6. Коли НЕ використовувати comprehension

```python
# ❌ Занадто складно — важко читати
result = [
    transform(x)
    for x in items
    if validate(x) and x.status == "active"
    if x.role in allowed_roles
]

# ✅ Краще звичайний цикл
result = []
for x in items:
    if not validate(x):
        continue
    if x.status != "active":
        continue
    if x.role not in allowed_roles:
        continue
    result.append(transform(x))
```

**Правило:** якщо comprehension не вміщується в один рядок або має 2+ умови — використовуйте цикл.

---

### 7. У тестах

```python
def test_extract_user_ids():
    users = [{"id": 1}, {"id": 2}, {"id": 3}]
    ids = [u["id"] for u in users]
    assert ids == [1, 2, 3]


def test_filter_error_codes():
    responses = [200, 201, 404, 500, 204]
    errors = [c for c in responses if c >= 400]
    assert errors == [404, 500]


def test_unique_roles():
    users = [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
        {"name": "Charlie", "role": "user"},
    ]
    roles = {u["role"] for u in users}
    assert roles == {"admin", "user"}
```

---

## ⚠️ Типові помилки

### Плутанина з позицією if

```python
# Фільтр — if в кінці
[x for x in items if x > 0]

# Тернарний — if/else перед for
[x if x > 0 else 0 for x in items]

# ❌ SyntaxError — if без else перед for
# [x if x > 0 for x in items]
```

### Надто складний comprehension

```python
# ❌ Нечитабельно
data = {k: [x["val"] for x in v if x["ok"]] for k, v in groups.items() if v}

# ✅ Розбийте на кроки
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-24-generators`