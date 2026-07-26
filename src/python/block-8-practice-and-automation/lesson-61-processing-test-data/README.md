# Lesson 61: Processing Test Data, Logs, and Reports

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Парсити рядки логів у структуровані дані (dict)
- ✅ Фільтрувати й рахувати результати (pass/fail, за рівнем)
- ✅ Агрегувати результати (counts, pass rate)
- ✅ Формувати текстовий звіт за допомогою f-strings
- ✅ З'єднувати навички блоків (рядки, dict, f-strings, regex-lite)

---

## 📋 Передумови

Ви вже знаєте:
- Рядки та методи рядків, dict (Block 2)
- f-strings (Lesson 39)
- regex-lite (Lesson 40 — але тут можна обійтися `split`)

---

## 📖 Теорія

### 1. Тестові логи — це рядки

Результат прогону тестів часто зберігається як текст. Кожен рядок — окрема подія:

```python
line = "2024-01-15 INFO test_login PASSED"
```

Тут закодовано кілька полів: дата, рівень (`INFO`), ім'я тесту (`test_login`) та статус (`PASSED`). Наша робота — витягти ці поля й порахувати статистику.

Дані передаємо у функції як **список рядків** (`list[str]`), а не читаємо з файлу. Це робить функції чистими й легкими для тестування:

```python
logs = [
    "2024-01-15 INFO test_login PASSED",
    "2024-01-15 INFO test_logout FAILED",
    "2024-01-15 ERROR test_payment FAILED",
]
```

---

### 2. Парсинг рядка у dict

Найпростіший спосіб розбити рядок — `split()`. Без аргументів він ділить за будь-якою кількістю пробілів і прибирає порожні елементи:

```python
def parse_line(line):
    """Розбити лог-рядок у dict з полями."""
    date, level, test, status = line.strip().split()
    return {"date": date, "level": level, "test": test, "status": status}

parse_line("2024-01-15 INFO test_login PASSED")
# {"date": "2024-01-15", "level": "INFO", "test": "test_login", "status": "PASSED"}
```

Коли треба відділити лише частину, зручний `partition` — він завжди повертає три елементи:

```python
key, sep, value = "status=PASSED".partition("=")
# key="status", sep="=", value="PASSED"
```

---

### 3. Фільтрація і підрахунок

Порахувати рядки з певним статусом можна через генератор:

```python
def count_status(lines, status):
    """Скільки рядків завершується заданим статусом."""
    return sum(1 for ln in lines if ln.strip().endswith(status))

logs = ["test_a PASSED", "test_b FAILED", "test_c PASSED"]
count_status(logs, "PASSED")  # 2
count_status(logs, "FAILED")  # 1
```

Так само рахуємо за рівнем (`ERROR`, `WARNING`):

```python
def count_level(lines, level):
    return sum(1 for ln in lines if level in ln.split())
```

---

### 4. Агрегація

Агрегація — це зведення багатьох рядків до кількох чисел. Наприклад, **pass rate**:

```python
def pass_rate(lines):
    """Частка PASSED серед усіх рядків (0.0..1.0)."""
    total = len(lines)
    if total == 0:
        return 0.0
    passed = count_status(lines, "PASSED")
    return passed / total
```

Групування за статусом у dict `status -> count`:

```python
def count_by_status(lines):
    counts = {}
    for ln in lines:
        status = ln.strip().split()[-1]
        counts[status] = counts.get(status, 0) + 1
    return counts
```

---

### 5. Формування звіту

Фінальний крок — зробити з чисел людиночитабельний текст через f-strings:

```python
def summary_line(lines):
    """Однорядковий підсумок: 'PASSED: 2/3 (66.7%)'."""
    total = len(lines)
    passed = count_status(lines, "PASSED")
    rate = (passed / total * 100) if total else 0.0
    return f"PASSED: {passed}/{total} ({rate:.1f}%)"
```

Багаторядковий звіт:

```python
def build_report(lines):
    counts = count_by_status(lines)
    header = summary_line(lines)
    body = "\n".join(f"{status}: {n}" for status, n in counts.items())
    return f"{header}\n{body}"
```

---

### 6. У QA automation

Типовий сценарій: після нічного прогону є сирий лог на тисячі рядків. Ніхто не читатиме його повністю. Ваш скрипт перетворює лог у короткий summary для звіту або повідомлення у Slack:

```
PASSED: 847/900 (94.1%)
FAILED: 41
ERROR: 12
```

Такий підхід — основа dashboards, нотифікацій та quality gates у CI.

---

## ⚠️ Типові помилки

### Ділення на нуль коли total = 0

```python
# ❌ ZeroDivisionError на порожньому списку
def pass_rate(lines):
    return count_status(lines, "PASSED") / len(lines)

# ✅ Спершу перевірити total
def pass_rate(lines):
    total = len(lines)
    if total == 0:
        return 0.0
    return count_status(lines, "PASSED") / total
```

### Не робити strip() рядків

```python
# ❌ "  test PASSED\n" не завершується на "PASSED"
line.endswith("PASSED")

# ✅ прибрати пробіли й перенос рядка
line.strip().endswith("PASSED")
```

### Крихкий парсинг (припущення про фіксовані пробіли)

```python
# ❌ ламається на подвійних пробілах
line.split(" ")

# ✅ split() без аргументів ділить за будь-якими пробілами
line.split()
```

### Регістрозалежний підрахунок

```python
# ❌ "passed" != "PASSED"
status == "PASSED"

# ✅ нормалізувати регістр
status.upper() == "PASSED"
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-62-helper-scripts`
