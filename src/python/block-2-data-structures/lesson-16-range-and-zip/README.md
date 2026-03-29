# Lesson 16: range() та zip()

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Генерувати послідовності чисел через `range()`
- ✅ Об'єднувати колекції через `zip()`
- ✅ Використовувати `enumerate()` для індексів
- ✅ Застосовувати ці інструменти у тестових сценаріях

---

## 📋 Передумови

Ви вже знаєте:
- Списки, кортежі, словники (Lesson 9-12)
- Цикли for в Python

---

## 📖 Теорія

### 1. range() — генерація послідовностей

```python
# range(stop) — від 0 до stop-1
list(range(5))        # [0, 1, 2, 3, 4]

# range(start, stop)
list(range(1, 6))     # [1, 2, 3, 4, 5]

# range(start, stop, step)
list(range(0, 10, 2)) # [0, 2, 4, 6, 8]
list(range(10, 0, -1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

**У тестах:**

```python
def test_generate_user_ids():
    ids = list(range(1, 6))
    assert ids == [1, 2, 3, 4, 5]
    assert len(ids) == 5

def test_pagination_offsets():
    page_size = 10
    offsets = list(range(0, 50, page_size))
    assert offsets == [0, 10, 20, 30, 40]
```

---

### 2. zip() — об'єднання колекцій

`zip()` з'єднує елементи з кількох колекцій попарно:

```python
names = ["Alice", "Bob", "Charlie"]
roles = ["admin", "user", "user"]

# Попарне об'єднання
pairs = list(zip(names, roles))
# [("Alice", "admin"), ("Bob", "user"), ("Charlie", "user")]

# Зручно в циклі
for name, role in zip(names, roles):
    print(f"{name}: {role}")
```

**Створення словника з двох списків:**

```python
keys = ["name", "role", "active"]
values = ["Alice", "admin", True]

user = dict(zip(keys, values))
# {"name": "Alice", "role": "admin", "active": True}
```

**Важливо:** `zip()` зупиняється на найкоротшій колекції:

```python
a = [1, 2, 3]
b = ["x", "y"]
list(zip(a, b))  # [(1, "x"), (2, "y")] — третій елемент a загублено
```

---

### 3. enumerate() — індекс + елемент

```python
endpoints = ["/users", "/auth", "/products"]

# Без enumerate
for i in range(len(endpoints)):
    print(i, endpoints[i])

# З enumerate — чистіше
for i, endpoint in enumerate(endpoints):
    print(i, endpoint)

# З початковим індексом
for num, endpoint in enumerate(endpoints, start=1):
    print(f"{num}. {endpoint}")
# 1. /users
# 2. /auth
# 3. /products
```

---

### 4. Комбінації у тестах

```python
import pytest


def test_zip_creates_test_cases():
    """zip для створення пар input/expected."""
    inputs = [0, 1, -1, 100]
    expected = ["zero", "positive", "negative", "positive"]

    for value, exp in zip(inputs, expected):
        if value == 0:
            result = "zero"
        elif value > 0:
            result = "positive"
        else:
            result = "negative"
        assert result == exp, f"Failed for input {value}"


def test_enumerate_finds_index():
    """enumerate для пошуку індексу першого збігу."""
    responses = [200, 200, 404, 200, 500]
    error_indices = [i for i, code in enumerate(responses) if code >= 400]
    assert error_indices == [2, 4]


def test_range_generates_ids():
    """range для генерації тестових ID."""
    user_ids = list(range(100, 105))
    assert user_ids == [100, 101, 102, 103, 104]
    assert all(isinstance(id, int) for id in user_ids)
```

---

## ⚠️ Типові помилки

### Забули list() навколо range/zip

```python
# range і zip повертають ітератори, не списки
r = range(5)      # range(0, 5) — не список!
z = zip([1], [2]) # zip object — не список!

# ✅ Обгортайте в list() якщо потрібен список
list(range(5))     # [0, 1, 2, 3, 4]
list(zip([1], [2]))  # [(1, 2)]
```

### zip втрачає елементи

```python
# ❌ Різна довжина — елементи губляться
names = ["Alice", "Bob", "Charlie"]
roles = ["admin", "user"]
list(zip(names, roles))  # [("Alice", "admin"), ("Bob", "user")]
# Charlie загублена!
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-17-test-data-structures` — робота зі складними тестовими даними