# Lesson 13: Shared Fixtures у conftest.py

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розуміти призначення `conftest.py` — спільні фікстури без імпорту
- ✅ Оголошувати фікстуру у `conftest.py` і використовувати її в тестах теки **БЕЗ** `import`
- ✅ Розуміти область дії `conftest.py` (тека + усі підтеки)
- ✅ Розуміти, що локальна фікстура може перекрити conftest-фікстуру
- ✅ Організовувати спільний setup для набору тестів

---

## 📋 Передумови

Ви вже знаєте:
- Що таке фікстури та `@pytest.fixture` (Lesson 9)
- Як фікстура повертає дані у тест через аргумент (Lesson 9-10)
- Що таке `scope` фікстури: `function`, `module`, `session` (Lesson 11-12)

Тепер ми розберемо, **де зберігати спільні фікстури**, щоб їх бачили одразу багато тестових файлів.

---

## 📖 Теорія

### 1. Проблема: та сама фікстура потрібна багатьом файлам

Уявіть, що у вас три тестові файли, і кожному потрібен той самий тестовий користувач:

```python
# test_login.py
@pytest.fixture
def sample_user():
    return {"name": "Alice", "role": "admin"}

# test_profile.py
@pytest.fixture
def sample_user():          # ❌ копія тієї самої фікстури
    return {"name": "Alice", "role": "admin"}

# test_permissions.py
@pytest.fixture
def sample_user():          # ❌ ще одна копія
    return {"name": "Alice", "role": "admin"}
```

Це дублювання: змінили дані в одному місці — треба пам'ятати про решту. Потрібен **один спільний дім** для таких фікстур.

---

### 2. conftest.py — pytest знаходить фікстури тут БЕЗ import

`conftest.py` — це спеціальний файл, який pytest **автоматично** підхоплює. Усі фікстури, оголошені в ньому, доступні тестам як аргументи — **без жодного `import`**.

```python
# conftest.py
import pytest

@pytest.fixture
def sample_user():
    return {"name": "Alice", "role": "admin"}
```

```python
# test_login.py — той самий каталог, БЕЗ import
def test_role(sample_user):
    assert sample_user["role"] == "admin"
```

Pytest сам зіставляє ім'я аргументу `sample_user` з фікстурою з `conftest.py`. Ви **ніколи** не пишете `from conftest import sample_user`.

**Чому так?** `conftest.py` — це механізм самого pytest для збору фікстур та плагінів. Він працює на рівні collection, а не звичайного імпорту Python.

---

### 3. Область дії: conftest.py діє на свою теку і всі підтеки

`conftest.py` видно тільки в тій теці, де він лежить, **та в усіх її підтеках**. Тести з сусідніх (паралельних) тек його не бачать.

```
tests/
├── conftest.py            # фікстури видно ВСЮДИ нижче
├── test_smoke.py          # ✅ бачить фікстури з tests/conftest.py
├── api/
│   ├── conftest.py        # фікстури тільки для api/ та нижче
│   └── test_api.py        # ✅ бачить tests/conftest.py + tests/api/conftest.py
└── ui/
    └── test_ui.py         # ✅ бачить tests/conftest.py, ❌ НЕ бачить api/conftest.py
```

Правило просте: **чим ближче `conftest.py` до тесту вгору по дереву, тим він видніший.** Тест бачить усі `conftest.py` на шляху від себе до кореня проєкту.

---

### 4. Приклад: sample_user у сусідньому файлі

```python
# conftest.py
import pytest

@pytest.fixture
def sample_user():
    return {"name": "Alice", "role": "admin"}
```

```python
# test_user.py — поряд, БЕЗ import
def test_user_name(sample_user):
    assert sample_user["name"] == "Alice"

def test_user_is_admin(sample_user):
    assert sample_user["role"] == "admin"
```

Обидва тести отримають **свіжу** копію `sample_user` (scope за замовчуванням — `function`), і жоден рядок `import` не потрібен.

---

### 5. Перекриття: локальна фікстура має пріоритет над conftest

Якщо у тестовому файлі оголосити фікстуру з **тим самим ім'ям**, що й у `conftest.py`, — виграє локальна. Це називають **override**.

```python
# conftest.py
@pytest.fixture
def sample_user():
    return {"name": "Alice", "role": "admin"}
```

```python
# test_special.py
import pytest

@pytest.fixture
def sample_user():                        # перекриває conftest-фікстуру
    return {"name": "Bob", "role": "guest"}

def test_local_wins(sample_user):
    assert sample_user["name"] == "Bob"   # ✅ локальна версія
```

Це зручно, коли **більшості** тестів підходить спільна фікстура, а одному файлу потрібен особливий випадок. Ви перекриваєте фікстуру локально, не чіпаючи `conftest.py`.

---

### 6. У QA: conftest.py для всього набору тестів

На реальних проєктах у `conftest.py` виносять усе, що потрібно багатьом тестам:

```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def config():
    return {"base_url": "https://api.example.com", "timeout": 5}

@pytest.fixture
def client(config):
    # у реальності — requests.Session() або тестовий клієнт застосунку
    return {"base_url": config["base_url"], "session_id": "abc-123"}

@pytest.fixture
def test_data():
    return {"user": {"name": "Alice"}, "product": {"id": 42, "price": 9.99}}
```

Тепер будь-який `test_*.py` у теці просто просить `client`, `config` чи `test_data` як аргумент — і отримує готовий об'єкт. Один центр налаштувань замість копіпасти по десятках файлів.

---

## ⚠️ Типові помилки

### import фікстури з conftest

```python
# ❌ Так НЕ треба — pytest сам знайде фікстуру
from conftest import sample_user

def test_user(sample_user):
    ...

# ✅ Просто попросіть її як аргумент
def test_user(sample_user):
    assert sample_user["role"] == "admin"
```

### conftest.py не в тій теці

```
# ❌ conftest лежить збоку — тести його не бачать
project/
├── fixtures/conftest.py      # тести в tests/ НЕ побачать ці фікстури
└── tests/test_login.py

# ✅ conftest у теці з тестами (або вище по дереву)
project/
└── tests/
    ├── conftest.py           # видно всім тестам у tests/
    └── test_login.py
```

### Дублювати фікстуру замість винести в conftest

```python
# ❌ Однакова фікстура скопійована у кожен файл
# test_a.py, test_b.py, test_c.py — усюди той самий sample_user

# ✅ Одна фікстура у conftest.py, файли просто її використовують
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-14-fixture-best-practices`
