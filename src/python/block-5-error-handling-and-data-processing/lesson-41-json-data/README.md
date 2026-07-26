# Lesson 41: Working with JSON Data

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Перетворювати JSON-рядок у Python-обʼєкт через `json.loads()`
- ✅ Перетворювати Python-обʼєкт у JSON-рядок через `json.dumps()`
- ✅ Розуміти мапінг типів JSON ↔ Python
- ✅ Навігувати вкладеними API-відповідями
- ✅ Форматувати JSON (`indent`, `sort_keys`, `ensure_ascii`)
- ✅ Безпечно обробляти невалідний JSON (`JSONDecodeError`)

---

## 📋 Передумови

Ви вже знаєте:
- `dict`/`list` та вкладені структури (Lesson 9-17)
- `try`/`except` (Lesson 35)

---

## 📖 Теорія

### 1. Що таке JSON і навіщо в QA

**JSON** (JavaScript Object Notation) — це текстовий формат обміну даними. Це просто **рядок**, який виглядає як вкладені словники та списки. У QA automation JSON зустрічається всюди: відповіді REST API, конфіги, тестові дані, логи.

Приклад JSON-рядка:

```json
{
  "name": "Alice",
  "age": 30,
  "active": true,
  "roles": ["admin", "user"]
}
```

Зверніть увагу: у JSON **тільки подвійні лапки**, `true`/`false`/`null` пишуться з малої літери. Це не Python-код — це рядок у певному форматі.

---

### 2. json.loads() та json.dumps()

Модуль `json` — вбудований, встановлювати нічого не треба:

```python
import json
```

`json.loads(str)` — **loads = load string** — парсить JSON-рядок у Python-обʼєкт (`dict` або `list`):

```python
raw = '{"name": "Alice", "age": 30}'
data = json.loads(raw)
print(data["name"])  # Alice
print(type(data))     # <class 'dict'>
```

`json.dumps(obj)` — **dumps = dump string** — серіалізує Python-обʼєкт назад у JSON-рядок:

```python
obj = {"name": "Bob", "age": 25}
text = json.dumps(obj)
print(text)        # {"name": "Bob", "age": 25}
print(type(text))  # <class 'str'>
```

Запамʼятайте напрямок:
- `loads` — **рядок → обʼєкт** (парсинг)
- `dumps` — **обʼєкт → рядок** (серіалізація)

---

### 3. Мапінг типів JSON ↔ Python

Коли ви парсите або серіалізуєте, типи автоматично конвертуються:

| JSON            | Python          |
|-----------------|-----------------|
| `object` `{}`   | `dict`          |
| `array` `[]`    | `list`          |
| `string`        | `str`           |
| `number` (int)  | `int`           |
| `number` (real) | `float`         |
| `true` / `false`| `True` / `False`|
| `null`          | `None`          |

```python
raw = '{"count": 3, "ratio": 0.5, "ok": true, "note": null}'
data = json.loads(raw)
# data == {"count": 3, "ratio": 0.5, "ok": True, "note": None}
```

---

### 4. Форматування dumps

За замовчуванням `dumps` дає компактний рядок в один рядок. Для читабельності є параметри:

```python
data = {"name": "Alice", "age": 30, "city": "Kyiv"}

# indent=2 — красиве форматування з відступами
json.dumps(data, indent=2)
# {
#   "name": "Alice",
#   "age": 30,
#   "city": "Kyiv"
# }

# sort_keys=True — ключі за алфавітом
json.dumps(data, sort_keys=True)
# {"age": 30, "city": "Kyiv", "name": "Alice"}
```

`ensure_ascii=False` — щоб кирилиця зберігалась як текст, а не як `ал...`:

```python
json.dumps({"місто": "Київ"})                     # {"м...": "К..."}
json.dumps({"місто": "Київ"}, ensure_ascii=False)  # {"місто": "Київ"}
```

---

### 5. Навігація вкладеною структурою (API response)

Реальні API повертають вкладені структури. Після `loads` це звичайні `dict`/`list`:

```python
raw = '''
{
  "status": "ok",
  "data": {
    "users": [
      {"id": 1, "email": "alice@test.com"},
      {"id": 2, "email": "bob@test.com"}
    ]
  }
}
'''
resp = json.loads(raw)

# Пряма навігація по ключах та індексах
resp["data"]["users"][0]["email"]  # "alice@test.com"

# Безпечна навігація через .get() — не впаде, якщо ключа немає
resp.get("data", {}).get("users", [])  # список або []
```

Якщо дані з невідомого джерела — використовуйте `.get()`, щоб уникнути `KeyError`.

---

### 6. Помилки: JSONDecodeError

Якщо рядок — невалідний JSON, `json.loads` кидає `json.JSONDecodeError` (підклас `ValueError`). Завжди обгортайте парсинг чужих даних у `try`/`except`:

```python
def safe_parse(raw):
    """Парсить JSON, повертає None при помилці."""
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None

safe_parse('{"ok": true}')  # {"ok": True}
safe_parse('{broken}')       # None
```

---

### 7. У QA automation

Найтиповіші сценарії:

```python
# 1. Парсинг відповіді (у бібліотеці requests це response.json())
data = json.loads(response_text)

# 2. Перевірка полів у тестах
def test_user_response():
    data = json.loads('{"id": 1, "name": "Alice"}')
    assert data["id"] == 1
    assert data["name"] == "Alice"

# 3. Порівняння очікуваного та фактичного
def test_matches_expected():
    actual = json.loads('{"a": 1, "b": 2}')
    expected = {"a": 1, "b": 2}
    assert actual == expected
```

> ℹ️ Читання/запис JSON-**файлів** (`json.load`/`json.dump` без `s`) буде в Block 7. Тут працюємо з **рядками**.

---

## ⚠️ Типові помилки

### Плутати loads та dumps

```python
# ❌ dumps робить рядок з обʼєкта, loads — навпаки
data = json.dumps('{"name": "Alice"}')  # серіалізує рядок у рядок!

# ✅ рядок → обʼєкт
data = json.loads('{"name": "Alice"}')
```

### Одинарні лапки в JSON

```python
# ❌ JSONDecodeError — JSON вимагає подвійні лапки
json.loads("{'name': 'Alice'}")

# ✅ подвійні лапки
json.loads('{"name": "Alice"}')
```

### True замість true при ручному написанні

```python
# ❌ JSONDecodeError — це Python, не JSON
json.loads('{"active": True}')

# ✅ JSON використовує true/false/null
json.loads('{"active": true}')
```

### Звертання до ключа без .get на невідомих даних

```python
data = json.loads(raw)

# ❌ KeyError, якщо ключа немає
email = data["user"]["email"]

# ✅ безпечно через .get()
email = data.get("user", {}).get("email")
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-42-classes-and-objects`
