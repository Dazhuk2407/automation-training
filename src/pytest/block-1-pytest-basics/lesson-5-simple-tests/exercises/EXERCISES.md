# Exercises - Lesson 5: Simple Tests

## Exercise 1: Test Integer Operations (EASY)

```python
def test_basic_math():
    """Тест базової математики."""
    # TODO: Додайте assertions для:
    # 1. 5 + 3 == 8
    # 2. 10 - 4 == 6
    # 3. 3 * 4 == 12
    # 4. 10 / 2 == 5
    assert ...
```

---

## Exercise 2: Test String Operations (EASY)

```python
def test_strings():
    """Тест операцій з рядками."""
    name = "pytest"
    
    # TODO: Додайте assertions для:
    # 1. Довжина = 6
    # 2. Upper case = "PYTEST"
    # 3. Містить "test"
    # 4. Починається з "py"
    assert ...
```

---

## Exercise 3: Test List Operations (MEDIUM)

```python
def test_list_operations():
    """Тест операцій зі списками."""
    numbers = [1, 2, 3, 4, 5]
    
    # TODO: Додайте assertions для:
    # 1. Довжина = 5
    # 2. Перший елемент = 1
    # 3. Останній елемент = 5
    # 4. 3 в списку
    # 5. Слайс [1:3] = [2, 3]
    assert ...
```

---

## Exercise 4: Test Float with Precision (MEDIUM)

```python
import pytest

def test_float_precision():
    """Тест float з точністю."""
    # TODO: Додайте тест для 0.1 + 0.2 ≈ 0.3
    # Підказка: используйте pytest.approx()
    result = 0.1 + 0.2
    assert result == pytest.approx(0.3)
```

---

## Exercise 5: Test Dictionary (MEDIUM)

```python
def test_dictionary():
    """Тест словника."""
    user = {"name": "Alice", "age": 25, "email": "alice@example.com"}
    
    # TODO: Додайте assertions для:
    # 1. name == "Alice"
    # 2. age == 25
    # 3. Словник має 3 ключі
    # 4. "email" в словнику
    # 5. "phone" НЕ в словнику
    assert ...
```

---

## Exercise 6: Comprehensive Test (HARD)

Створіть файл `test_comprehensive.py` з тестами для:

```python
def test_all_types():
    """Комплексний тест всіх типів."""
    # Integer
    assert 10 + 5 == 15
    
    # String
    assert "hello".upper() == "HELLO"
    
    # List
    numbers = [1, 2, 3]
    assert len(numbers) == 3
    assert 2 in numbers
    
    # Dictionary
    data = {"key": "value"}
    assert data["key"] == "value"
    
    # Nested structures
    matrix = [[1, 2], [3, 4]]
    assert matrix[0][1] == 2
    
    # Set
    unique = {1, 2, 3}
    assert 2 in unique
```

---

## Exercise 7: Test Edge Cases (HARD)

```python
def test_edge_cases():
    """Тест граничних випадків."""
    # TODO: Тестуйте:
    # 1. Порожній список: len([]) == 0
    # 2. Отримання останнього елемента: [1,2,3][-1] == 3
    # 3. Слайс з кроком: [1,2,3,4,5][::2] == [1,3,5]
    # 4. Негативне число: abs(-10) == 10
    # 5. Boolean порівняння
    assert ...
```

---

**Run all exercises:**
```bash
pytest -v
# Expected: All tests should PASS ✅
```

