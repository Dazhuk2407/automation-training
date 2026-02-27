# Lesson 8: Understanding Test Output

## 🎯 Learning Outcomes

- ✅ Читати вивід pytest
- ✅ Розуміти pass/fail статуси
- ✅ Аналізувати traceback
- ✅ Інтерпретувати помилки

---

## 📖 Теорія

### 1. Базовий Вивід Pytest

```bash
$ pytest -v

tests/test_example.py::test_addition PASSED      [33%]
tests/test_example.py::test_subtraction PASSED   [66%]
tests/test_example.py::test_division FAILED      [100%]

===================== FAILURES =====================
___________ test_division ___________

    def test_division():
        result = 10 / 0
>       assert result == 5
E       ZeroDivisionError: division by zero

tests/test_example.py:5: ZeroDivisionError
```

---

### 2. Вивід Символів

| Символ | Значення |
|--------|----------|
| `.` | PASSED |
| `F` | FAILED |
| `E` | ERROR |
| `s` | SKIPPED |
| `x` | XFAIL (expected fail) |
| `X` | XPASS (unexpected pass) |

**Приклад:**
```
tests/test_example.py .F..x    [100%]

1 passed, 1 failed, 2 skipped, 1 xfailed in 0.25s
```

---

### 3. Типи Помилок

#### AssertionError

```python
def test_assert():
    x = 5
    assert x == 10  # FAIL
```

**Вивід:**
```
AssertionError: assert 5 == 10

>       assert x == 10
E       assert 5 == 10

test_example.py:3: AssertionError
```

#### ZeroDivisionError

```python
def test_division():
    result = 10 / 0  # ERROR
```

**Вивід:**
```
ZeroDivisionError: division by zero

>       result = 10 / 0
E       ZeroDivisionError: division by zero

test_example.py:2: ZeroDivisionError
```

#### ValueError

```python
def test_int_conversion():
    x = int("not a number")  # ERROR
```

**Вивід:**
```
ValueError: invalid literal for int() with base 10: 'not a number'

>       x = int("not a number")
E       ValueError: invalid literal for int() with base 10: 'not a number'

test_example.py:2: ValueError
```

---

### 4. Читання Traceback

```
tests/test_example.py::test_function FAILED

_____________ test_function ____________

    def test_function():
        x = some_function()
>       assert x == 10
E       assert 5 == 10

tests/test_example.py:4: AssertionError
```

**Розбір:**
- `test_function` - назва тесту
- Рядок коду з `>` - де сталась помилка
- `E` - повідомлення помилки
- `tests/test_example.py:4` - файл та рядок

---

### 5. Деталізація Помилок

```bash
# Коротке трасування (за замовчуванням)
pytest --tb=short

# Довге трасування
pytest --tb=long

# Дуже детальне
pytest --tb=long --showlocals

# Без трасування
pytest --tb=no
```

---

### 6. Опції для Більш Інформативного Виводу

```bash
# Показати локальні змінні
pytest -l

# Показати print() виводи
pytest -s

# Детальний вивід
pytest -vv

# Із часом кожного тесту
pytest --durations=5
```

---

### 7. Статус Коди

```bash
# Exit codes:
# 0 - all tests passed
# 1 - tests failed
# 2 - interrupted by user
# 3 - internal error
# 4 - pytest command line error
# 5 - no tests found
```

---

### 8. Аналіз Помилок

```python
# ❌ ХОЧА БЬ один assert failed - тест falls
def test_multiple_asserts():
    assert 2 + 2 == 4      # ✅ PASS
    assert 5 > 3           # ✅ PASS
    assert "hello" == "world"  # ❌ FAIL - ТЕСТ ПАДАЄ ТУТ
    assert True            # Цей assert НЕ виконається
```

**Результат:**
```
AssertionError: assert "hello" == "world"
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

