# Lesson 12: Безпечний доступ до словників

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Використовувати `.get()` для безпечного доступу
- ✅ Задавати default values для відсутніх ключів
- ✅ Використовувати `setdefault()` для ініціалізації
- ✅ Обробляти відсутні ключі без KeyError
- ✅ Писати стійкі тести для API responses з неповними даними

---

## 📋 Передумови

Ви вже знаєте:
- Словники: створення, доступ, модифікація (Lesson 11)
- Що таке KeyError

---

## 📖 Теорія

### 1. Проблема: KeyError

У реальних тестах дані часто неповні. API може не повернути поле, конфіг може не мати ключа:

```python
# ❌ KeyError якщо поля немає
user = {"name": "Alice"}
email = user["email"]  # KeyError: 'email'
```

Це найчастіша причина падіння тестів при роботі зі словниками.

---

### 2. Рішення: `.get()`

`.get(key, default)` повертає значення за ключем. Якщо ключа немає — повертає `default` (за замовчуванням `None`):

```python
user = {"name": "Alice", "role": "admin"}

# Ключ є → повертає значення
user.get("name")          # "Alice"

# Ключа немає → повертає None (без помилки)
user.get("email")         # None

# Ключа немає → повертає default
user.get("email", "N/A")  # "N/A"
user.get("age", 0)        # 0
```

**Правило:** якщо ключ може бути відсутній — завжди використовуйте `.get()`.

---

### 3. `.get()` vs `[]` — коли що

```python
config = {"host": "localhost", "port": 8080}

# [] — коли ключ ОБОВ'ЯЗКОВО має бути (KeyError = баг)
host = config["host"]

# .get() — коли ключ МОЖЕ бути відсутній (None = нормально)
timeout = config.get("timeout", 30)
```

| Ситуація | Спосіб | Чому |
|----------|--------|------|
| Ключ обов'язковий | `dict["key"]` | KeyError покаже що дані некоректні |
| Ключ опціональний | `dict.get("key", default)` | Безпечно, не впаде |
| Не знаю чи є | `dict.get("key")` | Повертає None |

---

### 4. `setdefault()` — ініціалізація

`setdefault(key, default)` — якщо ключ є, повертає його. Якщо немає — додає default і повертає:

```python
config = {"host": "localhost"}

# Ключ є → повертає існуюче значення, нічого не змінює
config.setdefault("host", "0.0.0.0")  # "localhost"

# Ключа немає → додає default
config.setdefault("port", 8080)       # 8080
# config = {"host": "localhost", "port": 8080}
```

Корисно для накопичення даних:

```python
# Групування помилок за типом
errors = {}
for error in ["timeout", "404", "timeout", "500", "timeout"]:
    errors.setdefault(error, []).append(1)
# {"timeout": [1, 1, 1], "404": [1], "500": [1]}
```

---

### 5. Перевірка перед доступом

Іноді потрібна явна перевірка:

```python
user = {"name": "Alice"}

# Варіант 1: in + []
if "email" in user:
    email = user["email"]
else:
    email = "not provided"

# Варіант 2: .get() (коротше і краще)
email = user.get("email", "not provided")

# Варіант 3: try/except (коли потрібна складна обробка)
try:
    email = user["email"]
except KeyError:
    email = "not provided"
    log_missing_field("email")
```

---

### 6. Безпечний доступ до вкладених словників

```python
response = {
    "status": 200,
    "data": {"user": {"name": "Alice"}},
}

# ❌ Небезпечно — будь-який рівень може бути відсутній
# name = response["data"]["user"]["name"]

# ✅ Покроковий безпечний доступ
data = response.get("data", {})
user = data.get("user", {})
name = user.get("name", "Unknown")
assert name == "Alice"
```

---

### 7. У тестах

```python
def test_api_response_with_optional_fields():
    """API може повернути неповні дані."""
    response = {"id": 1, "name": "Alice"}  # email відсутній

    assert response.get("id") is not None
    assert response.get("name") == "Alice"
    assert response.get("email") is None  # нормально — поле опціональне
    assert response.get("email", "N/A") == "N/A"


def test_config_defaults():
    """Конфіг з default values."""
    config = {"host": "localhost"}

    host = config.get("host", "0.0.0.0")
    port = config.get("port", 8080)
    timeout = config.get("timeout", 30)

    assert host == "localhost"  # є в конфігу
    assert port == 8080         # default
    assert timeout == 30        # default
```

---

## ⚠️ Типові помилки

### `.get()` без default при порівнянні

```python
user = {"name": "Alice"}

# ❌ Порівнюєте None з рядком — тест впаде
assert user.get("email") == "alice@test.com"

# ✅ Перевірте чи ключ взагалі є
assert user.get("email") is None
# або
assert "email" not in user
```

### Використання `[]` для опціональних полів

```python
# ❌ Впаде якщо metadata відсутній
metadata = response["metadata"]["version"]

# ✅ Безпечний ланцюжок
metadata = response.get("metadata", {})
version = metadata.get("version", "unknown")
```

### Плутання `.get()` та `setdefault()`

```python
config = {"host": "localhost"}

# .get() НЕ змінює словник
config.get("port", 8080)
assert "port" not in config  # port не додано

# setdefault() ЗМІНЮЄ словник
config.setdefault("port", 8080)
assert config["port"] == 8080  # port додано
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-13-sets` — множини