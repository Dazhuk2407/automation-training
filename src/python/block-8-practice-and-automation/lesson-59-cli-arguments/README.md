# Lesson 59: Command-Line Arguments (argparse)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати `ArgumentParser`
- ✅ Додавати позиційні аргументи та опції (`--flag`)
- ✅ Задавати `type`, `default`, `choices`, `required`
- ✅ Використовувати `action="store_true"` для булевих прапорців
- ✅ Парсити аргументи у скрипті через `parse_args()`

---

## 📋 Передумови

Ви вже знаєте:
- `os` та `sys`, зокрема `sys.argv` (Lesson 52)
- Функції та повернення значень (Lesson 29)

---

## 📖 Теорія

### 1. Навіщо argparse замість ручного розбору sys.argv

Можна читати `sys.argv` вручну, але це швидко перетворюється на біль:

```python
import sys

# ❌ Ручний розбір: крихкий і без валідації
args = sys.argv[1:]           # ['--env', 'prod', '--retries', '3']
env = "dev"
if "--env" in args:
    env = args[args.index("--env") + 1]
retries = args[args.index("--retries") + 1]  # це рядок "3", не int!
```

`argparse` вирішує все це за вас:

- **валідація** — невідома опція чи пропущений `required` дає зрозумілу помилку;
- **`--help`** генерується автоматично;
- **типи** — `type=int` одразу конвертує рядок у число;
- **дефолти, choices** — описуються декларативно.

---

### 2. Базове використання

Три кроки: створити parser, додати аргумент, розпарсити.

```python
import argparse

parser = argparse.ArgumentParser(description="Привітати користувача")
parser.add_argument("name")          # позиційний аргумент
args = parser.parse_args()           # читає sys.argv

print(f"Hello, {args.name}!")
```

Запуск:

```bash
python greet.py Alice
# Hello, Alice!
```

Позиційний аргумент **обовʼязковий** за замовчуванням. Якщо його не передати — argparse виведе помилку і `usage`.

---

### 3. Опції: default, type, choices, required

Опції починаються з `--` і за замовчуванням **необовʼязкові**:

```python
parser.add_argument("--env", default="dev")            # рядок з дефолтом
parser.add_argument("--retries", type=int, default=0)  # конвертація у int
parser.add_argument("--browser", choices=["chrome", "firefox"])  # тільки з набору
parser.add_argument("--token", required=True)          # зробити обовʼязковою
```

- `default` — значення, якщо опцію не передали;
- `type=int` — argparse викличе `int(value)` і впаде з помилкою на нечислове;
- `choices=[...]` — дозволені лише перелічені значення;
- `required=True` — опція стає обовʼязковою.

---

### 4. Прапорці: action="store_true"

Булевий прапорець не потребує значення — сама його наявність вмикає `True`:

```python
parser.add_argument("--verbose", action="store_true")
parser.add_argument("--headless", action="store_true")
```

```bash
python run.py --verbose        # args.verbose == True
python run.py                  # args.verbose == False
```

За замовчуванням `store_true` дає `False`, коли прапорця немає.

---

### 5. Доступ до значень. Кілька аргументів

Після `parse_args()` значення доступні як атрибути обʼєкта `args`:

```python
parser = argparse.ArgumentParser()
parser.add_argument("suite")
parser.add_argument("--env", default="dev")
parser.add_argument("--retries", type=int, default=0)

args = parser.parse_args()
print(args.suite)     # позиційний
print(args.env)       # опція
print(args.retries)   # int
```

⚠️ Дефіс у назві опції стає підкресленням в атрибуті: `--dry-run` → `args.dry_run`.

---

### 6. У QA automation: скрипт-раннер тестів

Типовий приклад — раннер, який приймає набір тестів, середовище та режим:

```python
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="QA test runner")
    parser.add_argument("--suite", default="smoke",
                        choices=["smoke", "regression", "full"])
    parser.add_argument("--env", default="dev",
                        choices=["dev", "staging", "prod"])
    parser.add_argument("--retries", type=int, default=0)
    parser.add_argument("--headless", action="store_true")
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    print(f"Running {args.suite} on {args.env}, headless={args.headless}")
```

```bash
python runner.py --suite regression --env staging --retries 2 --headless
```

Винесення побудови у `build_parser()` робить код **тестованим**: у тестах ми викликаємо `build_parser().parse_args([...])` зі списком, не чіпаючи реальний командний рядок.

---

## ⚠️ Типові помилки

### Плутати позиційні й опційні аргументи

```python
# ❌ "env" тут позиційний і обовʼязковий
parser.add_argument("env")

# ✅ Опція з дефолтом
parser.add_argument("--env", default="dev")
```

### Забути type=int — усе приходить рядком

```python
# ❌ args.retries == "3" (рядок!)
parser.add_argument("--retries", default=0)

# ✅ args.retries == 3 (int)
parser.add_argument("--retries", type=int, default=0)
```

### Дефіс стає підкресленням

```python
parser.add_argument("--dry-run", action="store_true")
# ❌ args.dry-run  → SyntaxError / AttributeError
# ✅ args.dry_run
```

### required для позиційних аргументів зайве

```python
# ❌ позиційні і так обовʼязкові — required тут помилка
parser.add_argument("name", required=True)

# ✅ просто
parser.add_argument("name")
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-60-file-paths`
