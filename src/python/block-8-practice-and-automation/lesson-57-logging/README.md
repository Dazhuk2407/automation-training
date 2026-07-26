# Lesson 57: Introduction to Logging

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розуміти чому `logging` кращий за `print`
- ✅ Використовувати рівні: `DEBUG` / `INFO` / `WARNING` / `ERROR` / `CRITICAL`
- ✅ Налаштувати формат і рівень через `logging.basicConfig`
- ✅ Створювати іменований логер `logging.getLogger(__name__)`
- ✅ Логувати у функціях замість `print`

---

## 📋 Передумови

Ви вже знаєте:
- Функції (Lesson 26)
- f-strings (Lesson 39)

---

## 📖 Теорія

### 1. Навіщо logging замість print

`print` виводить усе в один потік без контексту. `logging` дає:

- **Рівні важливості** — можна відфільтрувати шум і бачити лише важливе.
- **Формат** — час, ім'я модуля, рівень поруч з повідомленням.
- **Керованість** — один рядок налаштування змінює поведінку всієї програми.
- **Вимкнення без видалення коду** — підняли рівень, і `DEBUG`-повідомлення зникли, але код залишився.

```python
import logging

# print — все однакове, нічого не вимкнути без видалення
print("Connecting to DB")
print("ERROR: connection failed")

# logging — рівні, формат, керованість
logging.debug("Connecting to DB")
logging.error("connection failed")
```

`print` пише у `stdout`, а `logging` за замовчуванням у `stderr` і легко перенаправляється у файл.

---

### 2. Рівні: DEBUG < INFO < WARNING < ERROR < CRITICAL

П'ять стандартних рівнів за зростанням важливості:

| Рівень | Число | Коли використовувати |
|--------|-------|----------------------|
| `DEBUG` | 10 | Детальна діагностика: значення змінних, кроки алгоритму |
| `INFO` | 20 | Нормальний хід роботи: тест почався, користувач створений |
| `WARNING` | 30 | Щось незвичне, але робота триває: retry, нестабільність |
| `ERROR` | 40 | Операція впала: assertion failed, exception |
| `CRITICAL` | 50 | Фатальна помилка, програма далі працювати не може |

Логер пропускає повідомлення, тільки якщо його рівень **≥** налаштованого мінімуму:

```python
import logging

logging.basicConfig(level=logging.WARNING)

logging.debug("не з'явиться")     # 10 < 30
logging.info("не з'явиться")      # 20 < 30
logging.warning("з'явиться")      # 30 >= 30
logging.error("з'явиться")        # 40 >= 30
```

---

### 3. logging.basicConfig(level=..., format=...)

`basicConfig` — базове налаштування кореневого логера. Викликається **один раз** на старті програми:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logging.info("Тест почався")
# 2026-07-26 10:00:00,123 [INFO] root: Тест почався
```

Корисні плейсхолдери формату:

- `%(asctime)s` — час
- `%(levelname)s` — рівень (`INFO`, `ERROR`, ...)
- `%(name)s` — ім'я логера
- `%(message)s` — саме повідомлення

---

### 4. Іменований логер: logging.getLogger(__name__)

У модулях краще створювати власний логер, а не викликати `logging.info` напряму:

```python
import logging

logger = logging.getLogger(__name__)

def create_user(name):
    logger.info("User created")
    return name
```

`__name__` дає ім'я модуля (наприклад, `tests.test_login`), тож у логах видно, звідки прийшло повідомлення. Це стандартний патерн у бібліотеках і тест-фреймворках.

---

### 5. Логування зі змінними

Не конкатенуйте рядки вручну. Передавайте параметри через `%`-плейсхолдери — це **lazy**: рядок формується лише якщо повідомлення реально логується:

```python
import logging

logger = logging.getLogger(__name__)

name = "alice"
# ✅ lazy %-параметри
logger.info("User %s created", name)

# ✅ f-string теж допустимо (просто, читабельно)
logger.info(f"User {name} created")
```

`%`-форма економить ресурси: якщо рівень `DEBUG` вимкнено, форматування взагалі не виконається.

---

### 6. Logging у QA automation

Логи роблять падіння тестів зрозумілими без дебагера:

```python
import logging

logger = logging.getLogger(__name__)

def run_login_test(user, password):
    logger.info("Step: open login page")
    logger.info("Step: enter credentials for %s", user)

    if not password:
        logger.warning("Empty password — test may be flaky")

    success = bool(user and password)
    if not success:
        logger.error("Login failed for user %s", user)
    return success
```

- `INFO` — кроки тесту (open page, click, submit).
- `WARNING` — ознаки нестабільності (retry, повільна відповідь).
- `ERROR` — падіння тесту, невдалий assert, exception.

---

## ⚠️ Типові помилки

### print замість logging

```python
# ❌ неможливо вимкнути чи відфільтрувати
print("User created")

# ✅ рівень, формат, керованість
logger.info("User created")
```

### Неправильний рівень (усе INFO)

```python
# ❌ помилку не відрізнити від звичайного кроку
logger.info("Login failed")

# ✅ падіння — це ERROR
logger.error("Login failed")
```

### logging.warn (deprecated) замість warning

```python
# ❌ deprecated
logger.warn("flaky")

# ✅
logger.warning("flaky")
```

### Конкатенація рядків замість %-параметрів

```python
# ❌ рядок формується завжди, навіть коли лог вимкнено
logger.info("User " + name + " created")

# ✅ lazy %-параметри
logger.info("User %s created", name)
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-58-project-structure`
