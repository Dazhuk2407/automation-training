# Exercises - Lesson 3: First Test File

## Exercise 1: Write Your First Test (EASY)

Створіть файл `test_basic.py`:

```python
def test_addition():
    """Тест додавання."""
    result = 5 + 3
    assert result == 8

def test_string():
    """Тест рядка."""
    text = "hello"
    assert len(text) == 5
    assert text.upper() == "HELLO"
```

Запустіть:
```bash
pytest test_basic.py -v
```

**Expected:** 2 passed ✅

---

## Exercise 2: Test a Calculator Function (EASY)

Створіть `calculator.py`:
```python
def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b
```

Створіть `test_calculator.py`:
```python
from calculator import subtract, divide

def test_subtract():
    assert subtract(10, 3) == 7

def test_divide():
    assert divide(10, 2) == 5
```

---

## Exercise 3: Multiple Assertions (MEDIUM)

```python
def test_list_operations():
    """Тест операцій зі списками."""
    numbers = [1, 2, 3, 4, 5]
    
    # TODO: Додайте assertions:
    # 1. Довжина списку = 5
    # 2. Перший елемент = 1
    # 3. Останній елемент = 5
    # 4. Сума елементів = 15
    # 5. 3 є в списку
```

---

## Exercise 4: Test Pass and Fail (MEDIUM)

Створіть 2 тести - один проходить, інший падає:

```python
def test_pass():
    """Цей тест має пройти."""
    # TODO: Напишіть assertion який пройде
    pass

def test_fail():
    """Цей тест має впасти."""
    # TODO: Напишіть assertion який впаде
    pass
```

Запустіть і подивіться різницю у виводі.

---

## Exercise 5: Test String Methods (MEDIUM)

```python
def test_string_methods():
    """Тест методів рядків."""
    text = "Python Testing"
    
    # TODO: Додайте assertions для:
    # - startswith("Python")
    # - endswith("Testing")
    # - contains "Test"
    # - split() дає 2 слова
    # - lower() дає "python testing"
```

---

## Exercise 6: Create Test File Structure (HARD)

Створіть повну структуру:

```
my_project/
├── src/
│   ├── __init__.py
│   └── math_operations.py  # add, subtract, multiply, divide
└── tests/
    ├── __init__.py
    └── test_math_operations.py  # тести для всіх функцій
```

Напишіть мінімум 8 тестів (по 2 на кожну функцію).

---

**Run all tests:**
```bash
pytest -v
```

**Expected:** All tests should pass! ✅

