# Lesson 24: Generators (Генератори)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати generator expressions
- ✅ Писати generator functions з yield
- ✅ Розуміти ліниві обчислення (lazy evaluation)
- ✅ Використовувати генератори для обробки великих даних
- ✅ Розуміти різницю між list comprehension та generator

---

## 📋 Передумови

Ви вже знаєте:
- List comprehensions (Lesson 23)
- for цикли та ітерація (Lesson 20)

---

## 📖 Теорія

### 1. Generator expression

Синтаксис як у list comprehension, але з круглими дужками `()`:

```python
# List comprehension — створює весь список в пам'яті
squares_list = [n ** 2 for n in range(1000000)]  # 1M елементів у пам'яті

# Generator expression — обчислює по одному елементу
squares_gen = (n ** 2 for n in range(1000000))  # майже 0 пам'яті
```

Генератор обчислює елементи **ліниво** — тільки коли їх запитують.

---

### 2. Використання generator з all(), any(), sum()

```python
users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
]

# all() та any() приймають генератор напряму
all_active = all(u["active"] for u in users)    # False
any_active = any(u["active"] for u in users)    # True

# sum() теж
total = sum(u.get("score", 0) for u in users)
```

**Перевага:** не створює проміжний список — ефективніше для великих даних.

---

### 3. Generator function (yield)

`yield` замість `return` — функція стає генератором:

```python
def count_up_to(n):
    """Генерувати числа від 1 до n."""
    i = 1
    while i <= n:
        yield i
        i += 1

# Використання
for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5

# Або перетворити в список
numbers = list(count_up_to(5))  # [1, 2, 3, 4, 5]
```

---

### 4. yield vs return

```python
# return — повертає одне значення і завершує функцію
def get_all():
    return [1, 2, 3, 4, 5]

# yield — повертає значення по одному, пам'ятає стан
def generate_all():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
```

---

### 5. Практичні генератори

```python
def generate_test_users(count):
    """Генерувати тестових користувачів."""
    for i in range(1, count + 1):
        yield {
            "id": i,
            "name": f"User_{i}",
            "email": f"user{i}@test.com",
        }


def retry_responses(responses):
    """Генерувати відповіді для retry тестів."""
    for response in responses:
        yield response


def page_numbers(total, page_size):
    """Генерувати номери сторінок для пагінації."""
    page = 1
    while (page - 1) * page_size < total:
        yield page
        page += 1
```

---

### 6. У тестах

```python
def test_all_active():
    users = [{"active": True}, {"active": True}]
    assert all(u["active"] for u in users)


def test_any_error():
    codes = [200, 200, 500, 200]
    assert any(c >= 400 for c in codes)


def test_generate_users():
    users = list(generate_test_users(3))
    assert len(users) == 3
    assert users[0]["name"] == "User_1"
    assert users[2]["email"] == "user3@test.com"


def test_pagination():
    pages = list(page_numbers(total=25, page_size=10))
    assert pages == [1, 2, 3]
```

---

## ⚠️ Типові помилки

### Генератор можна ітерувати тільки один раз

```python
gen = (n for n in range(5))
list(gen)  # [0, 1, 2, 3, 4]
list(gen)  # [] — вже вичерпаний!
```

### Генератор — не список

```python
gen = (n for n in range(5))
# len(gen)   # TypeError — генератор не має len()
# gen[0]     # TypeError — генератор не підтримує індексацію
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-25-operators`