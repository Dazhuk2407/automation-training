# Lesson 16: Data-Driven Testing — концепція

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розуміти ідею data-driven: логіка тесту одна, дані — окремо
- ✅ Виносити набори даних у структури (списки кортежів / список dict)
- ✅ Покривати позитивні **І** негативні кейси в одному наборі
- ✅ Давати читабельні `ids` для кожного кейса
- ✅ Розуміти переваги (масштабованість покриття) і межі (не ускладнювати)

---

## 📋 Передумови

Ви вже знаєте:
- `@pytest.mark.parametrize` — один тест на багато наборів даних (Lesson 15)
- Як писати assertions та окремі тести (Lesson 5, 6)

Тепер ми зробимо крок від *техніки* `parametrize` до *концепції* **data-driven testing**: як думати про тести, коли даних багато.

---

## 📖 Теорія

### 1. Data-driven: відокремити ЩО від НА ЧОМУ

Ідея data-driven проста: у тесті є дві різні речі, і їх треба розділити.

- **ЩО перевіряємо** — логіка тесту (виклик функції + assert). Вона одна.
- **НА ЧОМУ перевіряємо** — дані (входи + очікувані результати). Їх багато.

```python
# Логіка (ЩО) — написана один раз
def test_login(user, pwd, expected):
    assert is_valid_login(user, pwd) is expected

# Дані (НА ЧОМУ) — окремо, легко доповнити
LOGIN_CASES = [
    ("alice", "pass123", True),
    ("", "pass123", False),
    ("bob", "", False),
]
```

**Чому це важливо?** Додати новий кейс = додати рядок у список. Логіку тесту чіпати не треба. Тест стає **таблицею**, яку легко читати й розширювати.

---

### 2. Набори даних як окрема структура + parametrize

Виносьте дані у **іменовану структуру** над тестом (або в окремий модуль). Два поширені формати:

**Список кортежів** — компактно, коли полів мало:

```python
import pytest

DISCOUNT_CASES = [
    (100, 0, 100),
    (100, 10, 90),
    (100, 100, 0),
]

@pytest.mark.parametrize("price,percent,expected", DISCOUNT_CASES)
def test_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected
```

**Список словників** — самодокументований, коли полів багато:

```python
USER_CASES = [
    {"name": "Alice", "age": 30, "is_adult": True},
    {"name": "Bob", "age": 15, "is_adult": False},
]

@pytest.mark.parametrize("case", USER_CASES)
def test_is_adult(case):
    assert is_adult(case["age"]) is case["is_adult"]
```

Головне правило: **дані — це дані**. У наборі лежать готові значення, а не обчислення (див. розділ ⚠️).

---

### 3. Позитивні vs негативні кейси в одному наборі

Хороший набір даних покриває **обидва боки**:

- **Позитивні кейси** — валідний вхід, очікуємо успіх / коректний результат.
- **Негативні кейси** — невалідний вхід, очікуємо відмову / помилку / `False`.

```python
import pytest

# expected: True = валідний email, False = невалідний
EMAIL_CASES = [
    ("alice@example.com", True),   # позитивний
    ("bob@test.org", True),        # позитивний
    ("no-at-sign", False),         # негативний
    ("", False),                   # негативний
    ("@example.com", False),       # негативний
]

@pytest.mark.parametrize("email,expected", EMAIL_CASES)
def test_email_validation(email, expected):
    assert is_valid_email(email) is expected
```

**Чому це критично для QA?** Тест лише на позитивних кейсах створює *ілюзію* покриття. Баги живуть саме на невалідних входах: порожні рядки, `None`, від'ємні числа, некоректний формат.

---

### 4. Читабельні `ids` для кожного кейса

Без `ids` pytest генерує технічні назви (`test_login[alice-pass123-True]`), а для складних даних — і зовсім `test_login[case0]`. Додайте `ids`, щоб вивід читався як звіт:

