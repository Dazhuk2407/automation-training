# Lesson 10: Using Fixtures in Tests — фікстура як параметр

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Передавати фікстуру як параметр тесту
- ✅ Використовувати **кілька** фікстур в одному тесті
- ✅ Будувати фікстуру, що залежить від іншої фікстури (fixture requesting fixture)
- ✅ Розуміти, що кожен тест отримує **власний** екземпляр результату фікстури

---

## 📋 Передумови

Ви вже знаєте:
- Що таке фікстура і навіщо вона потрібна (Lesson 9)
- Як оголосити фікстуру через `@pytest.fixture`

Тепер ми навчимося **використовувати** фікстури: підставляти їх у тести за іменем, комбінувати кілька фікстур і будувати ланцюги фікстур.

---

## 📖 Теорія

### 1. Механізм: pytest підставляє фікстуру за іменем

Головна ідея: pytest дивиться на **імена параметрів** тестової функції. Для кожного параметра він шукає фікстуру з таким самим іменем, викликає її і підставляє результат.

```python
import pytest


@pytest.fixture
def username():
    return "alice"


def test_username(username):
    # pytest побачив параметр `username` → знайшов фікстуру `username`
    # → викликав її → передав результат "alice"
    assert username == "alice"
```

Ви **не викликаєте** фікстуру самі (`username()`). Ви лише пишете її ім'я як параметр — pytest робить решту.

**Ключове правило:** ім'я параметра має **точно** збігатися з іменем фікстури.

---

### 2. Кілька фікстур в одному тесті

Тест може приймати скільки завгодно фікстур — просто перелічіть їх імена як параметри.

```python
import pytest


@pytest.fixture
def user():
    return {"name": "alice", "role": "admin"}


@pytest.fixture
def config():
    return {"timeout": 30, "retries": 3}


def test_x(user, config):
    assert user["role"] == "admin"
    assert config["timeout"] == 30
```

Порядок параметрів **не має значення** — pytest шукає фікстури за іменем, а не за позицією.

---

### 3. Фікстура використовує іншу фікстуру (ланцюг фікстур)

Фікстура сама може приймати інші фікстури як параметри — точно так само, як тест. Це називається **fixture requesting fixture**.

```python
import pytest


@pytest.fixture
def base_url():
    return "https://api.example.com"


@pytest.fixture
def client(base_url):
    # фікстура `client` просить фікстуру `base_url`
    return {"url": base_url, "connected": True}


def test_client(client):
    assert client["connected"] is True
    assert client["url"].startswith("https://")
```

pytest будує **ланцюг**: щоб дати тесту `client`, він спершу створює `base_url`, потім передає його у `client`. Так можна будувати шари: `config` → `client` → `session`.

---

### 4. Порядок і незалежність: кожен тест — свіжі значення

За замовчуванням (`scope="function"`) фікстура виконується **заново для кожного тесту**. Тобто кожен тест отримує **власний** екземпляр результату.

```python
import pytest


@pytest.fixture
def cart():
    return []  # новий порожній список для КОЖНОГО тесту


def test_add_one(cart):
    cart.append("apple")
    assert len(cart) == 1


def test_cart_is_fresh(cart):
    # cart тут — НОВИЙ порожній список, попередній тест його не змінив
    assert cart == []
```

Це важлива гарантія: тести **ізольовані**. Зміни в одному тесті не «протікають» в інший.

---

### 5. У QA: `client`, що залежить від `config`

Типовий реальний патерн — багатошарова фікстура для API-тестів:

```python
import pytest


@pytest.fixture
def config():
    return {"base_url": "https://api.example.com", "timeout": 30}


@pytest.fixture
def client(config):
    # client будується НА ОСНОВІ config
    return {
        "base_url": config["base_url"],
        "timeout": config["timeout"],
        "session_id": "sess-001",
    }


def test_client_uses_config(client):
    assert client["base_url"] == "https://api.example.com"
    assert client["timeout"] == 30
```

Так налаштування (`config`) відокремлені від об'єкта, який ними користується (`client`). Змінили `config` — оновилися всі клієнти.

---

### 6. Зведена таблиця

| Що робимо | Як | Приклад |
|-----------|-----|---------|
| Одна фікстура | ім'я як параметр | `def test_x(user):` |
| Кілька фікстур | перелік імен | `def test_x(user, config):` |
| Фікстура ← фікстура | ім'я у параметрах фікстури | `def client(config):` |
| Незалежність | `scope="function"` (за замовч.) | свіжий результат на тест |

---

## ⚠️ Типові помилки

### Опечатка в імені фікстури → fixture not found

```python
@pytest.fixture
def config():
    return {"timeout": 30}

# ❌ Опечатка: `configg` — pytest не знайде фікстуру
def test_bad(configg):
    assert configg["timeout"] == 30
# E       fixture 'configg' not found

# ✅ Ім'я збігається точно
def test_good(config):
    assert config["timeout"] == 30
```

### Занадто багато фікстур в одному тесті

```python
# ❌ Тест приймає 6 фікстур — важко зрозуміти, що він перевіряє
def test_everything(user, config, client, db, cache, logger):
    ...

# ✅ Візьміть лише те, що дійсно потрібно тесту
def test_login(user, client):
    ...
```

### Спроба викликати фікстуру напряму

```python
@pytest.fixture
def user():
    return {"name": "alice"}

# ❌ Не викликайте фікстуру як звичайну функцію
def test_bad():
    u = user()   # помилка: фікстуру не можна викликати напряму
    assert u["name"] == "alice"

# ✅ Отримайте її через параметр
def test_good(user):
    assert user["name"] == "alice"
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-11-yield-fixtures`
