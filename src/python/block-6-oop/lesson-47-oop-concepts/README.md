# Lesson 47: Python OOP Concepts (інкапсуляція, поліморфізм, абстракція)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Пояснити 4 стовпи ООП: encapsulation, inheritance, polymorphism, abstraction
- ✅ Застосовувати інкапсуляцію через конвенції `_protected` та `__private` (name mangling)
- ✅ Використовувати поліморфізм: однаковий інтерфейс, різна реалізація
- ✅ Розуміти абстракцію — приховати складність за простим інтерфейсом
- ✅ Використовувати `@property` для контрольованого доступу

---

## 📋 Передумови

Ви вже знаєте:
- Наслідування (Lesson 46)
- Методи класу (Lesson 44-45)

---

## 📖 Теорія

### 1. Чотири стовпи ООП — короткий огляд

ООП тримається на 4 принципах:

| Стовп | Що означає |
|-------|------------|
| **Encapsulation** (інкапсуляція) | приховати внутрішній стан, дати контрольований доступ |
| **Inheritance** (наслідування) | клас-нащадок переймає поведінку батька (вже знаємо з Lesson 46) |
| **Polymorphism** (поліморфізм) | однаковий інтерфейс — різна реалізація |
| **Abstraction** (абстракція) | сховати складність за простим інтерфейсом |

Наслідування ми вже пройшли, тож сфокусуємось на решті трьох.

---

### 2. Інкапсуляція: `_single` та `__double`

У Python немає справжніх `private`/`protected` як у Java. Замість цього — **конвенції**:

```python
class Account:
    def __init__(self, balance):
        self.owner = "public"       # публічний — можна все
        self._balance = balance     # protected за конвенцією: "не чіпай ззовні"
        self.__pin = "0000"         # private: name mangling

    def get_balance(self):
        return self._balance
```

- `self._balance` — **одне** підкреслення. Технічно доступне, але це сигнал: "внутрішнє, не використовуй ззовні".
- `self.__pin` — **два** підкреслення. Python застосовує **name mangling**: атрибут перейменовується у `_Account__pin`.

```python
acc = Account(100)
acc._balance          # 100 — працює, але так робити не варто
# acc.__pin           # ❌ AttributeError
acc._Account__pin     # "0000" — name mangling НЕ робить атрибут абсолютно недоступним
```

Сенс інкапсуляції — сховати **внутрішній стан** і дати доступ через методи:

```python
class Counter:
    def __init__(self):
        self.__count = 0          # ніхто ззовні не змінить напряму

    def increment(self):
        self.__count += 1

    def value(self):
        return self.__count
```

---

### 3. `@property` — гетер як атрибут

`@property` дозволяє звертатись до методу як до атрибута — і додати валідацію:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Нижче абсолютного нуля")
        self._celsius = value


t = Temperature(20)
t.celsius          # 20 — без дужок, як атрибут
t.celsius = 25     # виклик setter з валідацією
```

Так внутрішній `_celsius` захищений, а доступ — контрольований.

---

### 4. Поліморфізм: однаковий інтерфейс, різна реалізація

Різні класи мають метод **з однаковим ім'ям**, але з різною реалізацією. Виклик — однаковий:

```python
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2


shapes = [Circle(10), Square(5)]
for shape in shapes:
    print(shape.area())   # однаковий виклик, різний результат
```

**Duck typing**: Python не перевіряє тип. Якщо об'єкт має метод `.area()` — його можна викликати. "Якщо це крякає як качка — це качка".

---

### 5. Абстракція

Абстракція — сховати **як** щось працює за простим інтерфейсом. Користувач класу бачить `send()`, а не сокети й ретраї всередині:

```python
class EmailSender:
    def send(self, to, text):
        self._connect()          # деталі сховані
        self._authenticate()
        return f"Sent to {to}"

    def _connect(self): ...
    def _authenticate(self): ...
```

Для формального контракту існує `abstractmethod` — метод, який **зобов'язані** реалізувати нащадки:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...
# Shape()  # ❌ не можна створити абстрактний клас напряму
```

Глибше `abc` розберемо пізніше — тут достатньо знати, що це формалізує абстракцію.

---

### 6. У QA automation

**Поліморфізм** — усі Page-класи мають `.is_loaded()`:

```python
class LoginPage:
    def is_loaded(self):
        return True

class DashboardPage:
    def is_loaded(self):
        return True


pages = [LoginPage(), DashboardPage()]
assert all(p.is_loaded() for p in pages)   # однаковий інтерфейс
```

**Інкапсуляція/абстракція** — `ApiClient` ховає токен і деталі HTTP:

```python
class ApiClient:
    def __init__(self, token):
        self.__token = token          # прихований секрет

    def get_user(self, user_id):
        return {"id": user_id, "auth": bool(self.__token)}
```

Тест викликає `get_user()`, не знаючи про заголовки, ретраї чи токен.

---

## ⚠️ Типові помилки

### `__private` — це НЕ абсолютна недоступність

```python
class Box:
    def __init__(self):
        self.__secret = 42

b = Box()
# b.__secret        # ❌ AttributeError
b._Box__secret      # ✅ 42 — name mangling обходиться
```

Name mangling лише **ускладнює** випадковий доступ і уникає колізій імен у наслідуванні — це не захист від зловмисника.

### Не плутай інкапсуляцію з приватністю

```python
# ❌ "Інкапсуляція = зробити все private"
# ✅ Інкапсуляція = дати контрольований доступ до внутрішнього стану
#    (методи, @property), а не просто заховати
```

### Не переускладнюй `@property`

```python
# ❌ property, який нічого не контролює — зайвий код
class User:
    @property
    def name(self):
        return self._name

# ✅ якщо валідації/логіки немає — використовуй звичайний атрибут
class User:
    def __init__(self, name):
        self.name = name
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-48-magic-methods`
