# Lesson 9: Fixture Basics — що таке фікстура (`@pytest.fixture`)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розуміти що таке фікстура і навіщо вона потрібна
- ✅ Оголошувати фікстуру через декоратор `@pytest.fixture`
- ✅ Повертати значення з фікстури через `return`
- ✅ Використовувати фікстуру, передавши її ім'я як параметр тесту
- ✅ Розуміти як фікстури усувають дублювання setup-коду

---

## 📋 Передумови

Ви вже знаєте:
- Як писати перший тест (Lesson 0)
- Що таке `assert` та базові перевірки (Lesson 5, 6)

Тепер ми додамо новий інструмент — **фікстури**. Це один з наріжних каменів pytest: майже кожен реальний тест-сьют їх використовує.

---

## 📖 Теорія

### 1. Проблема: дублювання підготовки даних

Уявіть, що кільком тестам потрібен той самий об'єкт користувача. Без фікстур ми
копіюємо його підготовку (**setup**) у кожен тест:

```python
def test_user_name():
    user = {"name": "Alice", "role": "admin", "active": True}  # setup
    assert user["name"] == "Alice"

def test_user_role():
    user = {"name": "Alice", "role": "admin", "active": True}  # той самий setup
    assert user["role"] == "admin"

def test_user_active():
    user = {"name": "Alice", "role": "admin", "active": True}  # знову те саме
    assert user["active"] is True
```

Один і той самий рядок повторюється тричі. Якщо структура даних зміниться —
доведеться правити її у кожному тесті. Це джерело помилок і зайвої роботи.

---

### 2. Рішення — фікстура

**Фікстура** — це функція, яка готує дані (або ресурс) для тестів. Ми позначаємо
її декоратором `@pytest.fixture` і повертаємо значення через `return`:

```python
import pytest

@pytest.fixture
def sample_user():
    """Готує тестового користувача — один раз в одному місці."""
    return {"name": "Alice", "role": "admin", "active": True}
```

Тепер підготовка даних живе **в одному місці**. Змінили структуру — правимо лише
фікстуру, і всі тести отримають оновлені дані.

---

### 3. Використання: ім'я фікстури як параметр тесту

Щоб скористатися фікстурою, тест приймає її **ім'я як параметр**. Pytest бачить
це ім'я, знаходить фікстуру, викликає її і **автоматично підставляє** повернуте
значення:

```python
def test_user_name(sample_user):          # ← ім'я фікстури як параметр
    assert sample_user["name"] == "Alice"  # sample_user — це вже {"name": ...}

def test_user_role(sample_user):
    assert sample_user["role"] == "admin"
```

Ви **не викликаєте** `sample_user()` самі. Pytest робить це за вас — цей механізм
називається **dependency injection** (впровадження залежності).

---

### 4. Фікстура може повертати будь-що

Фікстура — звичайна функція, тож повертати вона може будь-який об'єкт: `dict`,
`list`, число, рядок, екземпляр класу.

```python
@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def pi():
    return 3.14159

@pytest.fixture
def config():
    return {"timeout": 30, "retries": 3}

def test_sum(numbers):
    assert sum(numbers) == 15

def test_pi(pi):
    assert pi > 3

def test_timeout(config):
    assert config["timeout"] == 30
```

---

### 5. Кілька тестів — свіже значення кожному

Pytest викликає фікстуру **заново для кожного тесту**, який її запитує. Тому
навіть якщо один тест змінить отримані дані, наступний тест отримає **свіжу,
незіпсовану копію**:

```python
@pytest.fixture
def items():
    return [1, 2, 3]

def test_append(items):
    items.append(4)          # цей тест міняє список
    assert items == [1, 2, 3, 4]

def test_original(items):
    assert items == [1, 2, 3]  # ✅ тут список знову свіжий — фікстура викликалась заново
```

Це важлива гарантія **ізоляції тестів**: тести не впливають один на одного.

---

### 6. Фікстури у QA

У реальних QA-проєктах фікстури готують типові речі:

| Що готує фікстура | Приклад |
|-------------------|---------|
| Тестові дані | користувач, замовлення, продукт |
| Конфігурацію | URL сервера, таймаути, ключі |
| Підготовлений об'єкт | клієнт API, з'єднання, кошик |

```python
@pytest.fixture
def api_config():
    return {"base_url": "https://api.example.com", "timeout": 30}

@pytest.fixture
def test_order():
    return {"id": 1001, "items": ["book", "pen"], "total": 25.50}

def test_base_url(api_config):
    assert api_config["base_url"].startswith("https://")

def test_order_total(test_order):
    assert test_order["total"] == 25.50
```

---

## ⚠️ Типові помилки

### Забули додати фікстуру у параметри тесту

```python
@pytest.fixture
def sample_user():
    return {"name": "Alice"}

# ❌ Тест не приймає фікстуру — sample_user невизначений
def test_name():
    assert sample_user["name"] == "Alice"   # NameError

# ✅ Передаємо ім'я фікстури як параметр
def test_name(sample_user):
    assert sample_user["name"] == "Alice"
```

### Викликають фікстуру як функцію

```python
# ❌ Не викликайте фікстуру напряму — pytest це заборонить
def test_name(sample_user):
    user = sample_user()               # помилка: fixture called directly
    assert user["name"] == "Alice"

# ✅ Параметр вже містить повернуте значення
def test_name(sample_user):
    assert sample_user["name"] == "Alice"
```

### Функція без `@pytest.fixture`

```python
# ❌ Без декоратора це звичайна функція, не фікстура
def sample_user():
    return {"name": "Alice"}

# pytest не знайде фікстуру і скаже: fixture 'sample_user' not found

# ✅ Додаємо декоратор
@pytest.fixture
def sample_user():
    return {"name": "Alice"}
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-10-using-fixtures`
