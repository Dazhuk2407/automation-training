# Lesson 29: Return Values

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Повертати значення з функцій через return
- ✅ Розуміти що функція без return повертає None
- ✅ Повертати кілька значень через tuple
- ✅ Використовувати early return для чистого коду
- ✅ Розрізняти return та print

---

## 📋 Передумови

Ви вже знаєте:
- Створення функцій, аргументи, defaults (Lesson 26-28)
- Tuple unpacking (Block 2, Lesson 10)

---

## 📖 Теорія

### 1. Базовий return

```python
def add(a, b):
    return a + b

result = add(2, 3)  # 5
```

`return` повертає значення **і зупиняє функцію**. Код після return не виконується.

---

### 2. None — неявний return

```python
def log(message):
    print(message)
    # немає return → повертає None

result = log("test")
assert result is None
```

---

### 3. return vs print

```python
# ❌ print не повертає значення
def add_bad(a, b):
    print(a + b)  # виводить на екран, але повертає None

result = add_bad(2, 3)  # виведе "5", але result = None

# ✅ return повертає значення
def add_good(a, b):
    return a + b

result = add_good(2, 3)  # result = 5
```

---

### 4. Кілька значень — tuple

```python
def min_max(numbers):
    """Повернути мінімум та максимум."""
    return min(numbers), max(numbers)

# Unpacking
minimum, maximum = min_max([5, 2, 8, 1, 9])
assert minimum == 1
assert maximum == 9

# Або як tuple
result = min_max([5, 2, 8])
assert result == (2, 8)
```

---

### 5. Early return

```python
# ❌ Глибока вкладеність
def validate(user):
    if user:
        if user.get("name"):
            if user.get("email"):
                return "valid"
            else:
                return "no_email"
        else:
            return "no_name"
    else:
        return "no_user"

# ✅ Early return — плоско і зрозуміло
def validate(user):
    if not user:
        return "no_user"
    if not user.get("name"):
        return "no_name"
    if not user.get("email"):
        return "no_email"
    return "valid"
```

---

### 6. Return у тестах

```python
def parse_status(code):
    """Повернути (category, is_error)."""
    if code < 400:
        return "success", False
    return "error", True


def classify_and_count(codes):
    """Повернути dict з кількістю по категоріях."""
    result = {"success": 0, "error": 0}
    for code in codes:
        category, _ = parse_status(code)
        result[category] += 1
    return result


def test_parse_success():
    category, is_error = parse_status(200)
    assert category == "success"
    assert is_error is False


def test_parse_error():
    category, is_error = parse_status(404)
    assert category == "error"
    assert is_error is True


def test_classify():
    result = classify_and_count([200, 200, 404, 500])
    assert result == {"success": 2, "error": 2}
```

---

## ⚠️ Типові помилки

### Забули return

```python
# ❌ Повертає None
def calculate(a, b):
    result = a + b
    # забули return result

# ✅
def calculate(a, b):
    result = a + b
    return result
```

### print замість return

```python
# ❌ Не можна використовувати результат
def get_name():
    print("Alice")  # виводить, але не повертає

# ✅
def get_name():
    return "Alice"
```

### Код після return

```python
def func():
    return 42
    print("Цей рядок ніколи не виконається")  # dead code
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-30-args-kwargs`