# Lesson 45: Static Methods

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Оголошувати методи через декоратор `@staticmethod`
- ✅ Розуміти, що static method не отримує `self` та `cls`
- ✅ Вибирати між static / class / instance методом
- ✅ Використовувати static для утиліт, логічно пов'язаних з класом (валідатори, конвертери)
- ✅ Викликати static метод через клас і через екземпляр

---

## 📋 Передумови

Ви вже знаєте:
- Instance та class методи, `self` і `cls` (Lesson 44)
- Функції та return values (Lesson 26)

---

## 📖 Теорія

### 1. Що таке @staticmethod

`@staticmethod` — це метод, який **не отримує** ні `self`, ні `cls`. Це звичайна функція, яка живе у namespace класу.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        """Додати два числа. Не залежить від об'єкта чи класу."""
        return a + b
```

Static method не має доступу ані до стану екземпляра (`self.x`), ані до стану класу (`cls.y`). Він працює лише зі своїми аргументами.

```python
MathUtils.add(2, 3)  # 5
```

Ми групуємо таку функцію в класі, бо вона **логічно пов'язана** з ним, хоча й не потребує його стану.

---

### 2. Синтаксис і виклик

Static method можна викликати двома способами — через клас або через екземпляр. Результат однаковий:

```python
class Converter:
    @staticmethod
    def to_upper(text):
        return text.upper()

# Виклик через клас (найпоширеніше)
Converter.to_upper("qa")      # "QA"

# Виклик через екземпляр (теж працює)
c = Converter()
c.to_upper("qa")               # "QA"
```

Зверніть увагу: у виклику `Converter.to_upper("qa")` аргумент `"qa"` потрапляє прямо в параметр `text` — жодного прихованого `self` чи `cls` не передається.

---

### 3. Коли обирати static

Static підходить, коли функція:
- логічно належить класу (об'єднання за темою),
- **не залежить** від стану об'єкта (`self`) чи класу (`cls`).

Типові кандидати — валідатори, конвертери, форматери, генератори id:

```python
class User:
    def __init__(self, email):
        self.email = email

    @staticmethod
    def is_valid_email(email):
        """Чиста утиліта: перевірити email, не читаючи self."""
        return "@" in email and "." in email
```

Тепер `User.is_valid_email("a@b.com")` можна викликати **до** створення об'єкта — зручно для попередньої валідації.

---

### 4. Порівняльна таблиця: instance / class / static

| Тип методу | Перший параметр | Має доступ до | Типове застосування |
|------------|-----------------|---------------|---------------------|
| **instance** | `self` | стан екземпляра | робота з даними конкретного об'єкта |
| **class** | `cls` | стан класу | factory-методи, лічильники класу |
| **static** | немає | нічого (лише аргументи) | чисті утиліти: валідатори, конвертери |

```python
class Order:
    tax_rate = 0.2  # стан класу

    def __init__(self, amount):
        self.amount = amount  # стан екземпляра

    def total(self):                       # instance: читає self
        return self.amount * (1 + Order.tax_rate)

    @classmethod
    def free(cls):                         # class: factory через cls
        return cls(0)

    @staticmethod
    def is_valid_amount(amount):           # static: чиста утиліта
        return amount >= 0
```

---

### 5. У QA automation

Static-методи ідеально лягають на утиліти для тестів — валідатори та генератори:

```python
class Validator:
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    @staticmethod
    def is_valid_status_code(code):
        return 200 <= code < 300


class TestId:
    @staticmethod
    def generate(prefix, number):
        """Згенерувати стабільний id тесту, напр. 'TC-0007'."""
        return f"{prefix}-{number:04d}"
```

Використання у перевірках:

```python
def test_login_response():
    assert Validator.is_valid_status_code(200)
    assert Validator.is_valid_email("qa@example.com")
    assert TestId.generate("TC", 7) == "TC-0007"
```

Логіка згрупована в класі, але не тягне за собою жодного стану — легко тестувати й перевикористовувати.

---

## ⚠️ Типові помилки

### Зайвий self у staticmethod

```python
class Validator:
    # ❌ static method не отримує self — цей self буде першим аргументом
    @staticmethod
    def is_positive(self, x):
        return x > 0

    # ✅ без self
    @staticmethod
    def is_positive(x):
        return x > 0
```

### Static там, де потрібен стан

```python
class Cart:
    def __init__(self):
        self.items = []

    # ❌ static не бачить self.items
    # @staticmethod
    # def count():
    #     return len(self.items)  # NameError: self не існує

    # ✅ потрібен доступ до стану → instance method
    def count(self):
        return len(self.items)
```

### Забутий декоратор @staticmethod

```python
class Utils:
    # ❌ без декоратора Python вважає перший аргумент за self
    def square(x):
        return x * x
    # Utils().square(3) → square(instance, 3) → square отримає зайвий аргумент

    # ✅ з декоратором
    @staticmethod
    def square(x):
        return x * x
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-46-inheritance`
