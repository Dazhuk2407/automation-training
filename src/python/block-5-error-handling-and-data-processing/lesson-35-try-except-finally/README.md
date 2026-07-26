# Lesson 35: try / except / finally

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Перехоплювати винятки через `try` / `except`, щоб код не падав
- ✅ Ловити кілька типів винятків окремими `except` блоками (від конкретного до загального)
- ✅ Отримувати об'єкт винятку через `except SomeError as e` та читати повідомлення
- ✅ Використовувати `else` (коли помилки не було) та `finally` (виконується завжди)
- ✅ Застосовувати обробку помилок для надійних тестів і скриптів

---

## 📋 Передумови

Ви вже знаєте:
- Функції та `return` (Lesson 26-29)
- Базовий синтаксис Python (Lesson 1-10)

---

## 📖 Теорія

### 1. Базовий try/except — навіщо

Без обробки помилок будь-який виняток зупиняє програму. `try/except` дозволяє
перехопити помилку та продовжити роботу:

```python
def to_int(value):
    """Конвертувати рядок у число."""
    try:
        return int(value)
    except ValueError:
        return None  # не падаємо, повертаємо дефолт

to_int("42")    # 42
to_int("abc")   # None — без краху програми
```

Код у `try` виконується до першої помилки. Якщо помилки немає — `except` пропускається.

---

### 2. Кілька except блоків

Для різних типів помилок — окремі `except`. Порядок: **від конкретного до загального**:

```python
def get_first_item(data, index):
    """Взяти елемент за індексом."""
    try:
        return data[index]
    except IndexError:
        return "no such index"
    except KeyError:
        return "no such key"
    except TypeError:
        return "wrong type"

get_first_item([1, 2, 3], 10)      # "no such index"
get_first_item({"a": 1}, "b")       # "no such key"
get_first_item(None, 0)             # "wrong type"
```

Python перевіряє `except` зверху вниз і виконує **перший** що підходить.

---

### 3. except ... as e — доступ до повідомлення

`as e` дає об'єкт винятку. Через `str(e)` отримуємо текст помилки:

```python
def parse_int(value):
    """Повернути (результат, повідомлення_помилки)."""
    try:
        return int(value), None
    except ValueError as e:
        return None, str(e)  # "invalid literal for int() with base 10: 'abc'"

parse_int("10")    # (10, None)
parse_int("abc")   # (None, "invalid literal ...")
```

`e` — це екземпляр класу винятку, у нього є `.args` та рядкове представлення.

---

### 4. except (TypeA, TypeB) — кілька типів в одному except

Якщо кілька винятків треба обробити однаково — перелічіть їх у tuple:

```python
def safe_divide(a, b):
    """Ділення з захистом від типових помилок."""
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return 0.0

safe_divide(10, 2)      # 5.0
safe_divide(10, 0)      # 0.0  (ZeroDivisionError)
safe_divide(10, "x")    # 0.0  (TypeError)
```

---

### 5. else — коли except не спрацював

Блок `else` виконується **тільки якщо винятку не було**. Зручно відділяти
"ризиковий" код від того, що робимо при успіху:

```python
def read_config(raw):
    """Розпарсити конфіг та повернути статус."""
    try:
        value = int(raw)
    except ValueError:
        return "parse error"
    else:
        return f"ok: {value}"  # виконається лише коли int() успішний

read_config("8080")   # "ok: 8080"
read_config("bad")    # "parse error"
```

---

### 6. finally — виконується завжди

Блок `finally` виконується **у будь-якому випадку** — і при помилці, і без неї.
Використовується для cleanup: закриття файлів, звільнення ресурсів:

```python
def process_resource(data):
    """Симуляція роботи з ресурсом, що завжди закривається."""
    log = []
    try:
        log.append("open")
        if not data:
            raise ValueError("empty data")
        log.append("process")
    except ValueError:
        log.append("error")
    finally:
        log.append("close")  # завжди, навіть після помилки
    return log

process_resource([1])   # ["open", "process", "close"]
process_resource([])    # ["open", "error", "close"]
```

Реальний приклад — файли (хоча `with` робить це автоматично):

```python
f = open("data.txt")
try:
    content = f.read()
finally:
    f.close()  # файл закриється навіть якщо read() кине помилку
```

---

### 7. У QA: надійні операції та дефолти

У тестах і скриптах часто треба обгорнути ненадійну операцію та повернути
дефолт замість падіння всього прогону:

```python
def get_status_code(response, default=500):
    """Безпечно дістати status_code з відповіді."""
    try:
        return int(response["status"])
    except (KeyError, ValueError, TypeError):
        return default


def test_get_status_code():
    assert get_status_code({"status": "200"}) == 200
    assert get_status_code({}) == 500              # немає ключа
    assert get_status_code({"status": "oops"}) == 500  # не число
    assert get_status_code(None) == 500            # не dict
```

---

## ⚠️ Типові помилки

### Голий except: ловить усе

```python
# ❌ ловить навіть KeyboardInterrupt, приховує реальні баги
try:
    risky()
except:
    pass

# ✅ ловимо конкретний виняток
try:
    risky()
except ValueError:
    handle()
```

### Ловити Exception коли треба конкретний

```python
# ❌ занадто широко — сховає TypeError, KeyError тощо
try:
    value = int(raw)
except Exception:
    value = 0

# ✅ саме той, який очікуємо
try:
    value = int(raw)
except ValueError:
    value = 0
```

### Неправильний порядок except

```python
# ❌ загальний перед конкретним — ValueError недосяжний (dead code)
try:
    parse()
except Exception:
    ...
except ValueError:   # ніколи не виконається
    ...

# ✅ від конкретного до загального
try:
    parse()
except ValueError:
    ...
except Exception:
    ...
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-36-common-errors`
