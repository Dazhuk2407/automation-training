# Lesson 10: Variables, basic data types, and type conversion

## 🎯 Learning Outcomes

- ✅ Розуміти 5 основних типів даних Python
- ✅ Створювати змінні кожного типу
- ✅ Конвертувати між типами (int(), str(), float(), bool())
- ✅ Обробляти ValueError при конверсії
- ✅ Використовувати type() та isinstance()
- ✅ Розуміти truthy/falsy значення

---

## 📖 Теорія

### 1. П'ять основних типів даних

| Тип | Назва | Приклад | Опис |
|-----|-------|---------|------|
| `str` | String | `"Hello"` | Текст (у лапках) |
| `int` | Integer | `42` | Ціле число |
| `float` | Float | `3.14` | Число з комою |
| `bool` | Boolean | `True` / `False` | Логічне значення |
| `NoneType` | None | `None` | Відсутність значення |

### 2. Створення змінних

```python
# String - текст у лапках
name = "Alice"
message = 'Hello, World!'
multiline = """Це
багаторядковий
текст"""

# Integer - ціле число
age = 25
count = -10
big_number = 1_000_000  # Підкреслення для читабельності

# Float - число з десятковою комою
price = 19.99
temperature = -5.5
scientific = 1.5e10  # 15000000000.0

# Boolean - True або False (з великої літери!)
is_active = True
is_empty = False
is_valid = 1 > 0  # True

# None - відсутність значення
result = None
data = None
```

---

### 3. Перевірка типу

```python
# Функція type() - повертає тип змінної
x = 42
print(type(x))  # <class 'int'>

# Функція isinstance() - перевіряє чи змінна певного типу
print(isinstance(42, int))        # True
print(isinstance("hello", str))   # True
print(isinstance(3.14, float))    # True
print(isinstance(True, bool))     # True
print(isinstance(None, type(None)))  # True

# isinstance() краще для перевірок у коді
if isinstance(age, int):
    print("Age is an integer")
```

---

### 4. Конверсія типів (Type Conversion)

#### 4.1 У String (str())

```python
# Будь-який тип → string
str(42)       # "42"
str(3.14)     # "3.14"
str(True)     # "True"
str(None)     # "None"

# Завжди працює!
value = str([1, 2, 3])  # "[1, 2, 3]"
```

#### 4.2 У Integer (int())

```python
# String → int
int("42")      # 42
int("100")     # 100

# Float → int (обрізає дробову частину, НЕ округлює!)
int(3.14)      # 3   (відкинули .14)
int(3.99)      # 3   (відкинули .99, не округлили до 4!)
int(-2.7)      # -2  (не -3! обрізає в бік нуля)

# Boolean → int
int(True)      # 1
int(False)     # 0

# ❌ Помилки:
int("hello")   # ValueError: invalid literal
int("3.14")    # ValueError: invalid literal (треба float())
int(None)      # TypeError
```

#### 4.3 У Float (float())

```python
# String → float
float("3.14")   # 3.14
float("100")    # 100.0

# Integer → float
float(42)       # 42.0
float(-10)      # -10.0

# Boolean → float
float(True)     # 1.0
float(False)    # 0.0

# ❌ Помилки:
float("hello")  # ValueError
float(None)     # TypeError
```

#### 4.4 У Boolean (bool())

```python
# Integer → bool
bool(1)         # True
bool(0)         # False ⚠️ Єдине число = False
bool(42)        # True
bool(-10)       # True

# String → bool
bool("hello")   # True
bool("")        # False ⚠️ Порожній рядок = False
bool(" ")       # True (пробіл - не порожній!)

# Float → bool
bool(3.14)      # True
bool(0.0)       # False ⚠️

# None → bool
bool(None)      # False ⚠️

# Списки → bool
bool([1, 2])    # True
bool([])        # False ⚠️ Порожній список = False
```

**Правило:** У Python `False` це:
- `0`, `0.0`
- `""` (порожній рядок)
- `[]`, `{}`, `()` (порожні колекції)
- `None`

Все інше - `True`!

---

### 5. Обробка помилок конверсії

```python
# Спроба конвертувати невалідне значення
try:
    number = int("abc")
except ValueError as e:
    print(f"Помилка конверсії: {e}")
    number = 0  # Значення за замовчуванням

# Безпечна конверсія з перевіркою
def safe_int(value, default=0):
    """Безпечна конверсія в int."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Використання
safe_int("42")      # 42
safe_int("hello")   # 0
safe_int(None)      # 0
```

---

### 6. Таблиця конверсій

| З → У | str() | int() | float() | bool() |
|-------|-------|-------|---------|--------|
| **str** | - | ✅ (якщо число) | ✅ (якщо число) | ✅ (""=False) |
| **int** | ✅ | - | ✅ | ✅ (0=False) |
| **float** | ✅ | ✅ (обрізає) | - | ✅ (0.0=False) |
| **bool** | ✅ | ✅ (0/1) | ✅ (0.0/1.0) | - |
| **None** | ✅ ("None") | ❌ TypeError | ❌ TypeError | ✅ (False) |

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`
