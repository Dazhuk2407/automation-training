# Exercises - Lesson 6: Assertions

## Exercise 1: Basic Assertions (EASY)

```python
def test_basic_assertions():
    """Тест основних assertions."""
    # TODO: Додайте assertions для:
    # 1. 10 == 10
    # 2. "hello" != "world"
    # 3. 5 < 10
    # 4. 5 >= 5
    assert ...
```

---

## Exercise 2: Assertions with Messages (EASY)

```python
def test_with_messages():
    """Тест assertions з повідомленнями."""
    x = 10
    y = 5
    
    # TODO: Додайте assertions з повідомленнями:
    # assert x > y, "x має бути більше y"
    # assert x != y, f"Expected {x} != {y}"
    assert ...
```

---

## Exercise 3: Membership Assertions (MEDIUM)

```python
def test_membership():
    """Тест належності елементів."""
    numbers = [1, 2, 3, 4, 5]
    text = "pytest"
    data = {"name": "Alice", "age": 25}
    
    # TODO: Додайте assertions для:
    # - 3 in numbers
    # - 10 not in numbers
    # - "test" in text
    # - "name" in data
    # - "email" not in data
    assert ...
```

---

## Exercise 4: Type Assertions (MEDIUM)

```python
def test_types():
    """Тест перевірки типів."""
    # TODO: Додайте assertions для isinstance:
    # - 5 is int
    # - "hello" is str
    # - [1,2] is list
    # - {"a":1} is dict
    # - 3.14 is float
    assert isinstance(5, int)
    assert ...
```

---

## Exercise 5: Exception Testing (HARD)

```python
import pytest

def test_exceptions():
    """Тест для виключень."""
    # TODO: Тестуйте ці виключення:
    
    # 1. ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0
    
    # 2. ValueError
    with pytest.raises(ValueError):
        int("not a number")
    
    # 3. KeyError
    with pytest.raises(KeyError):
        d = {}
        _ = d["missing"]
    
    # 4. IndexError
    with pytest.raises(IndexError):
        lst = [1, 2]
        _ = lst[10]
```

---

## Exercise 6: Collection Assertions (HARD)

```python
def test_collections():
    """Тест assertions для колекцій."""
    # TODO: Тестуйте:
    
    # Lists
    lst = [1, 2, 3]
    assert lst == [1, 2, 3]
    assert len(lst) == 3
    assert 2 in lst
    
    # Dictionaries
    user = {"name": "Alice", "age": 25}
    assert user["name"] == "Alice"
    assert len(user) == 2
    assert "name" in user
    
    # Nested
    matrix = [[1, 2], [3, 4]]
    assert matrix[0][1] == 2
```

---

## Exercise 7: Float Assertions (HARD)

```python
import pytest

def test_float_precision():
    """Тест float з точністю."""
    # TODO: Тестуйте float porівняння:
    
    # Без tolerance (може fail!)
    # assert 0.1 + 0.2 == 0.3  # ❌
    
    # З pytest.approx
    assert 0.1 + 0.2 == pytest.approx(0.3)
    
    # З абсолютною точністю
    assert 22 / 7 == pytest.approx(3.14, abs=0.01)
    
    # З відносною точністю
    assert 22 / 7 == pytest.approx(3.142857, rel=1e-5)
```

---

**Run all exercises:**
```bash
pytest exercises/ -v
# Expected: All tests PASS ✅
```

