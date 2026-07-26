# Lesson 11: Setup/Teardown з yield-фікстурами

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Писати yield-фікстуру: код до `yield` — setup, після `yield` — teardown
- ✅ Розуміти що teardown виконується ПІСЛЯ тесту навіть якщо тест впав
- ✅ Віддавати значення у тест через `yield value`
- ✅ Застосовувати yield-фікстури для ресурсів (файл, з'єднання, тимчасовий стан)
- ✅ Розуміти порядок teardown при кількох фікстурах (LIFO)

---

## 📋 Передумови

Ви вже знаєте:
- Що таке фікстури та декоратор `@pytest.fixture` (Lesson 9)
- Як використовувати фікстуру як аргумент тесту (Lesson 10)

Тепер ми додамо **прибирання після тесту** — те, чого не вміє звичайний `return`.

---

## 📖 Теорія

### 1. return vs yield

Фікстура з `return` віддає значення, і на цьому все закінчується. Немає місця для коду, який має виконатись **після** тесту.

```python
import pytest

@pytest.fixture
def data_return():
    return {"opened": True}   # тест отримає це, але прибрати нічого не можна
```

Фікстура з `yield` віддає значення через `yield`, а потім **повертає керування назад** після завершення тесту — саме там ми прибираємо за собою.

```python
import pytest

@pytest.fixture
def data_yield():
    data = {"opened": True}   # setup
    yield data                # тест працює тут
    data["opened"] = False    # teardown — виконається ПІСЛЯ тесту
```

**Головна ідея:** `yield` розбиває фікстуру на дві частини — до і після тесту.

---

### 2. Структура yield-фікстури

Кожна yield-фікстура має три логічні частини:

```python
import pytest

@pytest.fixture
def temp_data():
    data = {"opened": True}      # 1. setup — підготовка
    yield data                    # 2. тест працює тут (отримує data)
    data["opened"] = False        # 3. teardown — прибирання
```

- **setup** — усе до `yield`: створити ресурс, підготувати дані.
- **`yield value`** — віддати значення тесту; pytest «зупиняється» тут поки триває тест.
- **teardown** — усе після `yield`: закрити, очистити, повернути стан.

---

### 3. Teardown виконується гарантовано

Навіть якщо тест **впав** (assert не пройшов) — код після `yield` все одно виконається.

```python
import pytest

@pytest.fixture
def session():
    log = {"open": True}
    yield log
    log["open"] = False   # виконається навіть якщо тест впав

def test_fails_but_cleanup_runs(session):
    assert session["open"] is True
    assert 1 == 2          # тест впаде тут...
    # ...але session["open"] все одно стане False
```

Це критично для ресурсів: з'єднання буде закрито, тимчасові дані прибрані — незалежно від результату тесту. Виняток: якщо помилка сталася **у setup** (до `yield`), то teardown НЕ виконується, бо ресурс ще не був створений.

---

### 4. Порядок teardown при кількох фікстурах (LIFO)

Якщо тест використовує кілька yield-фікстур, їхній setup виконується у порядку залежностей, а teardown — у **ЗВОРОТНЬОМУ** порядку (Last In — First Out, як стек).

```python
import pytest

@pytest.fixture
def outer(events):
    events.append("outer setup")
    yield
    events.append("outer teardown")

@pytest.fixture
def inner(events, outer):
    events.append("inner setup")
    yield
    events.append("inner teardown")
```

Порядок подій:
```
outer setup   → inner setup → [тест] → inner teardown → outer teardown
```

Останній, хто налаштувався, першим прибирається. Це логічно: `inner` залежить від `outer`, тому `inner` треба прибрати раніше.

---

### 5. Практика: імітація ресурсу

Не обов'язково працювати з реальним файлом чи мережею, щоб навчитись setup/teardown. Використовуйте звичайний `list` або `dict` як «ресурс» і лічильник відкрито/закрито.

```python
import pytest

@pytest.fixture
def connection():
    conn = {"status": "open", "queries": []}   # setup: «відкрили»
    yield conn                                   # тест виконує «запити»
    conn["status"] = "closed"                    # teardown: «закрили»
```

Якщо все ж потрібен справжній файл — використовуйте вбудовану фікстуру `tmp_path`, яка дає тимчасову директорію і сама прибирає її:

```python
def test_writes_file(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("hello")
    assert file.read_text() == "hello"
```

---

### 6. yield-фікстури у QA

Типові сценарії з роботи QA-інженера:

- **Тест-дані:** створити користувача/запис перед тестом, видалити після.
- **Сесія:** «відкрити» сесію/з'єднання до тесту, «закрити» після.
- **Тимчасовий стан:** змінити конфіг для тесту, повернути оригінал після.

yield робить це чистим: setup і відповідний teardown лежать поруч, в одній фікстурі.

---

### 7. Зведена таблиця

| Частина | Де | Що робить |
|---------|-----|-----------|
| setup | до `yield` | готує ресурс/дані |
| `yield value` | посередині | віддає значення тесту |
| teardown | після `yield` | прибирає, закриває, очищає |
| порядок teardown | — | LIFO (зворотній до setup) |
| гарантія | — | teardown виконується навіть при падінні тесту |

---

## ⚠️ Типові помилки

### return замість yield — немає teardown

```python
# ❌ Прибирання не виконається — після return коду немає
@pytest.fixture
def resource():
    conn = {"status": "open"}
    return conn
    conn["status"] = "closed"   # мертвий код, ніколи не виконається

# ✅ yield дає місце для teardown
@pytest.fixture
def resource():
    conn = {"status": "open"}
    yield conn
    conn["status"] = "closed"
```

### Teardown-код ДО yield

```python
# ❌ «Прибирання» виконається до тесту — безглуздо
@pytest.fixture
def resource():
    conn = {"status": "open"}
    conn["status"] = "closed"   # закрили ще до тесту!
    yield conn

# ✅ Спочатку віддати, потім прибирати
@pytest.fixture
def resource():
    conn = {"status": "open"}
    yield conn
    conn["status"] = "closed"
```

### Покладатися на порядок teardown неявно

```python
# ❌ Припускати "мій teardown точно перший" без розуміння залежностей
# ✅ Пам'ятати правило: teardown у ЗВОРОТНЬОМУ порядку (LIFO).
#    Якщо fixture B залежить від A → B прибирається раніше за A.
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-12-fixture-scopes`
