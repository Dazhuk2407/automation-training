# Lesson 11: Dictionaries (Словники)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати словники та звертатися до значень за ключем
- ✅ Додавати, змінювати та видаляти елементи
- ✅ Використовувати keys(), values(), items() для ітерації
- ✅ Перевіряти наявність ключів
- ✅ Використовувати словники як тестові дані та конфігурації

---

## 📋 Передумови

Ви вже знаєте:
- Списки та кортежі (Lesson 9-10)
- Базові типи Python (Block 1)

---

## 📖 Теорія

### 1. Створення словника

Словник — це колекція **ключ: значення**. Ключі унікальні, порядок збережено (Python 3.7+):

```python
# Порожній словник
empty = {}

# Користувач
user = {
    "name": "Alice",
    "role": "admin",
    "active": True,
}

# Конфігурація
config = {
    "base_url": "https://api.example.com",
    "timeout": 30,
    "retries": 3,
}
```

---

### 2. Доступ до значень

```python
user = {"name": "Alice", "role": "admin", "age": 25}

# За ключем
user["name"]      # "Alice"
user["role"]      # "admin"

# ❌ KeyError якщо ключа немає
# user["email"]   # KeyError: 'email'
```

---

### 3. Додавання та зміна

```python
user = {"name": "Alice"}

# Додати новий ключ
user["role"] = "admin"
# {"name": "Alice", "role": "admin"}

# Змінити існуючий
user["role"] = "user"
# {"name": "Alice", "role": "user"}

# Оновити кілька ключів одночасно
user.update({"age": 25, "active": True})
# {"name": "Alice", "role": "user", "age": 25, "active": True}
```

---

### 4. Видалення

```python
user = {"name": "Alice", "role": "admin", "age": 25}

# del — видалити за ключем
del user["age"]
# {"name": "Alice", "role": "admin"}

# pop — видалити та повернути значення
role = user.pop("role")
# role = "admin", user = {"name": "Alice"}

# pop з default — без KeyError
email = user.pop("email", None)
# email = None (ключа не було, помилки немає)
```

---

### 5. Перевірка наявності ключа

```python
user = {"name": "Alice", "role": "admin"}

# in перевіряє КЛЮЧІ (не значення)
"name" in user       # True
"email" not in user  # True
"Alice" in user      # False (це значення, не ключ)
```

---

### 6. Ітерація: keys(), values(), items()

```python
config = {"host": "localhost", "port": 8080, "debug": True}

# Тільки ключі
for key in config:                 # або config.keys()
    print(key)                     # host, port, debug

# Тільки значення
for value in config.values():
    print(value)                   # localhost, 8080, True

# Ключ + значення (найчастіше)
for key, value in config.items():
    print(f"{key} = {value}")      # host = localhost, port = 8080, ...

# Як списки
list(config.keys())    # ["host", "port", "debug"]
list(config.values())  # ["localhost", 8080, True]
```

---

### 7. Словники в тестах

```python
def test_user_has_required_fields():
    """Перевірити що API повернуло всі поля."""
    user = {"id": 1, "name": "Alice", "email": "alice@test.com"}
    required = ["id", "name", "email"]
    for field in required:
        assert field in user, f"Missing field: {field}"


def test_config_values():
    """Перевірити значення конфігурації."""
    config = {"timeout": 30, "retries": 3, "debug": False}
    assert config["timeout"] == 30
    assert config["retries"] <= 5
    assert config["debug"] is False


def test_response_structure():
    """Перевірити структуру API response."""
    response = {
        "status": 200,
        "data": {"users": [{"name": "Alice"}]},
    }
    assert response["status"] == 200
    assert "data" in response
    assert len(response["data"]["users"]) == 1
```

---

## ⚠️ Типові помилки

### KeyError — ключ не існує

```python
user = {"name": "Alice"}
# user["email"]  # KeyError: 'email'

# ✅ Перевірте перед доступом
if "email" in user:
    email = user["email"]
```

### `in` перевіряє ключі, не значення

```python
data = {"name": "Alice"}
assert "name" in data     # True (ключ)
assert "Alice" not in data # True ("Alice" — це значення, не ключ)

# Перевірити значення:
assert "Alice" in data.values()
```

### Забули що dict — mutable

```python
# ❌ Зміна впливає на оригінал
original = {"a": 1}
copy = original
copy["b"] = 2
# original тепер {"a": 1, "b": 2} — сюрприз!

# ✅ Створіть копію
copy = original.copy()
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-12-safe-dict-access` — безпечний доступ до словників