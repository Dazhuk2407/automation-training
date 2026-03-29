# Lesson 30: *args та **kwargs

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Використовувати `*args` для довільної кількості позиційних аргументів
- ✅ Використовувати `**kwargs` для довільної кількості keyword аргументів
- ✅ Комбінувати звичайні параметри з `*args` та `**kwargs`
- ✅ Писати функції-обгортки (wrappers)
- ✅ Використовувати unpacking при виклику функцій

---

## 📋 Передумови

Ви вже знаєте:
- Positional та keyword arguments (Lesson 27)
- Default parameters (Lesson 28)
- Return values (Lesson 29)

---

## 📖 Теорія

### 1. *args — довільна кількість позиційних аргументів

`*args` збирає всі позиційні аргументи у **tuple**:

```python
def sum_all(*args):
    """Сума довільної кількості чисел."""
    return sum(args)

sum_all(1, 2, 3)      # 6
sum_all(10, 20)        # 30
sum_all(5)             # 5
sum_all()              # 0
```

`args` — це tuple:

```python
def show(*args):
    print(type(args))  # <class 'tuple'>
    print(args)         # (1, 2, 3)

show(1, 2, 3)
```

---

### 2. **kwargs — довільна кількість keyword аргументів

`**kwargs` збирає keyword аргументи у **dict**:

```python
def build_config(**kwargs):
    """Побудувати конфіг з довільних параметрів."""
    return kwargs

build_config(host="localhost", port=8080)
# {"host": "localhost", "port": 8080}

build_config(debug=True)
# {"debug": True}
```

---

### 3. Комбінування

Порядок: `regular, *args, **kwargs`:

```python
def log(level, *messages, **metadata):
    """Логування з довільними повідомленнями та метаданими."""
    return {
        "level": level,
        "messages": messages,
        "metadata": metadata,
    }

result = log("ERROR", "Connection failed", "Retrying...", host="api.com", code=500)
# {
#   "level": "ERROR",
#   "messages": ("Connection failed", "Retrying..."),
#   "metadata": {"host": "api.com", "code": 500},
# }
```

---

### 4. Unpacking при виклику

```python
def create_user(name, role, active):
    return {"name": name, "role": role, "active": active}

# Unpacking list/tuple → positional
args = ("Alice", "admin", True)
user = create_user(*args)

# Unpacking dict → keyword
kwargs = {"name": "Bob", "role": "user", "active": True}
user = create_user(**kwargs)
```

---

### 5. Функції-обгортки (wrappers)

Головне практичне застосування — проксування аргументів:

```python
def with_logging(func):
    """Обгортка що логує виклик."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper
```

Простіший приклад:

```python
def retry(func, *args, max_retries=3, **kwargs):
    """Повторити виклик func до max_retries разів."""
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception:
            if attempt == max_retries - 1:
                raise
```

---

### 6. У тестах

```python
def assert_fields(data, **expected):
    """Перевірити що data містить очікувані поля."""
    for key, value in expected.items():
        assert data.get(key) == value, f"Expected {key}={value}, got {data.get(key)}"


def test_assert_fields():
    user = {"name": "Alice", "role": "admin", "age": 25}
    assert_fields(user, name="Alice", role="admin")


def test_sum_all():
    def sum_all(*args):
        return sum(args)
    assert sum_all(1, 2, 3) == 6
    assert sum_all() == 0


def test_unpack_dict():
    def create(name, role):
        return {"name": name, "role": role}

    data = {"name": "Alice", "role": "admin"}
    user = create(**data)
    assert user == data
```

---

## ⚠️ Типові помилки

### Неправильний порядок

```python
# ❌ SyntaxError
# def func(**kwargs, *args):

# ✅ Правильний порядок
def func(regular, *args, **kwargs):
    pass
```

### args — це tuple, не list

```python
def func(*args):
    # args.append(4)  # ❌ AttributeError — tuple не має append
    args_list = list(args)  # ✅ конвертувати якщо треба
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-31-lambda-functions`