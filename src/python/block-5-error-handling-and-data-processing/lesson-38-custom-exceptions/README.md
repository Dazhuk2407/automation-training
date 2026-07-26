# Lesson 38: Custom Exceptions (власні винятки)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати власні класи винятків успадкуванням від `Exception`
- ✅ Піднімати їх через `raise` з повідомленням
- ✅ Будувати ієрархію винятків (базовий + похідні)
- ✅ Перехоплювати власні винятки та читати їх повідомлення
- ✅ Застосовувати власні винятки у валідації тестових даних

---

## 📋 Передумови

Ви вже знаєте:
- `try/except/finally` (Lesson 35)
- Типи вбудованих помилок: `ValueError`, `KeyError`, `TypeError` (Lesson 36)

> Класи детально розглянемо у Block 6. Тут потрібен **мінімум**:
> `class MyError(Exception): pass` — цього достатньо для власного винятку.

---

## 📖 Теорія

### 1. Навіщо власні винятки

Вбудовані винятки (`ValueError`, `KeyError`) — загальні. Коли тест падає з
`ValueError`, незрозуміло, **що саме** пішло не так: неправильний вік,
поганий email чи зламана відповідь API.

Власний виняток робить помилку **зрозумілою та специфічною для домену**:

```python
# ❌ Загальна помилка — незрозуміло, де саме проблема
raise ValueError("bad data")

# ✅ Специфічна помилка — одразу видно домен проблеми
raise ValidationError("email invalid")
```

Переваги:
- у трейсбеку одразу видно **тип** проблеми (`ValidationError`, а не `ValueError`);
- можна ловити **саме свій** виняток, не перехоплюючи чужі;
- код читається як опис бізнес-правил.

---

### 2. Найпростіший власний виняток

Достатньо успадкувати від `Exception` і залишити тіло порожнім:

```python
class ValidationError(Exception):
    pass
```

Підняти його — через `raise` з повідомленням:

```python
def validate_email(email):
    if "@" not in email:
        raise ValidationError("email invalid")
    return email

validate_email("bad-email")   # ← ValidationError: email invalid
```

`pass` тут означає «класу достатньо того, що він успадкував від `Exception`».
Ніякого додаткового коду не потрібно.

---

### 3. Повідомлення та доступ через `as e`

Повідомлення передається у `raise` і зчитується через `str(e)`:

```python
def validate_age(age):
    if age < 0:
        raise ValidationError("age must be positive")
    return age

try:
    validate_age(-5)
except ValidationError as e:
    print(str(e))    # age must be positive
    print(e)          # age must be positive
```

`as e` дає доступ до об'єкта винятку; `str(e)` повертає текст повідомлення.

---

### 4. Ієрархія винятків

Створюємо **базовий** виняток і **похідні** від нього:

```python
class AppError(Exception):
    """Базовий виняток застосунку."""
    pass

class ConfigError(AppError):
    """Помилка конфігурації."""
    pass

class NetworkError(AppError):
    """Помилка мережі."""
    pass
```

Головна перевага: **ловля базового класу перехоплює всі похідні**:

```python
try:
    raise NetworkError("connection refused")
except AppError as e:      # ← ловить і ConfigError, і NetworkError
    print(f"App failed: {e}")
```

Так можна обробити всі помилки застосунку одним `except AppError`,
або точково — окремим `except ConfigError`.

---

### 5. Кастомні атрибути через `__init__`

Іноді винятку потрібні додаткові дані — наприклад, код помилки.
Додаємо `__init__`, зберігаємо атрибут і викликаємо `super().__init__(message)`:

```python
class ApiError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)   # ← передаємо текст базовому Exception
        self.status_code = status_code

try:
    raise ApiError("not found", status_code=404)
except ApiError as e:
    print(str(e))            # not found
    print(e.status_code)     # 404
```

`super().__init__(message)` потрібен, щоб `str(e)` повертав повідомлення.

---

### 6. У QA automation

Власні винятки роблять падіння тестів **точними**:

```python
class TestDataError(Exception):
    """Некоректні вхідні тестові дані."""
    pass

class ApiResponseError(Exception):
    """Неочікувана відповідь від API."""
    pass

def load_user(data):
    if "id" not in data:
        raise TestDataError("user fixture missing 'id'")
    return data

def check_status(response):
    if response["status"] != 200:
        raise ApiResponseError(f"unexpected status {response['status']}")
    return response
```

Коли тест падає з `TestDataError`, одразу зрозуміло, що проблема у
**фікстурі**, а не у самому продукті.

---

## ⚠️ Типові помилки

### Успадкування не від Exception

```python
# ❌ Не успадковано від Exception — не можна raise
class ValidationError:
    pass

# ✅ Успадковано від Exception
class ValidationError(Exception):
    pass
```

### raise без повідомлення

```python
# ❌ Незрозуміло, що сталося
raise ValidationError

# ✅ З повідомленням
raise ValidationError("age must be positive")
```

### Занадто широка ієрархія

```python
# ❌ Успадкування від BaseException ловить навіть KeyboardInterrupt / SystemExit
class AppError(BaseException):
    pass

# ✅ Успадковуй від Exception
class AppError(Exception):
    pass
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-39-f-strings`
