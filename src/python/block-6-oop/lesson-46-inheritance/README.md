# Lesson 46: Inheritance Basics

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати підклас через `class Child(Parent)`
- ✅ Успадковувати атрибути й методи батьківського класу
- ✅ Викликати батьківський конструктор через `super().__init__()`
- ✅ Перевизначати (override) методи в підкласі
- ✅ Використовувати `isinstance()` та `issubclass()`

---

## 📋 Передумови

Ви вже знаєте:
- Конструктор `__init__` (Lesson 43)
- Методи класу (Lesson 44)
- Власні винятки наслідуються від `Exception` (Lesson 38)

---

## 📖 Теорія

### 1. Навіщо наслідування

Наслідування (inheritance) дозволяє **повторно використати** код і **спеціалізувати** поведінку.
Замість того щоб копіювати спільні атрибути й методи в кожен клас, ми виносимо їх у
**базовий** клас (base / parent), а **спеціалізовані** класи (specialized / child) лише
додають або змінюють потрібне.

Аналогія: `Vehicle` (базовий) → `Car`, `Truck` (спеціалізовані). Усі транспортні
засоби мають `speed` і метод `move()`, але вантажівка додає `cargo`.

```python
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, {self.name}"


class Admin(User):
    pass
```

`Admin` не має жодного власного рядка коду, але вже вміє все, що вміє `User`.

---

### 2. Базовий підклас: `pass` успадковує все

Найпростіший підклас нічого не додає — він просто успадковує все від батька:

```python
class Admin(User):
    pass


admin = Admin("Alice")
print(admin.name)      # "Alice"  — атрибут з User
print(admin.greet())   # "Hi, Alice"  — метод з User
```

`Admin(User)` означає «`Admin` — це різновид `User`». Об'єкт `Admin` має доступ до
всіх атрибутів і методів `User` без повторення коду.

---

### 3. `super().__init__()` — розширення конструктора

Коли підклас додає **власні** атрибути, він визначає свій `__init__`, але спочатку
викликає батьківський через `super().__init__()`, щоб не втратити атрибути батька:

```python
class User:
    def __init__(self, name):
        self.name = name


class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)   # ← ініціалізує self.name
        self.level = level        # ← новий атрибут підкласу


admin = Admin("Alice", 5)
print(admin.name)    # "Alice"  — завдяки super().__init__()
print(admin.level)   # 5
```

`super()` повертає проксі до батьківського класу, тож `super().__init__(name)`
виконує `User.__init__` для того самого об'єкта.

---

### 4. Override — перевизначення методів

Підклас може **перевизначити** (override) метод батька, оголосивши метод з тим самим
іменем. За потреби всередині можна викликати батьківську версію через `super().method()`:

```python
class User:
    def role(self):
        return "user"

    def describe(self):
        return f"role={self.role()}"


class Admin(User):
    def role(self):
        return "admin"           # повністю замінює батьківський

    def describe(self):
        base = super().describe()  # виклик батьківської версії
        return f"[ADMIN] {base}"


print(Admin().role())       # "admin"
print(Admin().describe())   # "[ADMIN] role=admin"
```

Override дозволяє спеціалізувати поведінку, а `super().method()` — розширити її,
не переписуючи заново.

---

### 5. `isinstance()` та `issubclass()`

`isinstance(obj, Class)` перевіряє, чи об'єкт є екземпляром класу **або його підкласу**:

```python
admin = Admin("Alice", 5)

isinstance(admin, Admin)   # True
isinstance(admin, User)    # True  — Admin є підкласом User
isinstance(admin, str)     # False
```

`issubclass(Child, Parent)` перевіряє відношення між **класами**:

```python
issubclass(Admin, User)    # True
issubclass(User, Admin)    # False
issubclass(Admin, Admin)   # True  — клас є підкласом самого себе
```

---

### 6. У QA automation

Наслідування — основа Page Object Model та базових тест-класів:

```python
class BaseTest:
    def setup(self):
        self.driver = "chrome-driver"

    def teardown(self):
        self.driver = None


class LoginTest(BaseTest):
    def test_login(self):
        self.setup()             # метод з BaseTest
        assert self.driver == "chrome-driver"


class BasePage:
    def __init__(self, url):
        self.url = url

    def open(self):
        return f"GET {self.url}"


class LoginPage(BasePage):
    def __init__(self):
        super().__init__("/login")   # спільна логіка з BasePage

    def submit(self):
        return "submitted"
```

`BaseTest` тримає спільний `setup`/`teardown`, а `BasePage` — спільну навігацію.
Кожна спеціалізована сторінка/тест лише додає свою логіку.

---

## ⚠️ Типові помилки

### Забути `super().__init__()`

```python
class Admin(User):
    def __init__(self, name, level):
        # ❌ немає super().__init__(name) → self.name не існує
        self.level = level

# admin.name  → AttributeError
```

```python
class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)   # ✅ атрибути батька на місці
        self.level = level
```

### Плутати override та overload

```python
# ❌ Python не має overload за сигнатурою —
#    другий метод просто ПЕРЕЗАПИСУЄ перший
class C:
    def run(self): return 1
    def run(self, x): return x   # тепер run() без аргументу впаде

# ✅ Override — це заміна методу батька в ПІДКЛАСІ
class Base:
    def run(self): return 1

class Child(Base):
    def run(self): return 2      # перевизначення, не overload
```

### Глибокі ієрархії без потреби

```python
# ❌ A → B → C → D → E заради одного методу — важко читати й підтримувати
# ✅ Тримайте ієрархію пласкою; наслідуйте лише коли є реальне «є різновидом»
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-47-oop-concepts`
