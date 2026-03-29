# Lesson 5: Прості тести для базових типів

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Писати тести для чисел (int, float)
- ✅ Писати тести для рядків
- ✅ Писати тести для колекцій (list, dict, set, tuple)
- ✅ Правильно порівнювати float через `pytest.approx`
- ✅ Тестувати edge cases окремими тестами

---

## 📋 Передумови

Ви вже знаєте:
- Як створити проєкт з `src/` та `tests/` (Lesson 2-3)
- Як pytest знаходить тести (Lesson 4)
- Що таке `assert` та як читати вивід pytest (Lesson 0)

Тепер ми навчимось писати тести для різних типів даних Python.

---

## 📖 Теорія

### 1. Тестування чисел

#### Цілі числа (int)

```python
def test_add():
    assert 2 + 3 == 5

def test_comparison():
    assert 10 > 5
    assert 10 >= 10
    assert 3 != 7
```

#### Дробові числа (float) — обережно!

```python
import pytest

# ❌ НЕБЕЗПЕЧНО — float precision
# assert 0.1 + 0.2 == 0.3  # FAIL! 0.30000000000000004 != 0.3

# ✅ ПРАВИЛЬНО — pytest.approx
def test_float_sum():
    assert 0.1 + 0.2 == pytest.approx(0.3)

def test_pi():
    assert 22 / 7 == pytest.approx(3.14, abs=0.01)
```

`pytest.approx` — стандартний спосіб порівнювати float у pytest.

---

### 2. Тестування рядків

```python
def test_equality():
    assert "hello" == "hello"
    assert "Hello" != "hello"  # регістр має значення

def test_contains():
    text = "pytest testing framework"
    assert "pytest" in text
    assert "Java" not in text

def test_starts_ends():
    url = "https://example.com"
    assert url.startswith("https://")
    assert url.endswith(".com")

def test_methods():
    assert "hello".upper() == "HELLO"
    assert "  spaces  ".strip() == "spaces"
    assert "a,b,c".split(",") == ["a", "b", "c"]
```

---

### 3. Тестування списків

```python
def test_basics():
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert numbers[0] == 1
    assert numbers[-1] == 5

def test_membership():
    fruits = ["apple", "banana", "cherry"]
    assert "apple" in fruits
    assert "orange" not in fruits

def test_sorting():
    assert sorted([3, 1, 2]) == [1, 2, 3]
    assert sorted([3, 1, 2], reverse=True) == [3, 2, 1]
```

---

### 4. Тестування словників

```python
def test_access():
    user = {"name": "Alice", "age": 25}
    assert user["name"] == "Alice"
    assert user.get("phone") is None  # безпечний доступ

def test_keys():
    config = {"debug": True, "port": 8080}
    assert "debug" in config
    assert "host" not in config
```

---

### 5. Тестування множин та кортежів

```python
def test_set_removes_duplicates():
    unique = {1, 2, 3, 3, 4, 4}
    assert len(unique) == 4
    assert 3 in unique

def test_tuple():
    point = (10, 20)
    assert point[0] == 10
    assert len(point) == 2
```

---

### 6. Принцип: один тест — одна ідея

```python
# ❌ ПОГАНО — один тест перевіряє все
def test_everything():
    assert 2 + 2 == 4
    assert "hello".upper() == "HELLO"
    assert len([1, 2, 3]) == 3
    assert {"a": 1}["a"] == 1

# ✅ ДОБРЕ — окремі тести для окремих речей
def test_addition():
    assert 2 + 2 == 4

def test_upper():
    assert "hello".upper() == "HELLO"

def test_list_length():
    assert len([1, 2, 3]) == 3
```

**Чому це важливо:**
- Якщо `test_everything` впаде на рядку 3, ви не дізнаєтесь чи рядки 4+ працюють
- 5 простих тестів краще дебажити ніж 1 великий
- У виводі pytest видно яка саме перевірка впала

---

## ⚠️ Типові помилки

### Float через `==`

```python
# ❌ Може впасти
assert 0.1 + 0.2 == 0.3

# ✅ Використовуйте pytest.approx
assert 0.1 + 0.2 == pytest.approx(0.3)
```

### Занадто багато assert в одному тесті

```python
# ❌ Якщо assert #2 впаде, #3-#5 не виконаються
def test_all():
    assert func_a()  # 1
    assert func_b()  # 2 ← впав тут
    assert func_c()  # 3 ← не виконається
```

### Мутація списку між перевірками

```python
# ❌ Список змінився — наступні assert неочевидні
def test_list():
    items = [1, 2, 3]
    items.append(4)
    assert len(items) == 4
    items.remove(2)          # тепер [1, 3, 4]
    assert items[1] == 3     # чому 3, а не 2?

# ✅ Краще окремо
def test_append():
    items = [1, 2, 3]
    items.append(4)
    assert items == [1, 2, 3, 4]

def test_remove():
    items = [1, 2, 3]
    items.remove(2)
    assert items == [1, 3]
```

### Очікування порядку в set

```python
# ❌ set не гарантує порядок
assert list({3, 1, 2}) == [1, 2, 3]  # може впасти!

# ✅ Порівнюйте множини з множинами
assert {3, 1, 2} == {1, 2, 3}
```

### `in` для рядка vs `in` для колекції

```python
# "in" для рядка — шукає підрядок
assert "test" in "pytest"      # True (підрядок)

# "in" для списку — шукає точний елемент
assert "test" in ["pytest"]    # False! "test" != "pytest"
assert "pytest" in ["pytest"]  # True
```

### Сортування змішаних типів

```python
# ❌ Python 3 не сортує змішані типи
# sorted([1, "a", 2])  # TypeError!

# ✅ Сортуйте лише однотипні дані
assert sorted([3, 1, 2]) == [1, 2, 3]
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-6-assertions` — детальніше про assertions