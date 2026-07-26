# Lesson 50: Working with CSV and JSON Files

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Читати CSV через `csv.reader` та `csv.DictReader`
- ✅ Писати CSV через `csv.writer` та `csv.DictWriter`
- ✅ Читати JSON з файлу (`json.load`) та писати у файл (`json.dump`)
- ✅ Розуміти, навіщо `newline=""` при роботі з `csv`
- ✅ Обирати між CSV та JSON для тестових даних

---

## 📋 Передумови

Ви вже знаєте:
- Читання та запис файлів, контекст `with` (Lesson 49)
- JSON-рядки: `json.loads` / `json.dumps` (Lesson 41)

---

## 📖 Теорія

### 1. CSV — табличні дані. csv.reader

CSV (Comma-Separated Values) — це простий текстовий формат для **табличних даних**: рядки таблиці розділені переносами, а колонки — комами.

```
name,age,role
Alice,30,admin
Bob,25,user
```

`csv.reader` повертає **ітератор рядків**, де кожен рядок — це **список рядків-значень** (`list[str]`):

```python
import csv

with open("users.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ['name', 'age', 'role']
# ['Alice', '30', 'admin']
# ['Bob', '25', 'user']
```

Перший рядок — це заголовок. Усі значення — **рядки** (навіть `'30'`).

---

### 2. csv.DictReader — рядки як dict

`csv.DictReader` бере **перший рядок як заголовок** і повертає кожен наступний рядок як `dict`, де ключі — назви колонок:

```python
import csv

with open("users.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# Alice 30
# Bob 25
```

Це зручніше: не треба памʼятати порядок колонок — звертаємось за назвою.

---

### 3. Запис CSV: csv.writer та csv.DictWriter. newline=""

`csv.writer` пише **списки**: `writerow` — один рядок, `writerows` — багато:

```python
import csv

with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerows([["Alice", 30], ["Bob", 25]])
```

`csv.DictWriter` пише **словники**. Треба задати `fieldnames` і викликати `writeheader`:

```python
import csv

rows = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]

with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(rows)
```

**Чому `newline=""`?** Модуль `csv` сам керує переносами рядків. Якщо не передати `newline=""`, на Windows між рядками зʼявляться **зайві порожні рядки**. Тому CSV-файли завжди відкривають з `newline=""`.

---

### 4. JSON-файли: json.load та json.dump

На відміну від рядкових `loads`/`dumps` (Lesson 41), для файлів є `load`/`dump` — вони працюють напряму з файловим обʼєктом:

```python
import json

# Читання: файл → Python-обʼєкт
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

# Запис: Python-обʼєкт → файл
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
```

Різниця проста:
- `json.load(f)` / `json.dump(obj, f)` — працюють з **файлом**.
- `json.loads(s)` / `json.dumps(obj)` — працюють з **рядком** (Lesson 41).

Параметр `indent=2` робить файл читабельним (з відступами). Для не-ASCII символів корисний `ensure_ascii=False`.

---

### 5. Коли CSV, а коли JSON

| Критерій | CSV | JSON |
|----------|-----|------|
| Структура | Плоска таблиця | Вкладені структури |
| Типи | Усе — рядки | int, float, bool, list, dict |
| Excel/Google Sheets | ✅ Відкриється | ❌ |
| API-відповіді | ❌ | ✅ Типовий формат |

**CSV** — коли дані плоскі й треба відкрити в Excel (наприклад, набір тест-кейсів).
**JSON** — коли є вкладеність (обʼєкт з масивами всередині) або це відповідь API.

---

### 6. У QA automation

- **Читання тест-даних з CSV**: параметризація тестів (набори логінів/паролів, очікуваних результатів).
- **Збереження результатів у JSON**: звіт про прогін тестів зі вкладеною структурою (статус, тривалість, помилки).

```python
import csv, json


def load_test_cases(path):
    """Прочитати тест-кейси з CSV як список словників."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_report(path, report):
    """Зберегти звіт про прогін у JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
```

---

## ⚠️ Типові помилки

### Забути newline="" при роботі з csv

```python
# ❌ На Windows зʼявляться зайві порожні рядки між записами
with open("out.csv", "w") as f:
    csv.writer(f).writerow(["a", "b"])

# ✅ Завжди з newline=""
with open("out.csv", "w", newline="") as f:
    csv.writer(f).writerow(["a", "b"])
```

### Плутати load/loads та dump/dumps

```python
# ❌ loads очікує рядок, а не файл
data = json.loads(open("data.json"))

# ✅ load — для файлового обʼєкта
with open("data.json") as f:
    data = json.load(f)
```

### DictWriter без writeheader

```python
# ❌ Файл без рядка заголовка → DictReader не знатиме колонок
writer = csv.DictWriter(f, fieldnames=["name", "age"])
writer.writerows(rows)

# ✅ Спершу writeheader
writer.writeheader()
writer.writerows(rows)
```

### Читати числа з CSV як int

```python
# ❌ row["age"] — це рядок "30", а не число 30
total = row["age"] + 1  # TypeError

# ✅ Явно конвертувати
total = int(row["age"]) + 1
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-51-pathlib`
