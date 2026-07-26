# Lesson 44: Instance and Class Methods

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розрізняти методи екземпляра (`self`) і методи класу (`@classmethod`, `cls`)
- ✅ Оголошувати class methods з декоратором `@classmethod`
- ✅ Розрізняти атрибути екземпляра і атрибути класу (спільні)
- ✅ Використовувати `@classmethod` як альтернативний конструктор (factory)
- ✅ Застосовувати ці патерни у QA (напр. `from_dict`, лічильник тесткейсів)

---

## 📋 Передумови

Ви вже знаєте:
- Конструктор `__init__` (Lesson 43)
- Класи та об'єкти (Lesson 42)

---

## 📖 Теорія

### 1. Метод екземпляра — працює з self

Метод екземпляра — це звичайний метод класу. Перший параметр завжди `self` —
посилання на **конкретний об'єкт**. Через `self` метод читає і змінює стан саме
цього екземпляра:

```python
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def is_admin(self):
        """Метод екземпляра: працює зі станом self."""
        return self.role == "admin"

alice = User("Alice", "admin")
bob = User("Bob", "user")

alice.is_admin()  # True  — читає alice.role
bob.is_admin()    # False — читає bob.role
```

Виклик `alice.is_admin()` Python перетворює на `User.is_admin(alice)` —
екземпляр автоматично передається як `self`.

---

### 2. Атрибут класу vs атрибут екземпляра

**Атрибут екземпляра** створюється в `__init__` через `self.` — у кожного
об'єкта свій.

**Атрибут класу** оголошується в тілі класу — він **спільний для всіх
екземплярів**. Класичний приклад — лічильник створених об'єктів:

```python
class TestCase:
    count = 0  # атрибут класу — спільний для всіх

    def __init__(self, title):
        self.title = title       # атрибут екземпляра — свій у кожного
        TestCase.count += 1      # збільшуємо спільний лічильник

tc1 = TestCase("Login")
tc2 = TestCase("Logout")

TestCase.count  # 2 — спільний для всіх екземплярів
tc1.title       # "Login" — свій у кожного
tc2.title       # "Logout"
```

---

### 3. @classmethod і cls — метод рівня класу

`@classmethod` — це метод, який працює з **класом**, а не з екземпляром.
Перший параметр — `cls` (сам клас), а не `self`. Такий метод можна викликати
без створення об'єкта:

```python
class TestCase:
    count = 0

    def __init__(self, title):
        self.title = title
        TestCase.count += 1

    @classmethod
    def total_created(cls):
        """Метод класу: доступ до атрибута класу через cls."""
        return cls.count

TestCase("Login")
TestCase("Logout")

TestCase.total_created()  # 2 — виклик через клас, без екземпляра
```

---

### 4. classmethod як factory (альтернативний конструктор)

Найпоширеніше застосування `@classmethod` — **фабричний метод**, який створює
екземпляр іншим способом, ніж `__init__`. Всередині повертаємо `cls(...)`:

```python
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def from_dict(cls, data):
        """Альтернативний конструктор: створити User зі словника."""
        return cls(data["name"], data["role"])

data = {"name": "Alice", "role": "admin"}
alice = User.from_dict(data)  # еквівалент User("Alice", "admin")
```

Чому `cls(...)`, а не `User(...)`? Бо `cls` коректно працює зі спадкуванням —
підклас отримає екземпляр свого типу.

---

### 5. Доступ до атрибута класу через cls / ClassName

До атрибута класу можна звертатися двома способами:

```python
class TestCase:
    count = 0

    @classmethod
    def total(cls):
        return cls.count          # через cls — рекомендовано

TestCase.count      # через ім'я класу
TestCase.total()    # через cls всередині classmethod
```

`cls.count` гнучкіший: якщо метод успадкує підклас, `cls` вкаже саме на нього.

---

### 6. У QA automation

Фабричні методи і лічильники — щоденні патерни в автоматизації:

```python
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["role"])


# Розбір відповіді API у зручний об'єкт
api_response = {"name": "Bob", "role": "user"}
user = User.from_dict(api_response)
assert user.role == "user"
```

```python
class TestCase:
    count = 0  # скільки тесткейсів створено за прогін

    def __init__(self, title):
        self.title = title
        TestCase.count += 1

TestCase("Smoke: login")
TestCase("Smoke: logout")
assert TestCase.count == 2
```

---

## ⚠️ Типові помилки

### Мутація атрибута класу через екземпляр

```python
class Config:
    tags = []  # ❌ спільний список для ВСІХ екземплярів

    def __init__(self):
        self.tags.append("default")  # мутує спільний стан!

a = Config()
b = Config()
# a.tags -> ["default", "default"] — несподівано спільний стан

# ✅ Атрибут екземпляра — свій у кожного
class Config:
    def __init__(self):
        self.tags = []  # створюється в __init__
```

### Плутати self і cls

```python
class User:
    # ❌ classmethod з self замість cls
    @classmethod
    def from_dict(self, data):
        return self(data["name"], data["role"])

    # ✅ classmethod приймає cls
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["role"])
```

### Забути декоратор @classmethod

```python
class User:
    # ❌ без @classmethod: cls отримає екземпляр, а не клас
    def from_dict(cls, data):
        return cls(data["name"], data["role"])

    # ✅ з декоратором — це справжній метод класу
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["role"])
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-45-static-methods`
