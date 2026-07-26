# Lesson 60: Relative and Absolute File Paths

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розрізняти абсолютні й відносні шляхи (`Path.is_absolute()`)
- ✅ Розуміти роль поточної робочої директорії (cwd) і чому відносні шляхи ненадійні
- ✅ Будувати шляхи відносно скрипта через `Path(__file__)`
- ✅ Нормалізувати та резолвити шляхи через `resolve()`
- ✅ Безпечно з'єднувати шляхи й уникати path traversal (`../`)

---

## 📋 Передумови

Ви вже знаєте:
- `pathlib` та об'єкт `Path` (Lesson 51)
- Модулі `os` та `sys` (Lesson 52)

---

## 📖 Теорія

### 1. Абсолютний vs відносний шлях

**Абсолютний** шлях повністю задає розташування від кореня файлової системи:
- Unix/macOS: `/home/user/data/logs.txt`
- Windows: `C:\Users\user\data\logs.txt`

**Відносний** шлях задається відносно поточної робочої директорії:
- `data/logs.txt`
- `../config/settings.ini`

Перевірити тип шляху можна через `Path.is_absolute()`:

```python
from pathlib import Path

Path("/home/user/data.txt").is_absolute()   # True
Path("data/logs.txt").is_absolute()          # False
Path("../config.ini").is_absolute()          # False
```

---

### 2. Поточна робоча директорія (cwd)

Відносні шляхи рахуються **від cwd** — теки, з якої запущено процес, а НЕ від файлу скрипта:

```python
from pathlib import Path

Path.cwd()   # напр. PosixPath('/Users/qa/project')
```

Коли ви пишете `open("data/logs.txt")`, Python шукає файл у `cwd / "data/logs.txt"`.
Тому один і той самий код працює по-різному залежно від того, ЗВІДКИ його запустили:

```bash
cd /Users/qa/project && python tests/run.py   # шукає /Users/qa/project/data/logs.txt
cd /Users/qa       && python project/tests/run.py  # шукає /Users/qa/data/logs.txt  ← інша тека!
```

Саме тому відносні шляхи **ламаються** в CI, IDE та cron — там cwd часто інша, ніж очікує розробник.

---

### 3. Надійний патерн: шлях відносно скрипта

Замість того щоб покладатися на cwd, будуйте шлях відносно **самого файлу скрипта** через `Path(__file__)`:

```python
from pathlib import Path

HERE = Path(__file__).parent          # тека, де лежить цей .py файл
data_file = HERE / "data" / "file.txt"
```

`__file__` — це шлях до поточного модуля. `.parent` дає його теку.
Такий шлях **не залежить від cwd** — він завжди вказує на ту саму директорію
відносно скрипта, звідки б ви його не запустили. Це стабільніше за відносні шляхи.

---

### 4. resolve() — нормалізований абсолютний шлях

`resolve()` перетворює будь-який шлях на **абсолютний нормалізований** — прибирає `..`, `.`
і робить шлях канонічним:

```python
from pathlib import Path

Path("/a/b/../c").resolve()      # PosixPath('/a/c')
Path("/a/./b/./c").resolve()     # PosixPath('/a/b/c')
Path("data/x.txt").resolve()     # абсолютний шлях від cwd
```

`resolve()` корисний, щоб порівнювати шляхи та бачити реальне розташування файлу.

---

### 5. Безпечне з'єднання та path traversal

З'єднуйте шляхи оператором `/`, а не конкатенацією рядків — це кросплатформно:

```python
base = Path("/srv/uploads")
target = base / "reports" / "q1.csv"   # ✅ /srv/uploads/reports/q1.csv
```

Небезпека — коли частина шляху приходить ззовні й містить `../` (path traversal):

```python
base = Path("/srv/uploads")
user_input = "../../etc/passwd"
(base / user_input).resolve()          # /etc/passwd  ← вихід за межі base!
```

Щоб убезпечитись, після `resolve()` перевіряйте, що результат **всередині** базової теки:

```python
def is_inside(base, candidate):
    base = Path(base).resolve()
    candidate = (base / candidate).resolve()
    return base in candidate.parents or candidate == base
```

---

### 6. У QA automation

Тест-дані треба шукати **відносно тесту**, а не відносно cwd — тоді тести
працюють однаково локально й у CI:

```python
from pathlib import Path

TEST_DIR = Path(__file__).parent
FIXTURES = TEST_DIR / "fixtures" / "users.json"

def test_load_users():
    assert FIXTURES.exists()   # стабільно, бо шлях від файлу тесту
```

---

## ⚠️ Типові помилки

### Покладатися на cwd

```python
# ❌ Ламається, коли CI запускає тест з іншої теки
open("fixtures/data.json")

# ✅ Шлях відносно файлу
open(Path(__file__).parent / "fixtures" / "data.json")
```

### Хардкодити абсолютні шляхи

```python
# ❌ Працює лише на одній машині
Path("/Users/ivan/project/data.txt")

# ✅ Відносно скрипта
Path(__file__).parent / "data.txt"
```

### Конкатенувати рядками замість "/"

```python
# ❌ Не кросплатформно, легко зламати роздільник
path = str(base) + "/" + "sub" + "/" + name

# ✅ Оператор /
path = base / "sub" / name
```

### Не резолвити "../"

```python
# ❌ ".." лишається, порівняння та перевірки ненадійні
Path("/srv/uploads/../etc")

# ✅ resolve() нормалізує
Path("/srv/uploads/../etc").resolve()   # /srv/etc
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-61-processing-test-data`
