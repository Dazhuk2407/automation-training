# Lesson 6: Assertions

## 🎯 Learning Outcomes

- ✅ Розуміти різні типи assertions
- ✅ Писати assert з повідомленнями
- ✅ Використовувати складні перевірки
- ✅ Знати best practices для assertions

---

## 📖 Теорія

### 1. Базовий Assert

```python
# Простий assert
assert True
assert 5 > 3
assert "test" in "pytest"

# Assert з повідомленням
assert 5 > 10, "5 має бути більше 10"
assert "hello" == "world", f"Очікується 'world' але отримано 'hello'"
```

**Результат при failure:**
```
AssertionError: 5 має бути більше 10
```

---

### 2. Comparison Assertions

```python
# Рівність
assert x == y
assert x != y

# Порядок
assert x < y
assert x > y
assert x <= y
assert x >= y

# Boolean
assert condition is True
assert condition is False
assert condition is None
```

---

### 3. Membership Assertions

```python
# Належність
assert element in collection
assert element not in collection

# Приклади
assert "a" in "abc"
assert 5 in [1, 2, 3, 4, 5]
assert "key" in {"key": "value"}
assert "missing" not in ["a", "b", "c"]
```

---

### 4. Type Assertions

```python
# Перевірка типу
assert isinstance(x, int)
assert isinstance(x, str)
assert isinstance(x, (int, float))  # один з кількох типів
assert type(x) == int

# Приклади
assert isinstance([1, 2, 3], list)
assert isinstance("hello", str)
assert isinstance(3.14, (int, float))
```

---

### 5. Exception Assertions

```python
import pytest

# Тестування винятків
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0

def test_value_error():
    with pytest.raises(ValueError):
        int("not a number")

# З перевіркою повідомлення
def test_error_message():
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")
```

---

### 6. List/Dict Assertions

```python
# Списки
assert [1, 2, 3] == [1, 2, 3]
assert [1, 2, 3] != [3, 2, 1]
assert 2 in [1, 2, 3]

# Словники
assert {"a": 1} == {"a": 1}
assert {"a": 1} != {"a": 2}
assert "a" in {"a": 1}

# Вкладені структури
assert {"x": [1, 2]} == {"x": [1, 2]}
assert matrix[0][1] == 2
```

---

### 7. Assert Messages

```python
def test_with_message():
    x = 5
    y = 10
    assert x > y, f"Expected {x} > {y}"
    # Error: AssertionError: Expected 5 > 10

def test_descriptive_message():
    age = 15
    assert age >= 18, (
        f"User age {age} is below minimum required age 18"
    )
```

---

### 8. Multiple Assertions

```python
def test_user_validation():
    user = {"name": "Alice", "age": 25}
    
    # Кілька перевірок
    assert user["name"] == "Alice"
    assert user["age"] == 25
    assert len(user) == 2
    
    # ⚠️ Якщо перший assert fails - інші не виконаються!
    # Для всіх перевірок краще використовувати окремі тести
```

---

### 9. Best Practices

```python
# ✅ ДОБРЕ
def test_calculation():
    result = 2 + 2
    assert result == 4, f"Expected 4 but got {result}"

# ❌ ПОГАНО
def test_many_asserts():
    """Не робіть 10+ assertions в одному тесті"""
    # ...
    assert x == 1
    assert y == 2
    assert z == 3
    # ...

# ✅ ДОБРЕ - один assert за одну речь яка тестується
def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2
```

---

### 10. Assert Operators Summary

| Оператор | Опис | Приклад |
|----------|------|---------|
| `==` | Рівність | `assert x == 5` |
| `!=` | Нерівність | `assert x != 5` |
| `<` | Менше | `assert x < 10` |
| `>` | Більше | `assert x > 0` |
| `<=` | Менше або рівно | `assert x <= 10` |
| `>=` | Більше або рівно | `assert x >= 0` |
| `in` | Містить | `assert "a" in "abc"` |
| `not in` | Не містить | `assert "x" not in "abc"` |
| `is` | Ідентичність | `assert x is True` |
| `is not` | Не ідентичність | `assert x is not None` |

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

