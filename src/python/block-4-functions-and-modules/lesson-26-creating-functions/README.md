# Lesson 26: Creating Functions

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати функції через `def`
- ✅ Викликати функції з параметрами
- ✅ Розуміти навіщо потрібні функції
- ✅ Писати helper-функції для тестів
- ✅ Розуміти різницю між визначенням та викликом

---

## 📋 Передумови

Ви вже знаєте:
- Змінні, типи, оператори (Block 1-2)
- if/else, цикли (Block 3)
- Вбудовані функції: len, sorted, range (Block 1)

---

## 📖 Теорія

### 1. Навіщо потрібні функції

Без функцій код дублюється:

```python
# ❌ Дублювання
assert len("alice@test.com") > 0 and "@" in "alice@test.com"
assert len("bob@test.com") > 0 and "@" in "bob@test.com"
assert len("charlie@test.com") > 0 and "@" in "charlie@test.com"

# ✅ Функція — написати один раз, використати скрізь
def is_valid_email(email):
    return len(email) > 0 and "@" in email

assert is_valid_email("alice@test.com")
assert is_valid_email("bob@test.com")
assert is_valid_email("charlie@test.com")
```

**Функції дають:**
- **DRY** — Don't Repeat Yourself
- **Читабельність** — `is_valid_email(x)` зрозуміліше за `len(x) > 0 and "@" in x`
- **Тестовність** — функцію легко протестувати окремо

---

### 2. Створення функції (def)

```python
def greet(name):
    """Привітати користувача."""
    return f"Hello, {name}!"

# Виклик
message = greet("Alice")  # "Hello, Alice!"
```

**Анатомія функції:**
1. `def` — ключове слово
2. `greet` — ім'я функції (snake_case)
3. `(name)` — параметри
4. `:` — двокрапка
5. Тіло функції (з відступом)
6. `return` — повернути результат

---

### 3. Функції без return

Якщо `return` немає — функція повертає `None`:

```python
def log_action(action):
    """Записати дію (нічого не повертає)."""
    print(f"[LOG] {action}")

result = log_action("login")
# result is None
```

---

### 4. Параметри vs аргументи

```python
# name — це ПАРАМЕТР (при визначенні)
def greet(name):
    return f"Hello, {name}!"

# "Alice" — це АРГУМЕНТ (при виклику)
greet("Alice")
```

---

### 5. Функції для тестів — реальні приклади

```python
def validate_status_code(code):
    """Перевірити що код — успішний (2xx)."""
    return 200 <= code < 300


def format_user(name, role):
    """Створити словник користувача."""
    return {"name": name, "role": role, "active": True}


def calculate_discount(price, percent):
    """Розрахувати ціну зі знижкою."""
    return price * (1 - percent / 100)


# Тести
def test_validate_status():
    assert validate_status_code(200) is True
    assert validate_status_code(404) is False

def test_format_user():
    user = format_user("Alice", "admin")
    assert user["name"] == "Alice"
    assert user["active"] is True

def test_discount():
    assert calculate_discount(100, 10) == 90.0
```

---

### 6. Naming conventions

```python
# ✅ snake_case для функцій
def calculate_total():
    pass

def is_valid_email():  # is_ для boolean результатів
    pass

def get_user_by_id():  # get_ для отримання даних
    pass

# ❌ Не використовувати
def CalculateTotal():   # CamelCase — для класів
    pass

def calc():             # занадто коротко
    pass
```

---

## ⚠️ Типові помилки

### Виклик без дужок

```python
def get_status():
    return 200

# ❌ Це посилання на функцію, не виклик
result = get_status
print(result)  # <function get_status at 0x...>

# ✅ Виклик з дужками
result = get_status()
print(result)  # 200
```

### Визначення після виклику

```python
# ❌ NameError — функція ще не визначена
# result = greet("Alice")

def greet(name):
    return f"Hello, {name}!"

# ✅ Виклик після визначення
result = greet("Alice")
```

### Shadowing вбудованих функцій

```python
# ❌ Перезаписує вбудований list
def list(items):
    return items

# Тепер list() не працює як раніше!
# list([1, 2, 3])  # викличе вашу функцію, не вбудовану
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-27-arguments`