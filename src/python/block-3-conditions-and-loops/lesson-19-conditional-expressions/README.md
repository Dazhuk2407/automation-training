# Lesson 19: Conditional Expressions (Тернарний оператор)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Писати однорядкові умови (тернарний оператор)
- ✅ Розуміти коли inline умова доречна, а коли ні
- ✅ Використовувати `or` для default значень
- ✅ Застосовувати conditional expressions у тестах

---

## 📋 Передумови

Ви вже знаєте:
- if / elif / else (Lesson 18)
- Truthy / falsy значення

---

## 📖 Теорія

### 1. Тернарний оператор

Синтаксис: `value_if_true if condition else value_if_false`

```python
# Звичайний if/else
if status == 200:
    result = "ok"
else:
    result = "error"

# Тернарний оператор — те саме в один рядок
result = "ok" if status == 200 else "error"
```

---

### 2. Практичні приклади

```python
# Визначення типу
label = "admin" if user["role"] == "admin" else "user"

# Вибір значення
timeout = custom_timeout if custom_timeout else 30

# Plural форма
count = 5
word = "test" if count == 1 else "tests"
message = f"{count} {word} passed"  # "5 tests passed"

# У f-string
status = 200
print(f"Status: {'OK' if status == 200 else 'ERROR'}")
```

---

### 3. `or` для default значень

Коротший спосіб задати fallback:

```python
# Повний if/else
if username:
    name = username
else:
    name = "Anonymous"

# Тернарний
name = username if username else "Anonymous"

# Через or — найкоротший (працює з truthy/falsy)
name = username or "Anonymous"
```

**Як працює `or`:** повертає перше truthy значення або останнє:

```python
"Alice" or "Default"   # "Alice" (перше truthy)
"" or "Default"        # "Default" ("" — falsy)
None or "Default"      # "Default" (None — falsy)
0 or 42                # 42 (0 — falsy)
```

**Обережно:** `0 or 42` повертає `42`, навіть якщо `0` — валідне значення. У таких випадках краще тернарний або `.get()`.

---

### 4. Вкладені тернарні (не рекомендується)

```python
# ❌ Важко читати
result = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"

# ✅ Краще звичайний if/elif
if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
elif score >= 70:
    result = "C"
else:
    result = "F"
```

**Правило:** тернарний оператор — для **простих** умов з двома варіантами. Для складної логіки — if/elif/else.

---

### 5. У тестах

```python
def get_display_name(user):
    """Повернути nickname або name як fallback."""
    return user.get("nickname") or user["name"]


def format_status(code):
    """Коротке форматування статусу."""
    return "OK" if code == 200 else f"Error {code}"


def test_display_name_with_nickname():
    user = {"name": "Alice", "nickname": "ally"}
    assert get_display_name(user) == "ally"


def test_display_name_fallback():
    user = {"name": "Alice"}
    assert get_display_name(user) == "Alice"


def test_format_status_ok():
    assert format_status(200) == "OK"


def test_format_status_error():
    assert format_status(404) == "Error 404"
```

---

## ⚠️ Типові помилки

### Занадто складний тернарний

```python
# ❌ Нечитабельно
x = a if (b > c and d < e) else f if g else h

# ✅ Розбийте на if/else
if b > c and d < e:
    x = a
elif g:
    x = f
else:
    x = h
```

### `or` з falsy валідними значеннями

```python
# ❌ Баг: 0 — валідне значення, але falsy
port = config.get("port") or 8080
# Якщо port = 0, отримаємо 8080 замість 0!

# ✅ Правильно для таких випадків
port = config.get("port", 8080)
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-20-for-loops`