# Lesson 27: Function Arguments

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Використовувати positional та keyword arguments
- ✅ Розуміти порядок аргументів
- ✅ Змішувати positional та keyword аргументи правильно
- ✅ Уникати помилок з порядком аргументів

---

## 📋 Передумови

Ви вже знаєте:
- Як створювати та викликати функції (Lesson 26)

---

## 📖 Теорія

### 1. Positional arguments (за позицією)

Порядок має значення:

```python
def create_user(name, role):
    return {"name": name, "role": role}

# Positional — порядок важливий
user = create_user("Alice", "admin")
# {"name": "Alice", "role": "admin"}

# ❌ Переплутали порядок
user = create_user("admin", "Alice")
# {"name": "admin", "role": "Alice"} — баг!
```

---

### 2. Keyword arguments (за ім'ям)

Порядок НЕ важливий:

```python
# Keyword — явно вказуємо ім'я
user = create_user(name="Alice", role="admin")
user = create_user(role="admin", name="Alice")  # те саме
```

**Коли використовувати keyword:**
- Функція має 3+ параметри
- Порядок неочевидний
- Потрібна читабельність

---

### 3. Змішування positional та keyword

```python
def send_request(method, url, timeout=30, headers=None):
    return {"method": method, "url": url, "timeout": timeout}

# Positional + keyword
send_request("GET", "/api/users", timeout=60)

# ✅ Правило: positional ПЕРЕД keyword
send_request("GET", "/api/users", timeout=60)

# ❌ SyntaxError: positional після keyword
# send_request(method="GET", "/api/users")
```

---

### 4. Кілька параметрів — читабельність

```python
# ❌ Неочевидно що означає кожен аргумент
result = process(True, False, 3, "json")

# ✅ Keyword — зрозуміло
result = process(
    validate=True,
    verbose=False,
    retries=3,
    format="json",
)
```

---

### 5. У тестах

```python
def make_request(method, url, body=None, headers=None, timeout=30):
    """Імітація HTTP запиту."""
    return {
        "method": method,
        "url": url,
        "body": body,
        "headers": headers or {},
        "timeout": timeout,
    }


def test_get_request():
    req = make_request("GET", "/api/users")
    assert req["method"] == "GET"
    assert req["body"] is None


def test_post_with_body():
    req = make_request("POST", "/api/users", body={"name": "Alice"})
    assert req["method"] == "POST"
    assert req["body"] == {"name": "Alice"}


def test_custom_timeout():
    req = make_request("GET", "/api/slow", timeout=120)
    assert req["timeout"] == 120
```

---

## ⚠️ Типові помилки

### Positional після keyword

```python
# ❌ SyntaxError
# func(a=1, 2)

# ✅ Positional перед keyword
func(1, a=2)
```

### Дублювання аргументу

```python
# ❌ TypeError: got multiple values for argument 'name'
# create_user("Alice", name="Bob")
```

### Забутий аргумент

```python
def create_user(name, role):
    return {"name": name, "role": role}

# ❌ TypeError: missing required argument 'role'
# create_user("Alice")
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-28-default-parameters`