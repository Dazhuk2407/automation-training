# Lesson 0: Знайомство з Pytest

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Встановити pytest
- ✅ Написати тестову функцію
- ✅ Зрозуміти як працює `assert`
- ✅ Запустити тести з терміналу
- ✅ Прочитати вивід pytest (passed / failed)
- ✅ Перевірити що функція кидає помилку (`pytest.raises`)

---

## 📖 Теорія

### 1. Що таке Pytest?

Pytest — це фреймворк для тестування коду на Python. Він дозволяє перевірити, що ваш код працює правильно.

**Чому pytest, а не unittest?**

| Pytest                              | unittest                        |
|-------------------------------------|---------------------------------|
| Простий синтаксис                   | Багато boilerplate коду         |
| Звичайний `assert`                  | `self.assertEqual()`            |
| Автоматично знаходить тести        | Потрібна ручна реєстрація       |
| Зрозумілі повідомлення про помилки | Менш інформативні               |

```python
# unittest — багато зайвого коду
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

# pytest — просто і зрозуміло
def test_add():
    assert 2 + 2 == 4
```

---

### 2. Встановлення

```bash
pip install pytest
```

Перевірка:

```bash
pytest --version
```

---

### 3. Як pytest знаходить тести

Pytest автоматично шукає тести за правилами:

**Файли:**
- Назва починається з `test_` — наприклад `test_math.py`
- Або закінчується на `_test.py` — наприклад `math_test.py`

**Функції:**
- Назва починається з `test_` — наприклад `def test_addition():`

**Класи (для довідки):**
- Назва починається з `Test` — наприклад `class TestMath:`
- Методи всередині також починаються з `test_`

На цьому етапі ми будемо писати лише **функції**. Класи розглянемо пізніше.

---

### 4. Що таке Assert

`assert` — це перевірка: "Я очікую, що це правда". Якщо ні — тест падає.

```python
def test_addition():
    result = 2 + 3
    assert result == 5  # Правда — тест пройде

def test_will_fail():
    result = 2 + 3
    assert result == 10  # Неправда — тест впаде!
```

**Різні перевірки з assert:**

```python
assert value == 5          # дорівнює
assert value != 0          # не дорівнює
assert value > 0           # більше нуля
assert value is None       # є None
assert value is not None   # не None
assert "hello" in text     # містить підрядок
assert isinstance(x, int)  # перевірка типу
```

---

### 5. Запуск тестів

```bash
# Запустити всі тести в поточній папці
pytest

# Запустити конкретний файл
pytest test_example.py

# Детальний вивід (verbose)
pytest -v

# Зупинитись на першій помилці
pytest -x

# Показати print() у тестах
pytest -s

# Комбінація: детально + зупинка на помилці
pytest -v -x
```

---

### 6. Як читати вивід pytest

**Успішний тест:**
```
test_math.py::test_addition PASSED
```

**Падаючий тест:**
```
test_math.py::test_will_fail FAILED

    def test_will_fail():
        result = 2 + 3
>       assert result == 10
E       assert 5 == 10

FAILED test_math.py::test_will_fail - assert 5 == 10
```

Pytest показує:
- Який рядок впав (`>`)
- Що очікувалось і що отримали (`E`)
- Це дуже корисно для пошуку помилок!

---

### 7. Тестування винятків (pytest.raises)

Іноді потрібно перевірити, що функція **кидає помилку**:

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

`pytest.raises(ValueError)` означає: "Я очікую, що цей код кине `ValueError`". Якщо помилка не виникне — тест впаде.

Можна також перевірити текст помилки:

```python
def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

---

## ⚠️ Типові помилки новачків

| Помилка | Що відбувається |
|---------|-----------------|
| Назвали функцію `check_add()` замість `test_add()` | Pytest не знайде цей тест і просто пропустить |
| Забули написати `assert` | Тест пройде, але нічого не перевірить |
| Запустили не той файл | Pytest покаже `0 tests collected` |
| Використали `print()` замість `assert` | `print()` лише виводить текст, але не перевіряє результат |

**Правило:** якщо тест не містить `assert` або `pytest.raises` — він марний.

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

---

**Далі:** `lesson-1-install-pytest` — встановлення та налаштування pytest