# Lesson 54: Random Data Generation

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Генерувати випадкові числа (`random`, `randint`, `uniform`)
- ✅ Обирати елементи (`choice`, `choices`, `sample`) і перемішувати (`shuffle`)
- ✅ Використовувати `seed` для відтворюваних результатів у тестах
- ✅ Генерувати тестові дані (емейли, юзери, ID)
- ✅ Знати, чому для секретів потрібен `secrets`, а не `random`

---

## 📋 Передумови

Ви вже знаєте:
- Списки (Lesson 9)
- f-strings (Lesson 39)
- Функції (Lesson 26-29)

---

## 📖 Теорія

### 1. Навіщо random у QA

Тестам постійно потрібні дані: випадкові юзери, вибірки тесткейсів, «шумові» значення для перевірки меж. Модуль `random` генерує їх швидко.

```python
import random
```

---

### 2. Випадкові числа

```python
random.random()        # float у [0.0, 1.0)
random.randint(1, 6)   # int від 1 до 6 ВКЛЮЧНО (на відміну від range!)
random.uniform(1.0, 5.0)  # float у [1.0, 5.0]
```

`randint(a, b)` включає обидві межі — інакше, ніж `range`.

---

### 3. Вибір і перемішування

```python
colors = ["red", "green", "blue"]

random.choice(colors)          # один елемент
random.choices(colors, k=5)    # k елементів З ПОВЕРНЕННЯМ (можливі повтори)
random.sample(colors, 2)       # k елементів БЕЗ повернення (унікальні)
random.shuffle(colors)         # перемішує список НА МІСЦІ (повертає None!)
```

`sample(seq, k)` кидає `ValueError`, якщо `k` більший за розмір `seq`.

---

### 4. seed — відтворюваність

Без `seed` кожен запуск дає інші числа. `random.seed(N)` фіксує послідовність — критично для **стабільних тестів** і відтворення багів.

```python
random.seed(42)
random.randint(1, 6)   # 6 — щоразу те саме після seed(42)
```

У тестах став `seed` **всередині тесту**, щоб він був самодостатнім.

---

### 5. Генерація тестових даних

```python
def random_email():
    return f"user{random.randint(1000, 9999)}@test.com"

def random_user():
    return {
        "name": random.choice(["Alice", "Bob", "Eve"]),
        "age": random.randint(18, 80),
    }
```

---

### 6. Секрети — це НЕ random

`random` не є криптостійким. Для паролів, токенів, session id використовуйте модуль **`secrets`** (`secrets.token_hex()`), а не `random`.

---

### 7. У тестах

```python
def test_dice_seeded():
    random.seed(42)
    assert random.randint(1, 6) == 6

def test_choice_in_range():
    assert random.choice([1, 2, 3]) in [1, 2, 3]

def test_sample_length():
    assert len(random.sample(range(100), 5)) == 5
```

---

## ⚠️ Типові помилки

### randint включає верхню межу

```python
# range(1, 6) → 1..5, а randint(1, 6) → 1..6
random.randint(1, 6)  # ✅ може повернути 6
```

### shuffle повертає None

```python
# ❌ nums = random.shuffle(nums)  → nums стане None
random.shuffle(nums)   # ✅ змінює список на місці
```

### random для секретів

```python
# ❌ token = str(random.random())      # не криптостійко
# ✅ import secrets; token = secrets.token_hex(16)
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-55-modules-and-packages`
