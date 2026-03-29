# Lesson 21: while Loops

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Писати while цикли з умовою зупинки
- ✅ Реалізувати retry / polling паттерни
- ✅ Захищатися від нескінченних циклів
- ✅ Розуміти різницю між for та while

---

## 📋 Передумови

Ви вже знаєте:
- for цикли (Lesson 20)
- if / else (Lesson 18)

---

## 📖 Теорія

### 1. Базовий while

```python
count = 0
while count < 5:
    print(count)
    count += 1
# 0, 1, 2, 3, 4
```

**Правило:** while виконується поки умова `True`. Якщо умова ніколи не стане `False` — нескінченний цикл.

---

### 2. while vs for

| for | while |
|-----|-------|
| Відома кількість ітерацій | Невідома кількість ітерацій |
| Ітерація по колекції | Цикл поки умова True |
| `for i in range(10):` | `while not ready:` |

```python
# for — коли знаємо скільки
for i in range(5):
    process(i)

# while — коли не знаємо скільки
while not response.is_ready():
    wait()
```

---

### 3. Retry паттерн

Класичне використання while у тестуванні — повторні спроби:

```python
def retry_request(url, max_retries=3):
    """Повторити запит до max_retries разів."""
    attempt = 0
    while attempt < max_retries:
        result = make_request(url)
        if result.status == 200:
            return result
        attempt += 1
    return None  # всі спроби вичерпані
```

---

### 4. Polling паттерн

Очікування поки щось станеться:

```python
import time

def wait_for_status(check_func, timeout=10, interval=1):
    """Чекати поки check_func поверне True."""
    elapsed = 0
    while elapsed < timeout:
        if check_func():
            return True
        time.sleep(interval)
        elapsed += interval
    return False  # timeout
```

---

### 5. Захист від нескінченних циклів

```python
# ❌ Небезпечно — може зависнути
while True:
    data = get_data()
    if data:
        break

# ✅ З обмеженням
MAX_ITERATIONS = 1000
iterations = 0
while iterations < MAX_ITERATIONS:
    data = get_data()
    if data:
        break
    iterations += 1
else:
    raise TimeoutError("Max iterations reached")
```

---

### 6. У тестах

```python
def find_first_match(items, predicate):
    """Знайти перший елемент що відповідає predicate."""
    index = 0
    while index < len(items):
        if predicate(items[index]):
            return items[index]
        index += 1
    return None


def test_find_first_error():
    codes = [200, 200, 404, 500]
    result = find_first_match(codes, lambda c: c >= 400)
    assert result == 404


def test_find_no_match():
    codes = [200, 200, 201]
    result = find_first_match(codes, lambda c: c >= 400)
    assert result is None


def test_retry_simulation():
    """Симуляція retry — успіх на 3-й спробі."""
    attempts = []
    attempt = 0
    success = False
    while attempt < 5 and not success:
        attempt += 1
        attempts.append(attempt)
        if attempt == 3:
            success = True
    assert success is True
    assert len(attempts) == 3
```

---

## ⚠️ Типові помилки

### Забутий increment

```python
# ❌ Нескінченний цикл — i ніколи не змінюється
i = 0
while i < 10:
    print(i)
    # забули i += 1

# ✅
i = 0
while i < 10:
    print(i)
    i += 1
```

### while True без break

```python
# ❌ Зависне
while True:
    pass

# ✅ З умовою виходу
while True:
    result = check()
    if result:
        break
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-22-break-continue`