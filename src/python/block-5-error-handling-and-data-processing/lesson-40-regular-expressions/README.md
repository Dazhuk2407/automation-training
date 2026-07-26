# Lesson 40: Introduction to Regular Expressions (модуль `re`)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Використовувати `re.search`, `re.match`, `re.findall`, `re.fullmatch`
- ✅ Будувати базові патерни (`\d` `\w` `\s` `.` `+` `*` `?` `[]` `{}`)
- ✅ Витягувати групи через `()`
- ✅ Перевіряти формати (email, телефон, дата) у тестах
- ✅ Замінювати текст через `re.sub`

---

## 📋 Передумови

Ви вже знаєте:
- Рядки та методи рядків (Lesson 7-10)
- f-strings (Lesson 39)

---

## 📖 Теорія

### 1. Навіщо потрібні regex

**Regular expression (regex)** — це шаблон для пошуку тексту за правилами, а не за точним збігом.

У QA automation regex потрібні щоб:
- **шукати** — знайти рядок у логах за патерном;
- **валідувати** — перевірити, що email/телефон/дата у правильному форматі;
- **витягувати** — дістати ID тесту, код помилки, число з рядка.

Модуль `re` — частина стандартної бібліотеки, імпорт не потребує встановлення:

```python
import re

text = "User id=42 logged in"
match = re.search(r"id=(\d+)", text)
print(match.group(1))  # "42"
```

---

### 2. `search` vs `match` vs `fullmatch`

Три способи застосувати патерн до рядка:

| Функція | Де шукає | Повертає |
|---------|----------|----------|
| `re.search` | **перше входження будь-де** у рядку | Match object або `None` |
| `re.match` | тільки **з початку** рядка | Match object або `None` |
| `re.fullmatch` | збіг має покрити **весь рядок** | Match object або `None` |

```python
import re

re.search(r"\d+", "abc123")     # знайде "123"
re.match(r"\d+", "abc123")      # None — на початку не цифра
re.match(r"\d+", "123abc")      # знайде "123"
re.fullmatch(r"\d+", "123abc")  # None — не весь рядок цифри
re.fullmatch(r"\d+", "123")     # збіг — весь рядок цифри
```

**Match object** описує знайдений збіг. Текст збігу дає метод `.group()`:

```python
m = re.search(r"\d+", "id=42")
if m:                # ✅ спочатку перевіряємо, що не None
    print(m.group())  # "42"
```

Для валідації зручний прийом `... is not None`:

```python
def is_all_digits(s):
    return re.fullmatch(r"\d+", s) is not None
```

---

### 3. Метасимволи

Метасимволи — це скорочення для класів символів:

| Патерн | Значення |
|--------|----------|
| `\d` | одна цифра `0-9` |
| `\w` | символ слова: літера, цифра або `_` |
| `\s` | пробільний символ (пробіл, `\t`, `\n`) |
| `.` | будь-який символ (крім `\n`) |
| `^` | початок рядка |
| `$` | кінець рядка |

```python
import re

re.search(r"\d", "abc7")     # "7"
re.search(r"\w+", "log_42")  # "log_42"
re.search(r"^ERROR", "ERROR: fail")   # збіг — рядок починається з ERROR
re.search(r"failed$", "test failed")  # збіг — рядок закінчується failed
```

---

### 4. Квантифікатори

Квантифікатор задає, **скільки разів** повторюється попередній елемент:

| Патерн | Значення |
|--------|----------|
| `+` | один або більше |
| `*` | нуль або більше |
| `?` | нуль або один (необов'язково) |
| `{n}` | рівно `n` разів |
| `{n,m}` | від `n` до `m` разів |

```python
import re

re.search(r"\d+", "id=42")       # "42" — одна чи більше цифр
re.search(r"colou?r", "color")   # збіг — u необов'язкове
re.search(r"\d{3}", "code=500")  # "500" — рівно 3 цифри
re.search(r"\d{2,4}", "year2026") # "2026" — від 2 до 4 цифр
```

---

### 5. Класи символів `[]`

У квадратних дужках задають власний набір дозволених символів:

```python
import re

re.findall(r"[a-z]", "aB2c")      # ["a", "c"]
re.findall(r"[a-z0-9]", "aB2c")   # ["a", "2", "c"]
re.search(r"[A-Za-z]+", "Hello")  # "Hello"
```

`^` на початку класу — це **заперечення** (все, крім перелічених):

```python
re.findall(r"[^0-9]", "a1b2")  # ["a", "b"] — все, крім цифр
```

---

### 6. `re.findall` — усі входження

`re.findall` повертає **список** усіх збігів (а не Match object):

```python
import re

re.findall(r"\d+", "a1 b22 c333")  # ["1", "22", "333"]
re.findall(r"[A-Z]+", "AB cd EF")  # ["AB", "EF"]
```

Якщо у патерні є **групи `()`**, `findall` повертає список того, що в групах:

```python
re.findall(r"(\w+)=(\d+)", "a=1 b=2")
# [("a", "1"), ("b", "2")]  — список кортежів (група1, група2)
```

---

### 7. `re.sub` — заміна

`re.sub(pattern, replacement, text)` замінює всі збіги:

```python
import re

re.sub(r"\d", "*", "id=42")         # "id=**"
re.sub(r"\s+", " ", "a   b\t c")    # "a b c" — стиснути пробіли
```

Практичний приклад — **маскування чисел у логах** (щоб приховати чутливі дані):

```python
def mask_numbers(log):
    return re.sub(r"\d+", "***", log)

mask_numbers("user 42 paid 100")  # "user *** paid ***"
```

---

### 8. Regex у QA automation

Типові задачі під час автоматизації тестів:

```python
import re

# Валідація email
def is_valid_email(s):
    return re.fullmatch(r"[\w.]+@[\w.]+\.\w+", s) is not None

# Валідація телефону формату 123-456-7890
def is_valid_phone(s):
    return re.fullmatch(r"\d{3}-\d{3}-\d{4}", s) is not None

# Валідація дати формату YYYY-MM-DD
def is_valid_date(s):
    return re.fullmatch(r"\d{4}-\d{2}-\d{2}", s) is not None

# Витяг ID тесту з рядка логу
def extract_test_id(log):
    m = re.search(r"TEST-(\d+)", log)
    return m.group(1) if m else None

# Витяг коду помилки
def extract_error_code(log):
    m = re.search(r"error code (\d+)", log)
    return int(m.group(1)) if m else None
```

---

## ⚠️ Типові помилки

### Забути raw string `r"..."`

Без `r` зворотний слеш інтерпретується Python до передачі у regex:

```python
# ❌ "\d" без r — попередження/помилка escape-послідовності
re.search("\d+", text)

# ✅ Завжди raw string
re.search(r"\d+", text)
```

### Плутати `search` і `match`

```python
# ❌ match шукає лише з початку — тут None
re.match(r"\d+", "abc123")

# ✅ search знайде будь-де
re.search(r"\d+", "abc123")
```

### Жадібне `.*` замість `.*?`

`.*` захоплює якомога більше (жадібно), `.*?` — якомога менше (лінива версія):

```python
text = "<a><b>"
re.search(r"<.*>", text).group()   # ❌ "<a><b>" — забрав усе
re.search(r"<.*?>", text).group()  # ✅ "<a>" — до першого >
```

### Не перевірити, що match не `None`

```python
# ❌ AttributeError, якщо збігу немає (search повернув None)
code = re.search(r"\d+", text).group()

# ✅ Спочатку перевіряємо
m = re.search(r"\d+", text)
code = m.group() if m else None
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-41-json-data`
