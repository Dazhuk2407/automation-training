# Lesson 18: if / else Conditions

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Писати умовні конструкції if / elif / else
- ✅ Розуміти truthy та falsy значення в Python
- ✅ Використовувати вкладені умови
- ✅ Писати функції з умовною логікою для тестів
- ✅ Уникати типових помилок в умовах

---

## 📋 Передумови

Ви вже знаєте:
- Базові типи Python та операції (Block 1-2)
- Оператори порівняння: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Boolean: `True`, `False`

---

## 📖 Теорія

### 1. Базовий if / else

```python
status_code = 200

if status_code == 200:
    result = "success"
else:
    result = "error"
```

---

### 2. if / elif / else — кілька умов

```python
def classify_status(code):
    """Класифікувати HTTP статус код."""
    if code < 200:
        return "informational"
    elif code < 300:
        return "success"
    elif code < 400:
        return "redirect"
    elif code < 500:
        return "client_error"
    else:
        return "server_error"
```

**Важливо:** `elif` перевіряється тільки якщо попередня умова `False`. Порядок має значення.

---

### 3. Truthy та Falsy

Python вважає деякі значення `False` навіть без явного порівняння:

| Falsy (як False) | Truthy (як True) |
|-------------------|-----------------|
| `False` | `True` |
| `0`, `0.0` | Будь-яке ненульове число |
| `""` (порожній рядок) | `"text"` |
| `[]` (порожній список) | `[1, 2]` |
| `{}` (порожній dict) | `{"key": "val"}` |
| `None` | Будь-який об'єкт |

```python
# ❌ Занадто verbose
if len(users) > 0:
    process(users)

# ✅ Pythonic — використовуємо truthy
if users:
    process(users)

# Перевірка на None
if value is not None:
    use(value)
```

---

### 4. Логічні оператори: and, or, not

```python
def can_access(user):
    """Перевірити доступ: активний admin."""
    if user["active"] and user["role"] == "admin":
        return True
    return False

def needs_review(pr):
    """PR потребує ревью якщо не draft і не від бота."""
    if not pr["draft"] and pr["author"] != "bot":
        return True
    return False
```

**Пріоритет:** `not` > `and` > `or`

```python
# Це:
if a or b and c:
    pass
# Означає:
if a or (b and c):
    pass
# Якщо потрібно інше — дужки:
if (a or b) and c:
    pass
```

---

### 5. Вкладені умови

```python
def validate_user(user):
    """Валідація з вкладеними перевірками."""
    if "name" not in user:
        return "missing_name"
    if "email" not in user:
        return "missing_email"
    if "@" not in user["email"]:
        return "invalid_email"
    return "valid"
```

**Порада:** Уникайте глибокої вкладеності (3+ рівнів). Використовуйте early return:

```python
# ❌ Глибока вкладеність
def check(user):
    if user:
        if user.get("active"):
            if user.get("role") == "admin":
                return True
    return False

# ✅ Early return — плоско і зрозуміло
def check(user):
    if not user:
        return False
    if not user.get("active"):
        return False
    if user.get("role") != "admin":
        return False
    return True
```

---

### 6. У тестах

```python
def classify_response_time(ms):
    """Класифікувати час відповіді."""
    if ms < 100:
        return "fast"
    elif ms < 500:
        return "normal"
    else:
        return "slow"


def test_fast_response():
    assert classify_response_time(50) == "fast"

def test_normal_response():
    assert classify_response_time(200) == "normal"

def test_slow_response():
    assert classify_response_time(1000) == "slow"

def test_boundary_100():
    assert classify_response_time(100) == "normal"  # 100 — вже не fast
```

---

## ⚠️ Типові помилки

### `=` замість `==`

```python
# ❌ SyntaxError (в Python 3.8+) або баг
# if status = 200:

# ✅
if status == 200:
    pass
```

### Порівняння з None через `==`

```python
# ❌ Працює, але не pythonic
if value == None:
    pass

# ✅ Правильно
if value is None:
    pass
```

### Забутий elif — зайвий else

```python
# ❌ Неочевидна логіка
def grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    else:
        return "F"  # score 85 → "B", score 70 → "F" (немає "C")

# ✅ Повний ланцюжок
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-19-conditional-expressions`