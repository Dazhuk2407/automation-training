# Exercises - Lesson 8: Understanding Test Output

## Exercise 1: Read Simple Output (EASY)

```bash
# Запустіть:
pytest -v

# Розберіть вивід:
# ✅ PASSED - тест пройшов
# ❌ FAILED - тест впав
# ⏭️  SKIPPED - тест пропущено
```

---

## Exercise 2: Analyze Failing Test (EASY)

Створіть `test_fail.py`:

```python
def test_failing():
    x = 5
    assert x == 10, f"Expected 10 but got {x}"
```

Запустіть:
```bash
pytest test_fail.py -v
```

**Аналізуйте:**
- Рядок де тест впав
- Повідомлення помилки
- Назва тесту

---

## Exercise 3: Exception Tracebacks (MEDIUM)

```python
def test_zero_division():
    result = 10 / 0
```

Запустіть:
```bash
pytest test_exception.py -v --tb=short
pytest test_exception.py -v --tb=long
pytest test_exception.py -v --tb=no
```

**Порівняйте виводи!**

---

## Exercise 4: Print Output Analysis (MEDIUM)

```python
def test_with_prints():
    print("Step 1")
    x = 5
    print(f"x = {x}")
    print("Step 2")
    assert x == 5
```

Запустіть:
```bash
pytest test_prints.py        # print не показується
pytest test_prints.py -s     # print показується
```

---

## Exercise 5: Multiple Failures (HARD)

```python
def test_multiple_assertions():
    assert 1 + 1 == 2
    assert 2 + 2 == 4
    assert 3 + 3 == 5  # Впаде тут
    assert 4 + 4 == 8  # Цей НЕ виконається
```

**Запустіть та спостерігайте:**
- Як많 assertions виконався до failure?
- Які assertion впав?

---

## Exercise 6: Detailed Error Analysis (HARD)

```python
def test_dict_error():
    user = {"name": "Alice", "age": 25}
    assert user["email"] == "alice@example.com"
```

Запустіть:
```bash
pytest test_dict.py -v --tb=long -l
```

**Аналізуйте:**
- Тип помилки (KeyError)
- Рядок коду
- Локальні змінні

---

**Run these exercises and understand the output!**

