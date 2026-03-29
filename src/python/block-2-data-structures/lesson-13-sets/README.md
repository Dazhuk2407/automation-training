# Lesson 13: Sets (Множини)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати множини та розуміти їх унікальність
- ✅ Використовувати операції: union, intersection, difference
- ✅ Перевіряти підмножини та надмножини
- ✅ Видаляти дублікати зі списку через set
- ✅ Використовувати множини у тестових перевірках

---

## 📋 Передумови

Ви вже знаєте:
- Списки, кортежі, словники (Lesson 9-12)
- Оператор `in` для перевірки належності

---

## 📖 Теорія

### 1. Що таке Set

Set (множина) — **невпорядкована** колекція **унікальних** елементів:

```python
# Створення
unique_codes = {200, 301, 404, 500}
empty_set = set()  # НЕ {} — це порожній dict!

# Дублікати автоматично видаляються
numbers = {1, 2, 3, 3, 4, 4, 5}
# numbers = {1, 2, 3, 4, 5}
```

**Ключові властивості:**
- Елементи унікальні — дублікатів не буває
- Невпорядковані — порядок не гарантується
- Mutable — можна додавати/видаляти
- Елементи мають бути hashable (str, int, tuple — так; list, dict — ні)

---

### 2. Базові операції

```python
tags = {"api", "smoke", "regression"}

# Додати елемент
tags.add("critical")
# {"api", "smoke", "regression", "critical"}

# Видалити елемент (KeyError якщо немає)
tags.remove("smoke")

# Видалити безпечно (без помилки)
tags.discard("nonexistent")  # нічого не станеться

# Перевірка належності
"api" in tags      # True
"manual" not in tags  # True

# Довжина
len(tags)  # 3
```

---

### 3. Операції з множинами

Це головна суперсила set — операції над колекціями:

```python
smoke = {"login", "search", "checkout"}
regression = {"login", "search", "checkout", "profile", "settings"}

# Union (об'єднання) — все разом
smoke | regression
# {"login", "search", "checkout", "profile", "settings"}

# Intersection (перетин) — спільні
smoke & regression
# {"login", "search", "checkout"}

# Difference (різниця) — є в першому, немає в другому
regression - smoke
# {"profile", "settings"}

# Symmetric difference — є в одному АБО другому, але не в обох
smoke ^ regression
# {"profile", "settings"}
```

---

### 4. Підмножини та надмножини

```python
smoke = {"login", "search"}
full = {"login", "search", "checkout", "profile"}

# smoke — підмножина full?
smoke.issubset(full)      # True (або smoke <= full)

# full — надмножина smoke?
full.issuperset(smoke)    # True (або full >= smoke)

# Чи є спільні елементи?
smoke.isdisjoint({"api"})  # True (нічого спільного)
```

---

### 5. Видалення дублікатів

Класичне використання — прибрати дублікати зі списку:

```python
# Список з дублікатами
error_codes = [404, 500, 404, 502, 500, 404]

# Унікальні коди
unique_codes = set(error_codes)
# {404, 500, 502}

# Якщо потрібен список назад (порядок не гарантується)
unique_list = list(set(error_codes))

# Якщо потрібен порядок — dict.fromkeys()
unique_ordered = list(dict.fromkeys(error_codes))
# [404, 500, 502] — порядок збережено
```

---

### 6. Sets у тестах

```python
def test_api_returns_required_fields():
    """Перевірити що API повертає всі обов'язкові поля."""
    required = {"id", "name", "email"}
    response_fields = {"id", "name", "email", "avatar", "created_at"}
    assert required.issubset(response_fields)


def test_no_duplicate_user_ids():
    """Перевірити що ID користувачів унікальні."""
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]
    ids = [u["id"] for u in users]
    assert len(ids) == len(set(ids)), "Duplicate user IDs found"


def test_all_tests_covered():
    """Перевірити що smoke tests — підмножина всіх тестів."""
    all_tests = {"login", "search", "checkout", "profile", "settings"}
    smoke_tests = {"login", "search", "checkout"}
    assert smoke_tests <= all_tests


def test_new_endpoints_detected():
    """Знайти нові endpoints порівняно з попередньою версією."""
    v1_endpoints = {"/users", "/auth", "/products"}
    v2_endpoints = {"/users", "/auth", "/products", "/orders", "/payments"}
    new = v2_endpoints - v1_endpoints
    assert new == {"/orders", "/payments"}
```

---

## ⚠️ Типові помилки

### `{}` — це dict, не set

```python
# ❌ Це порожній словник
empty = {}
type(empty)  # <class 'dict'>

# ✅ Порожня множина
empty = set()
type(empty)  # <class 'set'>
```

### Порядок не гарантується

```python
# ❌ Може впасти — порядок set непередбачуваний
assert list({3, 1, 2}) == [1, 2, 3]

# ✅ Порівнюйте set з set
assert {3, 1, 2} == {1, 2, 3}
```

### Unhashable елементи

```python
# ❌ TypeError — list не може бути елементом set
# {[1, 2], [3, 4]}

# ✅ Використовуйте tuple
{(1, 2), (3, 4)}  # OK
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-14-mutable-vs-immutable`