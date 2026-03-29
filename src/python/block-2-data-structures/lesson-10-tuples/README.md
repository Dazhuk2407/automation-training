# Lesson 10: Tuples (Кортежі)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати кортежі та розуміти їх immutable природу
- ✅ Використовувати unpacking для зручного доступу до елементів
- ✅ Розуміти коли tuple краще за list
- ✅ Повертати кілька значень з функцій через tuple
- ✅ Використовувати кортежі в тестових сценаріях

---

## 📋 Передумови

Ви вже знаєте:
- Списки: створення, індексація, slicing, методи (Lesson 9)
- Базові типи Python (Block 1)

---

## 📖 Теорія

### 1. Що таке Tuple

Tuple (кортеж) — впорядкована колекція, яку **не можна змінити** після створення:

```python
# Створення
point = (10, 20)
status = (200, "OK")
single = (42,)        # одноелементний — кома обов'язкова!
empty = ()

# Без дужок теж працює (але з дужками читабельніше)
coords = 10, 20       # це теж tuple
```

---

### 2. Доступ — як у списку

Індексація та slicing працюють так само:

```python
response = (200, "OK", {"data": []})

response[0]     # 200
response[1]     # "OK"
response[-1]    # {"data": []}
response[:2]    # (200, "OK")

len(response)   # 3
200 in response # True
```

---

### 3. Immutable — не можна змінити

```python
point = (10, 20)

# ❌ Все це дасть TypeError
# point[0] = 30
# point.append(30)
# point.remove(10)
```

**Чому це добре:**
- Гарантія що дані не зміняться випадково
- Безпечно передавати у функції — ніхто не зіпсує
- Може бути ключем словника (list — не може)

---

### 4. Unpacking — розпакування

Головна суперсила tuple — зручне розпакування:

```python
# Базовий unpacking
point = (10, 20)
x, y = point
# x = 10, y = 20

# Unpacking з функцій
def get_status():
    return 200, "OK"

code, message = get_status()
# code = 200, message = "OK"

# Unpacking з ігноруванням (_)
status = (200, "OK", {"data": []})
code, _, body = status
# code = 200, body = {"data": []}

# Unpacking з * (зірочкою)
first, *rest = (1, 2, 3, 4, 5)
# first = 1, rest = [2, 3, 4, 5]

head, *middle, tail = (1, 2, 3, 4, 5)
# head = 1, middle = [2, 3, 4], tail = 5
```

---

### 5. Tuple vs List — коли що

| Ознака | Tuple | List |
|--------|-------|------|
| Змінюваність | Immutable (не можна змінити) | Mutable (можна змінити) |
| Синтаксис | `(1, 2, 3)` | `[1, 2, 3]` |
| Швидкість | Трохи швидший | Трохи повільніший |
| Ключ словника | Може бути | Не може |
| Коли використовувати | Фіксовані дані, координати, повернення з функції | Динамічні дані, колекції що змінюються |

**Правило:** якщо дані не повинні змінюватися — використовуйте tuple.

---

### 6. Tuples у тестах

```python
import pytest


def parse_response(raw):
    """Парсить відповідь і повертає (status_code, body)."""
    return raw["status"], raw["body"]


def test_parse_response():
    raw = {"status": 200, "body": {"users": []}}
    code, body = parse_response(raw)
    assert code == 200
    assert body == {"users": []}


# Parametrize з tuples — класичний pytest-паттерн
@pytest.mark.parametrize("input_val, expected", [
    (0, "zero"),
    (1, "positive"),
    (-1, "negative"),
])
def test_classify_number(input_val, expected):
    if input_val == 0:
        result = "zero"
    elif input_val > 0:
        result = "positive"
    else:
        result = "negative"
    assert result == expected
```

---

### 7. Named Tuples (preview)

Для кращої читабельності можна іменувати поля:

```python
from collections import namedtuple

User = namedtuple("User", ["name", "role", "active"])

alice = User(name="Alice", role="admin", active=True)
alice.name    # "Alice"
alice.role    # "admin"
alice[0]      # "Alice" — індекс теж працює
```

Це preview — детальніше в наступних блоках.

---

## ⚠️ Типові помилки

### Забули кому в одноелементному tuple

```python
# ❌ Це НЕ tuple, це просто число в дужках
not_a_tuple = (42)
type(not_a_tuple)  # <class 'int'>

# ✅ Кома робить tuple
real_tuple = (42,)
type(real_tuple)   # <class 'tuple'>
```

### Спроба змінити tuple

```python
# ❌ TypeError
data = (1, 2, 3)
# data[0] = 10

# ✅ Створіть новий tuple
data = (10,) + data[1:]  # (10, 2, 3)
```

### Неправильний unpacking

```python
# ❌ ValueError: too many values to unpack
point = (10, 20, 30)
# x, y = point

# ✅ Правильна кількість змінних
x, y, z = point

# ✅ Або з *
x, *rest = point  # x = 10, rest = [20, 30]
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-11-dictionaries` — словники