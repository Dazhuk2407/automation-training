# Lesson 31: Lambda Functions

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати lambda функції
- ✅ Використовувати lambda з sorted(), filter(), map()
- ✅ Розуміти коли lambda доречна, а коли ні
- ✅ Уникати зловживання lambda

---

## 📋 Передумови

Ви вже знаєте:
- Створення функцій через def (Lesson 26)
- List comprehensions (Block 3, Lesson 23)

---

## 📖 Теорія

### 1. Синтаксис

```python
# def — звичайна функція
def double(n):
    return n * 2

# lambda — анонімна функція в один рядок
double = lambda n: n * 2

# Обидва працюють однаково
double(5)  # 10
```

**Синтаксис:** `lambda параметри: вираз`

Lambda може мати тільки **один вираз** — він автоматично повертається (без `return`).

---

### 2. Головне використання — sorted()

```python
users = [
    {"name": "Charlie", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
]

# Сортувати за іменем
sorted(users, key=lambda u: u["name"])
# [Alice, Bob, Charlie]

# Сортувати за віком
sorted(users, key=lambda u: u["age"])
# [Alice(25), Charlie(30), Bob(35)]

# Сортувати за віком (спадання)
sorted(users, key=lambda u: u["age"], reverse=True)
```

---

### 3. filter() та map()

```python
numbers = [1, -2, 3, -4, 5]

# filter — залишити тільки позитивні
positive = list(filter(lambda n: n > 0, numbers))
# [1, 3, 5]

# map — трансформувати кожен елемент
doubled = list(map(lambda n: n * 2, numbers))
# [2, -4, 6, -8, 10]
```

**Але:** list comprehension часто читабельніший:

```python
# filter + lambda
positive = list(filter(lambda n: n > 0, numbers))

# comprehension — зрозуміліше
positive = [n for n in numbers if n > 0]
```

---

### 4. Коли використовувати lambda

| Ситуація | lambda | def |
|----------|--------|-----|
| `key=` для sorted/min/max | ✅ | зайве |
| Проста трансформація в map | ✅ | зайве |
| Складна логіка | ❌ | ✅ |
| Потрібна документація | ❌ | ✅ |
| Повторне використання | ❌ | ✅ |

**Правило:** lambda — для коротких одноразових функцій. Якщо lambda не вміщується в рядок — використовуйте def.

---

### 5. Коли НЕ використовувати

```python
# ❌ Надто складно для lambda
process = lambda x: x.strip().lower().replace(" ", "_") if x else "unknown"

# ✅ Краще def
def process(x):
    if not x:
        return "unknown"
    return x.strip().lower().replace(" ", "_")

# ❌ Присвоювати lambda змінній (PEP 8)
double = lambda n: n * 2

# ✅ Просто def
def double(n):
    return n * 2
```

---

### 6. У тестах

```python
def test_sort_by_name():
    users = [{"name": "Charlie"}, {"name": "Alice"}, {"name": "Bob"}]
    result = sorted(users, key=lambda u: u["name"])
    assert [u["name"] for u in result] == ["Alice", "Bob", "Charlie"]


def test_sort_by_response_time():
    responses = [
        {"url": "/api", "time": 150},
        {"url": "/auth", "time": 30},
        {"url": "/data", "time": 200},
    ]
    fastest = min(responses, key=lambda r: r["time"])
    assert fastest["url"] == "/auth"


def test_filter_active():
    users = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False},
    ]
    active = list(filter(lambda u: u["active"], users))
    assert len(active) == 1
```

---

## ⚠️ Типові помилки

### Lambda з кількома виразами

```python
# ❌ SyntaxError — lambda може мати тільки один вираз
# f = lambda x: x += 1; return x

# ✅ Використовуйте def
def f(x):
    x += 1
    return x
```

### Присвоєння lambda (PEP 8 E731)

```python
# ❌ PEP 8 не рекомендує
double = lambda n: n * 2

# ✅
def double(n):
    return n * 2
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-32-scope-and-globals`