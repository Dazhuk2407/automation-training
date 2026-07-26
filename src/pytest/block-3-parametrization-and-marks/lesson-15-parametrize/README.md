# Lesson 15: Parametrized Tests (@pytest.mark.parametrize)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Використовувати `@pytest.mark.parametrize` для запуску одного тесту з багатьма наборами даних
- ✅ Передавати кілька параметрів одразу
- ✅ Давати читабельні `ids` для кожного тест-кейсу
- ✅ Розуміти що кожен набір даних — це окремий тест-кейс у звіті
- ✅ Уникати дублювання майже однакових тестів

---

## 📋 Передумови

Ви вже знаєте:
- Як писати `assert` та перевіряти дані (Lesson 6)
- Як працюють фікстури (Block 2)

Тепер ми навчимося запускати **один тест на багатьох даних** — без копіювання коду.

---

## 📖 Теорія

### 1. Проблема: 5 майже однакових тестів

Уявіть, що треба перевірити функцію `square(n)` на кількох входах:

```python
def test_square_2():
    assert 2 * 2 == 4

def test_square_3():
    assert 3 * 3 == 9

def test_square_4():
    assert 4 * 4 == 16

def test_square_5():
    assert 5 * 5 == 25
```

Це **дублювання**: логіка однакова, відрізняються лише числа. Якщо зміниться формула — доведеться правити кожен тест. Додати новий кейс = скопіювати ще одну функцію.

---

### 2. Рішення: `@pytest.mark.parametrize`

Один тест — багато наборів даних:

```python
import pytest

@pytest.mark.parametrize("n,expected", [(2, 4), (3, 9), (4, 16)])
def test_square(n, expected):
    assert n * n == expected
```

Перший аргумент — рядок з іменами параметрів (`"n,expected"`).
Другий аргумент — список наборів значень. Кожен кортеж `(n, expected)` стає окремим запуском.

**Результат:** один код, три перевірки. Додати кейс = додати кортеж у список.

---

### 3. Кожен набір = окремий тест у звіті

pytest розгортає параметризований тест на кілька окремих тест-кейсів:

```
test_square[2-4] PASSED
test_square[3-9] PASSED
test_square[4-16] PASSED
```

У квадратних дужках — значення параметрів. Якщо один кейс впаде — інші **все одно виконаються**, і ви побачите який саме набір даних зламався:

```
test_square[2-4] PASSED
test_square[3-8] FAILED
test_square[4-16] PASSED
```

Це велика перевага: одна функція, але діагностика така ж точна, як у окремих тестів.

---

### 4. Кілька параметрів; кортежі значень

Параметрів може бути скільки завгодно — перелічіть їх через кому в рядку імен, а значення передавайте кортежами тієї ж довжини:

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (10, 5, 15),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert a + b == expected
```

Кількість імен у рядку **має збігатися** з довжиною кожного кортежу.

---

### 5. `ids` — зрозумілі імена кейсів

За замовчуванням pytest будує id з самих значень (`[2-4]`). Для складних даних це нечитабельно. Задайте власні імена через `ids`:

```python
@pytest.mark.parametrize(
    "email,is_valid",
    [
        ("user@example.com", True),
        ("no-at-sign", False),
        ("", False),
    ],
    ids=["valid_email", "missing_at", "empty_string"],
)
def test_email(email, is_valid):
    assert ("@" in email) == is_valid
```

Тепер у звіті:

```
test_email[valid_email] PASSED
test_email[missing_at] PASSED
test_email[empty_string] PASSED
```

Довжина `ids` має дорівнювати кількості наборів даних.

---

### 6. Комбінування parametrize з фікстурами (коротко)

`parametrize` вільно поєднується з фікстурами. Просто додайте фікстуру як ще один аргумент тесту:

```python
import pytest

@pytest.fixture
def base():
    return 100

@pytest.mark.parametrize("bonus,expected", [(0, 100), (50, 150)])
def test_total(base, bonus, expected):
    assert base + bonus == expected
```

`base` приходить з фікстури, `bonus` та `expected` — з `parametrize`. Кожен набір використовує ту саму фікстуру.

---

### 7. У QA: перевірка функції на багатьох входах

Параметризація — головний інструмент data-driven тестування. Типовий набір кейсів для однієї функції:

- **Звичайні (happy path):** типові валідні входи
- **Межові (boundary):** 0, порожній рядок, мінімум/максимум, межа діапазону
- **Негативні (negative):** невалідні дані, які мають бути відхилені

```python
@pytest.mark.parametrize("age,allowed", [
    (18, True),    # межа
    (17, False),   # межа
    (25, True),    # звичайний
    (0, False),    # межа
    (-5, False),   # негативний
])
def test_can_vote(age, allowed):
    assert (age >= 18) == allowed
```

Один тест покриває весь спектр — від happy path до країв і помилок.

---

## ⚠️ Типові помилки

### Невідповідність кількості імен і значень

```python
# ❌ Два імені, але в кортежах по три значення
@pytest.mark.parametrize("a,b", [(1, 2, 3), (4, 5, 6)])
def test_bad(a, b):
    ...
# pytest: ValueError — wrong number of values

# ✅ Кількість імен = довжина кортежу
@pytest.mark.parametrize("a,b,c", [(1, 2, 3), (4, 5, 6)])
def test_ok(a, b, c):
    ...
```

### Занадто багато параметрів — нечитабельно

```python
# ❌ 6 параметрів — важко зрозуміти що є що
@pytest.mark.parametrize("a,b,c,d,e,expected", [...])

# ✅ Згрупуйте пов'язані дані або передайте dict/об'єкт
@pytest.mark.parametrize("user,expected", [
    ({"name": "Alice", "age": 30, "role": "admin"}, True),
])
```

### `parametrize` замість `fixture` там, де потрібен ресурс

```python
# ❌ parametrize для створення/прибирання ресурсу — це не його робота
@pytest.mark.parametrize("db", [create_db()])  # створює ресурс один раз при зборі
def test_query(db):
    ...

# ✅ Ресурс (БД, з'єднання, файл) — це fixture; parametrize лише для ДАНИХ
@pytest.fixture
def db():
    conn = create_db()
    yield conn
    conn.close()

@pytest.mark.parametrize("query,expected", [("SELECT 1", 1)])
def test_query(db, query, expected):
    ...
```

`parametrize` — для **вхідних даних**. `fixture` — для **ресурсів**, які треба створити й прибрати.

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-16-data-driven`
