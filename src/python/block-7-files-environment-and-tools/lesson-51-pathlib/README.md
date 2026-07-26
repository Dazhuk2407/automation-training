# Lesson 51: Керування шляхами через pathlib

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати шляхи через клас `Path`
- ✅ З'єднувати шляхи оператором `/`
- ✅ Отримувати частини шляху (`name`, `stem`, `suffix`, `parent`, `parts`)
- ✅ Перевіряти шляхи через `exists()`, `is_file()`, `is_dir()`
- ✅ Читати та писати файли через `read_text()` / `write_text()`
- ✅ Ітерувати теку через `iterdir()`, `glob()`, `rglob()`
- ✅ Розуміти переваги `pathlib` над `os.path`

---

## 📋 Передумови

Ви вже знаєте:
- Роботу з файлами (Lesson 49)
- Рядки та їхні методи

---

## 📖 Теорія

### 1. Навіщо pathlib замість рядкових шляхів

Раніше шляхи будували як рядки або через `os.path`. Це крихко: різні розділювачі
у Windows (`\`) та Linux/macOS (`/`), легко припуститися помилки при конкатенації.

`pathlib` дає **об'єктний** та **крос-платформний** підхід — один клас `Path`
працює однаково на всіх ОС:

```python
from pathlib import Path

# ❌ Старий стиль — рядки
path = "data" + "/" + "logs" + "/" + "app.log"

# ❌ os.path
import os
path = os.path.join("data", "logs", "app.log")

# ✅ pathlib — об'єктний і читабельний
path = Path("data") / "logs" / "app.log"
```

`Path` автоматично підставляє правильний розділювач для поточної ОС.

---

### 2. Створення і з'єднання шляхів

Шлях створюють з рядка, а з'єднують оператором `/`:

```python
from pathlib import Path

base = Path("data")
log = base / "logs" / "app.log"   # data/logs/app.log
```

Дуже корисний трюк — шлях до поточного файлу через `__file__`:

```python
here = Path(__file__)           # абсолютний шлях до .py файлу
project_dir = Path(__file__).parent   # тека, де лежить файл
data_file = project_dir / "data" / "users.json"
```

Так тести знаходять свої дані незалежно від того, звідки їх запустили.

---

### 3. Частини шляху

Об'єкт `Path` дає зручний доступ до складників шляху:

```python
from pathlib import Path

p = Path("data/reports/report.csv")

p.name      # "report.csv"   — ім'я файлу з розширенням
p.stem      # "report"       — ім'я БЕЗ розширення
p.suffix    # ".csv"         — розширення (з крапкою!)
p.parent    # Path("data/reports") — батьківська тека
p.parts     # ("data", "reports", "report.csv") — усі частини
```

Запам'ятайте різницю: `name` = ім'я з розширенням, `stem` = ім'я без розширення.

---

### 4. Перевірки

Перш ніж читати файл, перевірте, що він існує:

```python
from pathlib import Path

p = Path("data/app.log")

p.exists()   # True якщо шлях існує (файл АБО тека)
p.is_file()  # True якщо це файл
p.is_dir()   # True якщо це тека
```

Ці методи не кидають виняток, якщо шляху немає — просто повертають `False`.

---

### 5. Робота з файлами

`pathlib` вміє читати й писати файли без явного `open()`:

```python
from pathlib import Path

p = Path("data/report.txt")

# Записати текст (створює або перезаписує файл)
p.write_text("Hello, QA!", encoding="utf-8")

# Прочитати весь текст
content = p.read_text(encoding="utf-8")
```

Щоб створити вкладену теку, використовують `mkdir` з прапорцями:

```python
Path("data/logs/2026").mkdir(parents=True, exist_ok=True)
```

- `parents=True` — створює всі проміжні теки (`data`, `data/logs`)
- `exist_ok=True` — не кидає помилку, якщо тека вже є

---

### 6. Ітерація по теці

```python
from pathlib import Path

folder = Path("data")

# Усі елементи теки (файли + підтеки)
for item in folder.iterdir():
    print(item)

# Тільки .txt файли у цій теці
for txt in folder.glob("*.txt"):
    print(txt)

# Рекурсивно у всіх підтеках
for json_file in folder.rglob("*.json"):
    print(json_file)
```

- `iterdir()` — прямі елементи теки
- `glob(pattern)` — за шаблоном у цій теці
- `rglob(pattern)` — те саме, але рекурсивно вглиб

---

### 7. У QA automation

`pathlib` щодня потрібен для роботи з тест-даними:

```python
from pathlib import Path

TEST_DATA = Path(__file__).parent / "test_data"

# Зібрати всі JSON-фікстури
fixtures = list(TEST_DATA.glob("*.json"))

# Прочитати конкретний файл даних
users = (TEST_DATA / "users.json").read_text(encoding="utf-8")

# Знайти всі скріншоти в усіх підтеках
screenshots = list(Path("reports").rglob("*.png"))
```

---

## ⚠️ Типові помилки

### Конкатенація шляхів рядком

```python
# ❌ Крихко і не крос-платформно
path = "data" + "/" + "app.log"

# ✅ Оператор /
path = Path("data") / "app.log"
```

### Плутанина name та stem

```python
p = Path("report.csv")

# ❌ Думати, що name — без розширення
p.name   # "report.csv" — З розширенням!

# ✅ Для імені без розширення
p.stem   # "report"
```

### Забути parents=True при вкладеній теці

```python
# ❌ FileNotFoundError, якщо "data" ще немає
Path("data/logs").mkdir()

# ✅ Створює всі проміжні теки
Path("data/logs").mkdir(parents=True, exist_ok=True)
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-52-os-and-sys`
