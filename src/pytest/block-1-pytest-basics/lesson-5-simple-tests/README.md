# Lesson 5: Simple Tests

## 🎯 Learning Outcomes

- ✅ Писати тести для чисел (integers, floats)
- ✅ Писати тести для рядків (strings)
- ✅ Писати тести для списків (lists)
- ✅ Використовувати різні patterns assertions
- ✅ Розуміти типи перевірок

---

## 📖 Теорія

### 1. Testing Numbers

#### Integers (Цілі числа)

```python
def test_integers():
    """Тести для цілих чисел."""
    # Рівність
    assert 10 == 10
    assert 2 + 2 == 4
    
    # Порівняння
    assert 5 < 10
    assert 15 > 10
    assert 10 <= 10
    assert 10 >= 10
    
    # Нерівність
    assert 5 != 10


def test_integer_operations():
    """Тести математичних операцій."""
    assert 10 + 5 == 15
    assert 10 - 3 == 7
    assert 4 * 5 == 20
    assert 10 / 2 == 5
    assert 10 // 3 == 3  # ціле ділення
    assert 10 % 3 == 1   # остача
```

#### Floats (Дробові числа)

```python
def test_floats():
    """Тести для float чисел."""
    # ⚠️ ПРОБЛЕМА: float precision
    # assert 0.1 + 0.2 == 0.3  # ❌ FAIL!
    
    # ✅ ПРАВИЛЬНО: використовувати tolerance
    result = 0.1 + 0.2
    expected = 0.3
    assert abs(result - expected) < 0.0001
    
    # Або pytest.approx
    import pytest
    assert 0.1 + 0.2 == pytest.approx(0.3)
```

---

### 2. Testing Strings

```python
def test_string_equality():
    """Тест рівності рядків."""
    name = "pytest"
    assert name == "pytest"
    assert name != "Pytest"  # case sensitive


def test_string_methods():
    """Тест методів рядків."""
    text = "Hello World"
    
    assert text.upper() == "HELLO WORLD"
    assert text.lower() == "hello world"
    assert text.capitalize() == "Hello world"
    assert text.title() == "Hello World"


def test_string_contains():
    """Тест перевірки вмісту."""
    text = "pytest testing framework"
    
    assert "pytest" in text
    assert "test" in text
    assert "Java" not in text


def test_string_startswith_endswith():
    """Тест початку та кінця рядка."""
    url = "https://example.com"
    
    assert url.startswith("https://")
    assert url.endswith(".com")
    assert not url.startswith("http://")


def test_string_length():
    """Тест довжини рядка."""
    password = "MyPassword123"
    
    assert len(password) >= 8  # мінімум 8 символів
    assert len(password) <= 20  # максимум 20 символів
```

---

### 3. Testing Lists

```python
def test_list_basics():
    """Базові тести списків."""
    numbers = [1, 2, 3, 4, 5]
    
    assert len(numbers) == 5
    assert numbers[0] == 1
    assert numbers[-1] == 5
    assert numbers[1:3] == [2, 3]


def test_list_membership():
    """Тест належності елементів."""
    fruits = ["apple", "banana", "cherry"]
    
    assert "apple" in fruits
    assert "banana" in fruits
    assert "orange" not in fruits


def test_list_operations():
    """Тест операцій зі списками."""
    numbers = [1, 2, 3]
    
    # Додавання
    numbers.append(4)
    assert numbers == [1, 2, 3, 4]
    
    # Видалення
    numbers.remove(2)
    assert numbers == [1, 3, 4]
    
    # Довжина
    assert len(numbers) == 3


def test_list_sorting():
    """Тест сортування."""
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    
    sorted_asc = sorted(numbers)
    assert sorted_asc == [1, 1, 2, 3, 4, 5, 6, 9]
    
    sorted_desc = sorted(numbers, reverse=True)
    assert sorted_desc == [9, 6, 5, 4, 3, 2, 1, 1]


def test_empty_list():
    """Тест порожнього списку."""
    empty = []
    
    assert len(empty) == 0
    assert not empty  # порожній список = False
    assert empty == []
```

---

### 4. Testing Dictionaries

```python
def test_dict_basics():
    """Базові тести словників."""
    user = {"name": "Alice", "age": 25}
    
    assert user["name"] == "Alice"
    assert user["age"] == 25
    assert len(user) == 2


def test_dict_keys():
    """Тест ключів словника."""
    config = {"debug": True, "port": 8080}
    
    assert "debug" in config
    assert "host" not in config
    assert list(config.keys()) == ["debug", "port"]


def test_dict_values():
    """Тест значень словника."""
    scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
    
    assert scores["Alice"] > 90
    assert max(scores.values()) == 95
    assert min(scores.values()) == 87
```

---

### 5. Testing Tuples and Sets

```python
def test_tuples():
    """Тест кортежів."""
    coords = (10, 20)
    
    assert len(coords) == 2
    assert coords[0] == 10
    assert coords[1] == 20


def test_sets():
    """Тест множин."""
    unique_numbers = {1, 2, 3, 3, 4, 4, 5}
    
    assert len(unique_numbers) == 5  # дублікати видалені
    assert 3 in unique_numbers
    assert 6 not in unique_numbers
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