```python
import pytest

LOGIN_CASES = [
    ("alice", "pass123", True),
    ("", "pass123", False),
    ("bob", "", False),
]

@pytest.mark.parametrize(
    "user,pwd,expected",
    LOGIN_CASES,
    ids=["valid_login", "empty_user", "empty_password"],
)
def test_login(user, pwd, expected):
    assert is_valid_login(user, pwd) is expected
```

Вивід стає прозорим:

```
test_login[valid_login] PASSED
test_login[empty_user] PASSED
test_login[empty_password] PASSED
```

Коли кейс падає, ви одразу бачите **який саме** — `empty_password`, а не `case2`.

---

### 5. Межі й edge cases як дані

Найцінніші кейси — на **межах**. Замість того щоб описувати їх словами, покладіть їх у набір як звичайні рядки даних:

| Категорія | Приклади входів |
|-----------|-----------------|
| Нуль / порожнє | `0`, `""`, `[]`, `{}` |
| Мінімум / максимум | `1`, `MAX_INT`, межа діапазону |
| Одразу за межею | `-1`, `MAX + 1`, `18` для "18+" |
| Спецзначення | `None`, пробіли, дуже довгий рядок |

```python
import pytest

# Правило: доступ дозволено з 18 років
AGE_CASES = [
    (17, False),   # одразу під межею
    (18, True),    # рівно на межі
    (19, True),    # над межею
    (0, False),    # нуль
]

@pytest.mark.parametrize("age,allowed", AGE_CASES)
def test_access_by_age(age, allowed):
    assert has_access(age) is allowed
```

Межі (`17` vs `18`) ловлять класичну помилку `>` замість `>=`.

---

### 6. У QA: таблиця тест-кейсів як дані

Data-driven — це природний спосіб думати для QA, бо тест-кейси й так живуть у **таблицях**. Класичний приклад — перевірка статус-кодів API:

```python
import pytest

# (шлях, метод, очікуваний статус)
API_CASES = [
    ("/users",      "GET",    200),
    ("/users/1",    "GET",    200),
    ("/users/9999", "GET",    404),
    ("/users",      "POST",   201),
    ("/admin",      "GET",    403),
]

@pytest.mark.parametrize(
    "path,method,status",
    API_CASES,
    ids=["list_ok", "get_ok", "not_found", "create_ok", "forbidden"],
)
def test_api_status(path, method, status):
    assert fake_request(path, method) == status
```

Тепер QA-інженер додає новий кейс з тест-плану одним рядком — і логіку тесту не чіпає.

---

### 7. Зведена таблиця

| Питання | Data-driven відповідь |
|---------|-----------------------|
| Де логіка тесту? | Одна функція `test_*` |
| Де дані? | Окрема іменована структура |
| Формат даних? | Список кортежів або список dict |
| Позитив і негатив? | Обидва в одному наборі |
| Як читати вивід? | Через `ids` |
| Що додати новий кейс? | +1 рядок у набір |

---

## ⚠️ Типові помилки

### Логіка в даних замість очікуваного значення

```python
# ❌ Обчислення в наборі — тест перевіряє сам себе, а не функцію
CASES = [
    (100, 10, 100 - 100 * 10 / 100),  # це логіка, не дані!
]

# ✅ Готове очікуване значення
CASES = [
    (100, 10, 90),
]
```

Якщо у наборі лежить формула — тест повторює реалізацію і не зловить у ній баг.

### Лише позитивні кейси

```python
# ❌ Тільки валідні входи — ілюзія покриття
CASES = [
    ("alice@example.com", True),
    ("bob@test.org", True),
]

# ✅ Позитив + негатив
CASES = [
    ("alice@example.com", True),
    ("no-at-sign", False),
    ("", False),
]
```

### Гігантський набір без `ids`

```python
# ❌ 50 кортежів → у виводі case0..case49, нечитабельно
@pytest.mark.parametrize("data,expected", HUGE_LIST)

# ✅ Або дайте ids, або згрупуйте у менші осмислені набори
@pytest.mark.parametrize("data,expected", CASES, ids=CASE_IDS)
```

Data-driven не означає "запхати все в один список". Читабельність важливіша за кількість.

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-17-markers`
