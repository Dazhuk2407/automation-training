# Lesson 14: Fixture Best Practices

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Писати **ізольовані** фікстури (тести не впливають один на одного)
- ✅ Обирати **мінімальний scope**, який вирішує задачу
- ✅ Давати фікстурам зрозумілі імена та **одну відповідальність**
- ✅ Розуміти небезпеку `autouse=True`
- ✅ Уникати спільного мутабельного стану між тестами

---

## 📋 Передумови

Ви вже знаєте:
- Як створювати фікстури та передавати їх у тести (Lesson 9-10)
- Що таке `scope` фікстури: `function`, `class`, `module`, `session` (Lesson 12)
- Як виносити спільні фікстури у `conftest.py` (Lesson 13)

Тепер ми розберемо **як писати фікстури правильно**: щоб тести залишались надійними, читабельними та незалежними.

---

## 📖 Теорія

### 1. Ізоляція — головний принцип

Кожен тест має бути **незалежним**: результат тесту не повинен залежати від того, які тести виконувались до нього. Фікстура function-scope створюється **заново для кожного тесту** — це дає свіжі дані за замовчуванням.

```python
import pytest

@pytest.fixture
def sample_user():
    # Свіжий словник для КОЖНОГО тесту
    return {"name": "Alice", "roles": ["viewer"]}

def test_add_role(sample_user):
    sample_user["roles"].append("admin")
    assert sample_user["roles"] == ["viewer", "admin"]

def test_roles_are_fresh(sample_user):
    # Не бачить змін з попереднього тесту — фікстура створена заново
    assert sample_user["roles"] == ["viewer"]
```

**Чому це важливо?** Ізольовані тести можна запускати в будь-якому порядку, паралельно, поодинці. Якщо тест падає — причина саме в ньому, а не у «сусіді».

---

### 2. Мінімальний scope

Беріть **найвужчий scope, який працює** — за замовчуванням це `function`. Розширюйте scope (`module`, `session`) лише коли ресурс **дорогий** у створенні (з'єднання з БД, запуск сервера, читання великого файлу).

```python
import pytest

# ✅ Дешеві дані → function-scope (свіжі для кожного тесту)
@pytest.fixture
def cart():
    return []

# ✅ Дорогий ресурс → ширший scope, створюємо ОДИН раз
@pytest.fixture(scope="session")
def db_engine():
    engine = connect_to_test_db()   # дорого
    yield engine
    engine.close()
```

**Правило:** ширший scope = швидше, але **більший ризик** спільного стану. Розширюйте свідомо, лише для незмінних (read-only) або дорогих ресурсів.

---

### 3. Одна відповідальність

Фікстура має готувати **одну** річ. Складні сценарії **компонуйте** з менших фікстур, а не пишіть один «комбайн».

```python
import pytest

# ✅ Кожна фікстура робить одну річ
@pytest.fixture
def user():
    return {"id": 1, "name": "Alice"}

@pytest.fixture
def client(user):
    return {"user": user, "base_url": "https://example.test"}

@pytest.fixture
def authed_session(client):
    return {"client": client, "token": "session-abc"}   # фейковий токен-приклад
```

Кожна фікстура **бере** попередню як аргумент і **додає** один шар. Тест просить лише те, що йому потрібно.

---

### 4. Зрозумілі імена

Ім'я фікстури має пояснювати **що саме** вона повертає. `data`, `obj`, `thing` — нічого не говорять.

```python
# ❌ Незрозуміло
@pytest.fixture
def data():
    return {"name": "Bob", "role": "admin"}

# ✅ Зрозуміло з першого погляду
@pytest.fixture
def sample_admin_user():
    return {"name": "Bob", "role": "admin"}
```

Коли тест виглядає як `def test_x(sample_admin_user):` — одразу видно, з чим він працює.

---

### 5. `autouse=True` — обережно

Фікстура з `autouse=True` застосовується **автоматично до всіх тестів** у своїй області, навіть якщо тест її не просить. Це «прихована магія»: тест може мати побічні ефекти, яких не видно у його сигнатурі.

```python
import pytest

@pytest.fixture(autouse=True)
def reset_config():
    # Виконується перед КОЖНИМ тестом автоматично
    config = {"debug": False}
    yield config
    # прибирання після тесту
```

**Коли доречно:** технічне прибирання/скидання стану, яке справді потрібне всім тестам (очистити кеш, скинути seed).

**Небезпека:** якщо `autouse` робить щось нетривіальне, читач тесту не розуміє, звідки береться поведінка. Використовуйте **рідко** й лише для очевидного housekeeping. У решті випадків — явно передавайте фікстуру в тест.

---

### 6. Уникай мутабельного спільного стану

Найгірша комбінація: **широкий scope** + **мутабельний об'єкт**, який тести змінюють. Тоді тести починають «бачити» зміни один одного, і порядок запуску впливає на результат.

```python
import pytest

# ❌ НЕБЕЗПЕЧНО: один список на весь модуль, тести його мутують
@pytest.fixture(scope="module")
def shared_items():
    return []

def test_a(shared_items):
    shared_items.append("a")
    assert len(shared_items) == 1   # ок першим

def test_b(shared_items):
    shared_items.append("b")
    assert len(shared_items) == 1   # ❌ впаде: список вже містить "a"
```

```python
# ✅ БЕЗПЕЧНО: function-scope дає свіжий список кожному тесту
@pytest.fixture
def items():
    return []
```

Якщо потрібен ширший scope для швидкості — тримайте ресурс **read-only** (не мутуйте його в тестах).

---

### 7. Композиція фікстур у QA

У QA-автоматизації типовий патерн — **маленькі композовані фікстури**, що будують об'єкт шар за шаром:

```python
import pytest

@pytest.fixture
def user():
    return {"name": "Alice"}

@pytest.fixture
def client(user):
    return {"user": user, "base_url": "https://example.test"}

@pytest.fixture
def authed_session(client):
    return {"client": client, "token": "session-abc"}   # фейковий приклад, не секрет

def test_authed(authed_session):
    assert authed_session["client"]["user"]["name"] == "Alice"
```

Переваги: кожен шар тестується окремо, тести просять рівно те, що потрібно, а дублювання setup зникає.

---

## ⚠️ Типові помилки

### Фікстура-«комбайн» (робить усе одразу)

```python
# ❌ Одна фікстура створює користувача, клієнта, сесію і дані
@pytest.fixture
def everything():
    user = {"name": "Alice"}
    client = {"user": user}
    session = {"client": client, "token": "abc"}
    data = [1, 2, 3]
    return user, client, session, data

# ✅ Окремі фікстури — компонуй за потреби
@pytest.fixture
def user():
    return {"name": "Alice"}

@pytest.fixture
def client(user):
    return {"user": user}
```

### Module/session scope з мутабельним станом

```python
# ❌ Тести мутують спільний список — падіння залежить від порядку
@pytest.fixture(scope="module")
def cart():
    return []

# ✅ Function-scope — свіжий стан кожному тесту
@pytest.fixture
def cart():
    return []
```

### `autouse=True` скрізь

```python
# ❌ Прихована магія: тест не просить фікстуру, але вона діє
@pytest.fixture(autouse=True)
def seed_database():
    insert_100_rows()

# ✅ Явно там, де потрібно
def test_report(seed_database):
    ...
```

### Незрозумілі імена

```python
# ❌
@pytest.fixture
def data(): ...

# ✅
@pytest.fixture
def sample_admin_user(): ...
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-15-parametrize`
