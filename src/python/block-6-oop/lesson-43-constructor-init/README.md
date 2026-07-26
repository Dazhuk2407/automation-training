# Lesson 43: Constructor (`__init__`)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Писати `__init__` для ініціалізації об'єкта
- ✅ Передавати параметри при створенні об'єкта
- ✅ Призначати атрибути екземпляра через `self`
- ✅ Використовувати значення за замовчуванням у `__init__`
- ✅ Розуміти, коли `__init__` викликається автоматично

---

## 📋 Передумови

Ви вже знаєте:
- Класи та об'єкти (Lesson 42)
- Default parameters (Lesson 28)

---

## 📖 Теорія

### 1. Навіщо `__init__`

`__init__` — це **конструктор** (точніше, ініціалізатор). Python викликає його **автоматично** одразу після створення об'єкта, щоб задати початковий стан.

Без `__init__` довелося б призначати атрибути вручну після створення:

```python
class User:
    pass

u = User()
u.name = "Alice"   # ручна ініціалізація — легко забути атрибут
u.role = "admin"
```

З `__init__` стан задається в одному місці, і **жоден об'єкт не буде створено без потрібних даних**:

```python
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

u = User("Alice", "admin")   # __init__ викликається автоматично
```

---

### 2. Базовий `__init__`

Найпростіший конструктор приймає один параметр і зберігає його як атрибут:

```python
class User:
    def __init__(self, name):
        self.name = name

u = User("Alice")   # Python сам викликає User.__init__(u, "Alice")
print(u.name)        # Alice
```

- `self` — це сам створюваний об'єкт (передається автоматично).
- `name` — параметр, який ми передаємо у дужках при створенні.
- `self.name = name` — зберігає значення в **атрибуті екземпляра**.

---

### 3. Кілька параметрів і атрибутів

`__init__` може приймати скільки завгодно параметрів:

```python
class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

u = User("Alice", "alice@example.com", "admin")
print(u.email)   # alice@example.com
print(u.role)     # admin
```

Кожен атрибут — окрема змінна об'єкта, доступна через `self` всередині класу і через об'єкт зовні (`u.role`).

---

### 4. Значення за замовчуванням

Параметри `__init__` підкоряються тим самим правилам, що й звичайні функції (Lesson 28). Можна задати значення за замовчуванням:

```python
class User:
    def __init__(self, name, active=True):
        self.name = name
        self.active = active

a = User("Alice")            # active=True за замовчуванням
b = User("Bob", active=False)

print(a.active)   # True
print(b.active)    # False
```

Параметри зі значеннями за замовчуванням мають йти **після** обов'язкових.

---

### 5. `__init__` НЕ повертає значення

`__init__` завжди повертає `None`. Його завдання — **змінити** `self`, а не повернути об'єкт. Спроба повернути щось інше призведе до помилки при створенні.

```python
class User:
    def __init__(self, name):
        self.name = name
        # return self.name   # ❌ TypeError при User("Alice")
```

Порівняння: **без** `__init__` vs **з** ним:

```python
# Без __init__ — об'єкт "порожній"
class Empty:
    pass

e = Empty()
# print(e.name)   # ❌ AttributeError — атрибута не існує


# З __init__ — стан гарантовано заданий
class Ready:
    def __init__(self, name):
        self.name = name

r = Ready("Alice")
print(r.name)   # ✅ Alice
```

---

### 6. Обчислені (похідні) атрибути

В `__init__` можна не лише зберігати аргументи, а й **обчислювати** нові атрибути на їх основі:

```python
class TestReport:
    def __init__(self, passed, failed):
        self.passed = passed
        self.failed = failed
        self.total = passed + failed                       # похідний атрибут
        self.success_rate = passed / self.total if self.total else 0.0

r = TestReport(passed=8, failed=2)
print(r.total)          # 10
print(r.success_rate)   # 0.8
```

Похідні атрибути обчислюються один раз при створенні об'єкта.

---

### 7. `__init__` у QA automation

Класи з `__init__` — основа тестових моделей та клієнтів API:

```python
class TestUser:
    def __init__(self, name, role, active=True):
        self.name = name
        self.role = role
        self.active = active


class ApiClient:
    def __init__(self, base_url, timeout=30):
        self.base_url = base_url
        self.timeout = timeout
        self.session_headers = {"Accept": "application/json"}


user = TestUser("Alice", "admin")
client = ApiClient("https://api.example.com")

print(user.role)         # admin
print(client.timeout)    # 30 (за замовчуванням)
```

Такий підхід дає **готові до використання** тестові дані з передбачуваним станом.

---

## ⚠️ Типові помилки

### Забути `self.`

```python
class User:
    def __init__(self, name):
        name = name        # ❌ локальна змінна, атрибут НЕ створено

class User:
    def __init__(self, name):
        self.name = name   # ✅ атрибут екземпляра
```

### `return` у `__init__`

```python
class User:
    def __init__(self, name):
        self.name = name
        return self        # ❌ TypeError: __init__ should return None

class User:
    def __init__(self, name):
        self.name = name   # ✅ нічого не повертаємо
```

### Mutable default (list) як параметр

Та сама пастка, що й у Lesson 28: змінюваний об'єкт за замовчуванням спільний для всіх екземплярів.

```python
class TestSuite:
    def __init__(self, tests=[]):     # ❌ один список на всі об'єкти
        self.tests = tests

class TestSuite:
    def __init__(self, tests=None):   # ✅ безпечний патерн
        self.tests = tests if tests is not None else []
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-44-instance-and-class-methods`
