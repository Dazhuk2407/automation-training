# Lesson 6: Assertions — глибше розуміння

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Використовувати різні типи assertions усвідомлено
- ✅ Розуміти як pytest показує помилки (assert introspection)
- ✅ Правильно перевіряти типи, винятки та float
- ✅ Знати коли assert message потрібен, а коли — ні

---

## 📋 Передумови

Ви вже знаєте:
- Що таке `assert` та базові перевірки (Lesson 0, 5)
- Як писати тести для різних типів даних (Lesson 5)

Тепер ми розберемо assertions **глибше**: як вони працюють всередині pytest, коли додавати повідомлення, і як уникнути типових помилок.

---

## 📖 Теорія

### 1. Як pytest показує помилки (Assert Introspection)

Pytest **перехоплює** `assert` і показує детальну інформацію про помилку:

```python
def test_dict_comparison():
    assert {"a": 1, "b": 2} == {"a": 1, "b": 3}
```

Вивід pytest:

```
E       AssertionError: assert {'a': 1, 'b': 2} == {'a': 1, 'b': 3}
E         Differing items:
E         {'b': 2} != {'b': 3}
```

Pytest сам покаже:
- Які значення порівнювались
- Що саме відрізняється
- Повний diff для великих структур

**Це головна суперсила pytest.** У unittest потрібно писати `self.assertEqual(a, b)` щоб отримати хороший diff. У pytest достатньо `assert a == b`.

---

### 2. Boolean assertions — правильний стиль

```python
# ✅ Правильно (ідіоматичний Python)
assert condition
assert not condition
assert value is None
assert value is not None

# ❌ Надмірно (не потрібно порівнювати з True/False)
assert condition is True
assert condition is False
assert condition == True
```

**Чому?** `assert condition` вже перевіряє truthiness. Порівняння з `True`/`False` через `is` або `==` — це зайвий код, який нічого не додає.

Виняток: `assert value is None` — правильно, бо `None` — це конкретний об'єкт, і `is` тут семантично точніший за `==`.

---

### 3. Перевірка типів

```python
# ✅ Рекомендовано — isinstance
assert isinstance(x, int)
assert isinstance(x, (int, float))  # один з кількох типів

# ⚠️ Менш гнучкий — type()
assert type(x) == int
```

**Чому `isinstance` краще за `type()`?**

`isinstance` враховує наслідування:

```python
class PositiveInt(int):
    pass

x = PositiveInt(5)
assert isinstance(x, int)   # ✅ True — PositiveInt наслідує int
assert type(x) == int        # ❌ False — type це PositiveInt, не int
```

У реальних проєктах наслідування — звичайна річ. `isinstance` працює коректно в усіх випадках.

---

### 4. Assert messages — коли потрібні, а коли ні

**Pytest вже показує хороший diff.** Тому message потрібен не завжди.

```python
# Без message — pytest сам покаже "assert 5 == 10"
def test_without_message():
    result = calculate(2, 3)
    assert result == 5

# З message — додатковий контекст для складної логіки
def test_with_message():
    user = get_user(42)
    assert user is not None, "User with ID=42 should exist in test database"
```

**Коли додавати message:**
- Складна бізнес-логіка, де причина падіння неочевидна
- Перевірка передумов (preconditions)
- Тест з циклом або динамічними даними

**Коли НЕ потрібен:**
- Прості порівняння (`assert result == 5`) — pytest покаже diff
- Очевидні перевірки (`assert len(items) == 3`)

---

### 5. Assertions для винятків

```python
import pytest

def test_division_by_zero():
    """Базова перевірка винятку."""
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0

def test_error_message():
    """Перевірка тексту помилки через match (regex)."""
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")
```

---

### 6. Float assertions — pytest.approx

```python
import pytest

# ❌ Може впасти через float precision
assert 0.1 + 0.2 == 0.3

# ✅ pytest.approx — стандартний спосіб
assert 0.1 + 0.2 == pytest.approx(0.3)
assert 22 / 7 == pytest.approx(3.14, abs=0.01)
```

---

### 7. Зведена таблиця assertions

| Що перевіряємо | Assert | Приклад |
|---------------|--------|---------|
| Рівність | `==` | `assert result == 5` |
| Нерівність | `!=` | `assert result != 0` |
| Порівняння | `<` `>` `<=` `>=` | `assert age >= 18` |
| Truthiness | `assert x` / `assert not x` | `assert is_valid` |
| None | `is None` / `is not None` | `assert value is not None` |
| Належність | `in` / `not in` | `assert "a" in text` |
| Тип | `isinstance()` | `assert isinstance(x, int)` |
| Виняток | `pytest.raises()` | `with pytest.raises(ValueError):` |
| Float | `pytest.approx()` | `assert x == pytest.approx(3.14)` |

---

## ⚠️ Типові помилки

### Порівняння з True/False через `is`

```python
# ❌
assert result is True
# ✅
assert result
```

### Type через `type()` замість `isinstance`

```python
# ❌ Не враховує наслідування
assert type(x) == int
# ✅
assert isinstance(x, int)
```

### Зайві message у простих перевірках

```python
# ❌ Pytest і так покаже "assert 5 == 10"
assert result == 5, f"Expected 5 but got {result}"
# ✅ Достатньо
assert result == 5
```

### "Комбайн" — один тест на все

```python
# ❌ Якщо впаде на рядку 3, рядки 4-5 не виконаються
def test_everything():
    assert func_a() == 1
    assert func_b() == 2
    assert func_c() == 3

# ✅ Окремі тести — окрема діагностика
def test_func_a():
    assert func_a() == 1

def test_func_b():
    assert func_b() == 2
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-7-run-tests` — запуск тестів з командного рядка