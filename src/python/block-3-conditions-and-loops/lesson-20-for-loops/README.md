# Lesson 20: for Loops

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Ітерувати по списках, словниках, рядках
- ✅ Використовувати `enumerate()` та `range()` у циклах
- ✅ Писати вкладені цикли
- ✅ Збирати результати у нову колекцію через цикл
- ✅ Використовувати for у тестових сценаріях

---

## 📋 Передумови

Ви вже знаєте:
- Колекції: list, dict, set, tuple (Block 2)
- range(), enumerate(), zip() (Lesson 16)
- if / else (Lesson 18)

---

## 📖 Теорія

### 1. Базовий for

```python
# По списку
for code in [200, 301, 404]:
    print(code)

# По рядку
for char in "pytest":
    print(char)

# По словнику (ітерація по ключах)
config = {"host": "localhost", "port": 8080}
for key in config:
    print(key, config[key])

# По парах ключ-значення
for key, value in config.items():
    print(f"{key} = {value}")
```

---

### 2. for + range()

```python
# N ітерацій
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Від start до stop
for i in range(1, 11):
    print(i)  # 1..10

# З кроком
for i in range(0, 20, 5):
    print(i)  # 0, 5, 10, 15
```

---

### 3. for + enumerate()

Коли потрібен і індекс, і елемент:

```python
endpoints = ["/users", "/auth", "/products"]

# ❌ Через range(len()) — не pythonic
for i in range(len(endpoints)):
    print(i, endpoints[i])

# ✅ Через enumerate — чисто
for i, endpoint in enumerate(endpoints):
    print(i, endpoint)
```

---

### 4. Збір результатів

```python
# Фільтрація
codes = [200, 301, 404, 500, 201]
errors = []
for code in codes:
    if code >= 400:
        errors.append(code)
# errors = [404, 500]

# Трансформація
names = ["alice", "bob", "charlie"]
upper_names = []
for name in names:
    upper_names.append(name.upper())
# ["ALICE", "BOB", "CHARLIE"]
```

---

### 5. Вкладені цикли

```python
# Перевірка всіх полів у всіх користувачах
users = [
    {"name": "Alice", "email": "a@t.com"},
    {"name": "Bob", "email": "b@t.com"},
]
required = ["name", "email"]

for user in users:
    for field in required:
        assert field in user
```

---

### 6. У тестах

```python
def test_all_responses_ok():
    """Перевірити що всі відповіді — 200."""
    responses = [200, 200, 200, 200]
    for code in responses:
        assert code == 200


def test_all_users_valid():
    """Кожен user має обов'язкові поля."""
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    for user in users:
        assert "id" in user
        assert "name" in user
        assert isinstance(user["id"], int)


def test_error_indices():
    """Знайти позиції помилок через enumerate."""
    codes = [200, 200, 404, 200, 500]
    errors = [(i, c) for i, c in enumerate(codes) if c >= 400]
    assert errors == [(2, 404), (4, 500)]
```

---

## ⚠️ Типові помилки

### Модифікація списку під час ітерації

```python
# ❌ Пропустить елементи
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)

# ✅ Створіть новий список
odd = [item for item in items if item % 2 != 0]
```

### range(len()) замість enumerate

```python
# ❌ Не pythonic
for i in range(len(items)):
    print(i, items[i])

# ✅ Pythonic
for i, item in enumerate(items):
    print(i, item)
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-21-while-loops`