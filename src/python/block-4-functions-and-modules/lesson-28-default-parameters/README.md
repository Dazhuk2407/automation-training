# Lesson 28: Default Parameters

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Задавати значення за замовчуванням для параметрів
- ✅ Розуміти пастку mutable default arguments
- ✅ Правильно використовувати None як default
- ✅ Створювати гнучкі функції з опціональними параметрами

---

## 📋 Передумови

Ви вже знаєте:
- Positional та keyword arguments (Lesson 27)
- Mutable vs immutable типи (Block 2, Lesson 14)

---

## 📖 Теорія

### 1. Значення за замовчуванням

```python
def make_request(method, url, timeout=30, verify=True):
    return {"method": method, "url": url, "timeout": timeout, "verify": verify}

# Всі defaults
make_request("GET", "/api")
# {"method": "GET", "url": "/api", "timeout": 30, "verify": True}

# Перевизначити один
make_request("GET", "/api", timeout=60)

# Перевизначити кілька
make_request("GET", "/api", timeout=60, verify=False)
```

**Правило:** параметри з default **завжди після** параметрів без default:

```python
# ✅ Правильно
def func(required, optional=10):
    pass

# ❌ SyntaxError
# def func(optional=10, required):
#     pass
```

---

### 2. Mutable Default Argument — ГОЛОВНА ПАСТКА

```python
# ❌ НЕБЕЗПЕЧНО — list спільний між усіма викликами
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags

result1 = add_tag("smoke")     # ["smoke"]
result2 = add_tag("api")       # ["smoke", "api"] — СЮРПРИЗ!
result3 = add_tag("regression") # ["smoke", "api", "regression"]
```

**Чому так?** Default `[]` створюється **один раз** при визначенні функції, а не при кожному виклику. Всі виклики працюють з **тим самим списком**.

---

### 3. Правильний спосіб — None як default

```python
# ✅ ПРАВИЛЬНО — None + створення всередині
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags

result1 = add_tag("smoke")     # ["smoke"]
result2 = add_tag("api")       # ["api"] — кожен виклик свій список ✅
```

**Правило:** ніколи не використовуйте `list`, `dict`, `set` як default. Завжди `None`.

```python
# ✅ Шаблон
def func(items=None, config=None):
    if items is None:
        items = []
    if config is None:
        config = {}
```

---

### 4. Реальні приклади

```python
def create_user(name, role="user", active=True, permissions=None):
    """Створити користувача з defaults."""
    if permissions is None:
        permissions = []
    return {
        "name": name,
        "role": role,
        "active": active,
        "permissions": permissions,
    }


def build_headers(content_type="application/json", auth_token=None, extra=None):
    """Побудувати HTTP headers."""
    headers = {"Content-Type": content_type}
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    if extra:
        headers.update(extra)
    return headers
```

---

## ⚠️ Типові помилки

### Mutable default — dict

```python
# ❌ Той самий dict між викликами
def set_config(key, value, config={}):
    config[key] = value
    return config

# ✅ None як default
def set_config(key, value, config=None):
    if config is None:
        config = {}
    config[key] = value
    return config
```

### Default після required

```python
# ❌ SyntaxError
# def func(a=1, b):

# ✅ Required перед default
def func(b, a=1):
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

**Далі:** `lesson-29-return-values`