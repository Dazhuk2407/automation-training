# Lesson 49: Reading and Writing Files

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Відкривати файли через `with open(...)` (контекстний менеджер)
- ✅ Читати файли: `read()`, `readline()`, `readlines()`, ітерація по рядках
- ✅ Писати та додавати дані (режими `"w"`, `"a"`, `"r"`)
- ✅ Розуміти, навіщо потрібен контекстний менеджер (автозакриття)
- ✅ Працювати з `encoding="utf-8"`

---

## 📋 Передумови

Ви вже знаєте:
- Рядки та методи рядків (Lesson 7-10)
- Цикли `for` / `while` (Lesson 20-22)

---

## 📖 Теорія

### 1. Навіщо `with open()`

Файл треба **відкрити**, попрацювати з ним і обов'язково **закрити**. Якщо забути закрити — дані можуть не записатися, а файловий дескриптор «зависне».

Контекстний менеджер `with` закриває файл **автоматично**, навіть якщо станеться помилка:

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("hello")
# тут файл вже закрито — гарантовано
```

Синтаксис: `open(path, mode, encoding=...)`. `f` — це файловий об'єкт. Після виходу з блоку `with` файл закривається сам.

---

### 2. Запис у режимі `"w"`

Режим `"w"` (write) **створює** файл або **повністю перезаписує** його вміст:

```python
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("line 1\n")
    f.write("line 2\n")
```

`write()` не додає `\n` автоматично — ставте перенос рядка самі.

Щоб записати список рядків, зручний `writelines()`:

```python
lines = ["first\n", "second\n"]
with open("out.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```

Завжди вказуйте `encoding="utf-8"`, щоб коректно писати кирилицю та emoji.

---

### 3. Читання у режимі `"r"`

Режим `"r"` (read) — читання. Це режим за замовчуванням.

```python
# Весь текст одним рядком
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Список рядків (з символами \n на кінці)
with open("data.txt", encoding="utf-8") as f:
    lines = f.readlines()

# Ітерація по рядках — найекономніша по пам'яті
with open("data.txt", encoding="utf-8") as f:
    for line in f:
        print(line)
```

`read()` повертає весь вміст як `str`. `readlines()` — `list[str]`. Ітерація `for line in f` читає файл порядково.

---

### 4. Додавання у режимі `"a"`

Режим `"a"` (append) **дописує** в кінець файлу, не стираючи наявне:

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("new event\n")
```

Якщо файлу немає — він створюється. Це головна відмінність від `"w"`, який стирає старий вміст.

---

### 5. `.strip()` при читанні рядків

Рядки з файлу приходять із символом переносу `\n` на кінці. Перед порівнянням чи обробкою його прибирають через `.strip()`:

```python
with open("data.txt", encoding="utf-8") as f:
    for line in f:
        clean = line.strip()   # прибрали \n та зайві пробіли
        print(repr(clean))
```

Без `strip()` рядок `"admin\n"` не дорівнюватиме `"admin"`.

---

### 6. У QA automation

Файли постійно потрібні у тестуванні:

```python
# Запис лог-файлу тесту
def log_result(path, name, status):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{name}: {status}\n")


# Читання тест-даних (наприклад логінів) з файлу
def read_test_data(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
```

Логи дописують у режимі `"a"`, щоб не втратити попередні записи. Тест-дані читають і чистять через `strip()`.

---

## ⚠️ Типові помилки

### Відкрити без `with` і забути `close()`

```python
# ❌ Файл лишається відкритим, дані можуть не записатися
f = open("data.txt", "w", encoding="utf-8")
f.write("hi")
# забули f.close()

# ✅ with закриває автоматично
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("hi")
```

### `"w"` замість `"a"` — втрата даних

```python
# ❌ Кожен запис стирає попередній лог
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("event\n")

# ✅ Дописуємо в кінець
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("event\n")
```

### Забути `encoding`

```python
# ❌ Кирилиця/emoji можуть зламатися на різних ОС
with open("data.txt", "w") as f:
    f.write("привіт")

# ✅ Явний encoding
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("привіт")
```

### Не робити `strip()` рядків

```python
# ❌ "admin\n" != "admin"
with open("data.txt", encoding="utf-8") as f:
    for line in f:
        if line == "admin":  # ніколи не спрацює
            ...

# ✅ Прибрати \n
with open("data.txt", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "admin":
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

**Далі:** `lesson-50-csv-and-json-files`
