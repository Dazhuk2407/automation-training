# Lesson 52: Робота з os та sys

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Читати змінні оточення через `os.getenv()` / `os.environ`
- ✅ Безпечно давати дефолт для env var (без `KeyError`)
- ✅ Працювати з `os.path` (`basename`, `join`, `splitext`) і знати, що `pathlib` сучасніший
- ✅ Використовувати `sys.argv`, `sys.path`, `sys.exit()`, `sys.platform`
- ✅ Розуміти, навіщо env vars у QA (конфіг без хардкоду)

---

## 📋 Передумови

Ви вже знаєте:
- `pathlib` та роботу зі шляхами (Lesson 51)
- Функції, параметри, default-значення (Lesson 28)

---

## 📖 Теорія

### 1. os.environ та os.getenv — безпечне читання env vars

`os.environ` — це dict-подібний обʼєкт з усіма змінними оточення:

```python
import os

os.environ["HOME"]        # значення або KeyError, якщо змінної немає
```

`os.getenv("KEY", default)` — **безпечне** читання з дефолтом:

```python
import os

# Якщо BASE_URL немає — повернеться дефолт, без винятку
base_url = os.getenv("BASE_URL", "http://localhost")
timeout = int(os.getenv("TIMEOUT", "30"))
```

Правило: у коді читайте env vars **тільки** через `os.getenv` з дефолтом, якщо змінна не обовʼязкова.

---

### 2. Навіщо env vars у QA — конфіг без хардкоду (це безпека)

Тести часто мають конфіг: `BASE_URL`, `TIMEOUT`, `API_TOKEN`. Зберігати їх у коді — погано:

```python
# ❌ Хардкод — не гнучко і НЕБЕЗПЕЧНО (секрет у коді потрапить у git)
API_TOKEN = "super-secret-real-token"

# ✅ Читаємо з оточення — код чистий, секрет не в репозиторії
API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = os.getenv("BASE_URL", "http://localhost")
```

Переваги:
- Один код працює на dev / staging / CI — змінюємо лише env vars.
- **Секрети (токени, паролі) ніколи не потрапляють у код і git.**

---

### 3. os.path — робота зі шляхами (коротко)

`os.path` — класичний спосіб працювати зі шляхами як з рядками:

```python
import os

path = "/home/user/report.txt"

os.path.basename(path)   # "report.txt"
os.path.dirname(path)    # "/home/user"
os.path.splitext(path)   # ("/home/user/report", ".txt")
os.path.join("logs", "run", "out.log")  # "logs/run/out.log"
os.path.exists(path)     # True / False
```

> 💡 Для нового коду зручніший `pathlib` (Lesson 51): `Path(path).name`, `Path(path).suffix`, `Path("logs") / "run"`. `os.path` варто знати, бо він скрізь у старому коді.

---

### 4. Інше з os — поточна директорія та вміст (оглядово)

```python
import os

os.getcwd()          # поточна робоча директорія
os.listdir(".")      # список файлів/папок у директорії
os.sep               # роздільник шляху ("/" або "\\")
```

---

### 5. Модуль sys

`sys` дає доступ до інтерпретатора та середовища запуску:

```python
import sys

sys.argv          # список аргументів; sys.argv[0] — імʼя скрипта
sys.path          # список шляхів пошуку модулів
sys.platform      # "darwin" / "linux" / "win32"
sys.version_info  # (major, minor, ...) — версія Python
sys.exit(0)       # завершити скрипт з кодом (0 — успіх, ≠0 — помилка)
```

`sys.argv` детально розглянемо в Lesson 59. Головне зараз:
- `sys.argv[0]` — це **імʼя скрипта**, а не перший аргумент.
- Аргументи починаються з `sys.argv[1]`.

```python
# python run.py smoke fast
# sys.argv == ["run.py", "smoke", "fast"]
```

---

### 6. У QA: env vars + визначення платформи

```python
import os
import sys

def get_config():
    """Конфіг тестів з оточення, з безпечними дефолтами."""
    return {
        "base_url": os.getenv("BASE_URL", "http://localhost"),
        "timeout": int(os.getenv("TIMEOUT", "30")),
        "token": os.getenv("API_TOKEN"),  # без дефолту: секрет обовʼязково з env
    }


def is_windows():
    """Пропустити частину тестів залежно від платформи."""
    return sys.platform.startswith("win")
```

---

## ⚠️ Типові помилки

### os.environ["KEY"] замість os.getenv

```python
# ❌ KeyError, якщо змінної немає
timeout = os.environ["TIMEOUT"]

# ✅ Безпечно з дефолтом
timeout = os.getenv("TIMEOUT", "30")
```

### Хардкод секретів замість env vars

```python
# ❌ Секрет у коді — потрапить у git
token = "real-token-123"

# ✅ Читаємо з оточення
token = os.getenv("API_TOKEN")
```

### Плутати sys.argv[0] з аргументами

```python
# ❌ sys.argv[0] — це імʼя скрипта, а не перший аргумент
first_arg = sys.argv[0]

# ✅ Аргументи починаються з індексу 1
first_arg = sys.argv[1]
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-53-dates-and-time`
