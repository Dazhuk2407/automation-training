# Lesson 3: First Test File

## 🎯 Learning Outcomes

- ✅ Створити перший тестовий файл
- ✅ Розуміти структуру test файлу
- ✅ Написати простий тест
- ✅ Запустити перший тест
- ✅ Зрозуміти pass/fail результати

---

## 📖 Теорія

### 1. Структура Тестового Файлу

Тестовий файл в pytest має просту структуру:

```python
# tests/test_basic.py

def test_simple_addition():
    """Тест додавання двох чисел."""
    result = 2 + 2
    assert result == 4
```

**Ключові моменти:**
- Файл починається з `test_` або закінчується на `_test.py`
- Функції тестів починаються з `test_`
- Використовуємо `assert` для перевірок

---

### 2. Перший Простий Тест

```python
# tests/test_calculator.py

def test_addition():
    """Тест що 2 + 2 = 4."""
    assert 2 + 2 == 4

def test_subtraction():
    """Тест що 5 - 3 = 2."""
    assert 5 - 3 == 2

def test_multiplication():
    """Тест що 3 * 4 = 12."""
    assert 3 * 4 == 12
```

---

### 3. Запуск Першого Тесту

```bash
# Запустити всі тести
pytest

# Запустити конкретний файл
pytest tests/test_calculator.py

# Запустити з детальним виводом
pytest -v tests/test_calculator.py
```

**Вивід:**
```
tests/test_calculator.py::test_addition PASSED      [33%]
tests/test_calculator.py::test_subtraction PASSED   [66%]
tests/test_calculator.py::test_multiplication PASSED [100%]

===================== 3 passed in 0.02s =====================
```

---

### 4. Тест з Функцією

```python
# src/calculator.py
def add(a, b):
    """Додати два числа."""
    return a + b

def subtract(a, b):
    """Відняти b від a."""
    return a - b
```

```python
# tests/test_calculator.py
from src.calculator import add, subtract

def test_add_positive_numbers():
    """Тест додавання позитивних чисел."""
    result = add(3, 5)
    assert result == 8

def test_add_negative_numbers():
    """Тест додавання негативних чисел."""
    result = add(-3, -5)
    assert result == -8

def test_subtract():
    """Тест віднімання."""
    result = subtract(10, 4)
    assert result == 6
```

---

### 5. Що Робить Assert?

`assert` перевіряє умову. Якщо умова `False` - тест fails:

```python
def test_example():
    x = 10
    assert x == 10    # ✅ PASS - умова True
    assert x > 5      # ✅ PASS - умова True
    assert x < 20     # ✅ PASS - умова True
    # assert x == 20  # ❌ FAIL - умова False
```

---

### 6. Перший Failing Тест

```python
def test_intentional_fail():
    """Цей тест навмисно падає."""
    result = 2 + 2
    assert result == 5  # ❌ FAIL: assert 4 == 5
```

**Вивід:**
```
tests/test_example.py::test_intentional_fail FAILED [100%]

===================== FAILURES =====================
___________ test_intentional_fail ___________

    def test_intentional_fail():
        result = 2 + 2
>       assert result == 5
E       assert 4 == 5

tests/test_example.py:4: AssertionError
```

---

### 7. Docstrings в Тестах

```python
def test_example():
    """
    Опис тесту - що він перевіряє.
    
    Given: Вхідні дані
    When: Що робимо
    Then: Очікуваний результат
    """
    # Arrange
    x = 10
    
    # Act
    result = x * 2
    
    # Assert
    assert result == 20
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`
