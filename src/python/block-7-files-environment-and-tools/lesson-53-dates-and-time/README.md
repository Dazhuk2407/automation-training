# Lesson 53: Робота з датами й часом (datetime)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створювати дати й час через `datetime` та `date`
- ✅ Форматувати дату у рядок через `strftime`
- ✅ Парсити дату з рядка через `strptime`
- ✅ Рахувати різницю між датами через `timedelta`
- ✅ Додавати й віднімати інтервали часу
- ✅ Розуміти, навіщо timestamps у логах і тестах

---

## 📋 Передумови

Ви вже знаєте:
- f-strings (Lesson 39)
- Функції та return values (Lesson 29)

---

## 📖 Теорія

### 1. datetime, date, time — що це

Модуль `datetime` містить кілька класів:

- `date` — лише дата (рік, місяць, день)
- `datetime` — дата **і** час (рік, місяць, день, година, хвилина, секунда)
- `timedelta` — інтервал (різниця) між двома моментами

Імпортуємо потрібне:

```python
from datetime import datetime, date, timedelta
```

---

### 2. Створення дат

Явно передаємо компоненти:

```python
from datetime import datetime, date

dt = datetime(2024, 1, 15, 10, 30)   # 2024-01-15 10:30:00
d = date(2024, 1, 15)                # 2024-01-15
```

Порядок аргументів: `year, month, day, hour, minute, second`. Час можна не вказувати — тоді буде `00:00:00`.

Поточний момент — `datetime.now()`:

```python
now = datetime.now()   # напр. 2026-07-26 14:05:33.123456
```

⚠️ `datetime.now()` повертає **різне** значення при кожному виклику. Тому у тестах **ніколи** не порівнюйте `now()` з фіксованим очікуваним значенням — тест стане недетермінованим. Максимум — перевіряйте тип: `isinstance(datetime.now(), datetime)`.

---

### 3. Атрибути дати

У об'єкта `datetime`/`date` є зручні атрибути:

```python
dt = datetime(2024, 1, 15, 10, 30, 0)

dt.year     # 2024
dt.month    # 1
dt.day      # 15
dt.hour     # 10
dt.minute   # 30

dt.weekday()  # 0 = понеділок, 6 = неділя (15.01.2024 — понеділок → 0)
```

`weekday()` — це **метод** (з дужками), а `year`/`month`/`day` — атрибути (без дужок).

---

### 4. Форматування: strftime (date → str)

`strftime` перетворює дату у **рядок** за шаблоном:

```python
dt = datetime(2024, 1, 15, 10, 30, 0)

dt.strftime("%Y-%m-%d")            # "2024-01-15"
dt.strftime("%H:%M:%S")            # "10:30:00"
dt.strftime("%Y-%m-%d %H:%M:%S")   # "2024-01-15 10:30:00"
```

Основні коди формату:

| Код  | Значення                | Приклад |
|------|-------------------------|---------|
| `%Y` | Рік (4 цифри)           | `2024`  |
| `%m` | Місяць (2 цифри)        | `01`    |
| `%d` | День (2 цифри)          | `15`    |
| `%H` | Година (24-год, 2 цифри)| `10`    |
| `%M` | Хвилина (2 цифри)       | `30`    |
| `%S` | Секунда (2 цифри)       | `00`    |

Мнемоніка: **strf**time = **str f**rom time (робимо рядок з дати).

---

### 5. Парсинг: strptime (str → datetime)

`strptime` — зворотна операція: з **рядка** робить `datetime`:

```python
from datetime import datetime

dt = datetime.strptime("2024-01-15", "%Y-%m-%d")
# datetime(2024, 1, 15, 0, 0)

dt = datetime.strptime("2024-01-15 10:30:00", "%Y-%m-%d %H:%M:%S")
# datetime(2024, 1, 15, 10, 30, 0)
```

Шаблон **мусить точно** відповідати рядку, інакше буде `ValueError`.

Мнемоніка: **strp**time = **str p**arse time (парсимо рядок у дату).

---

### 6. timedelta — інтервали часу

Різниця двох дат — це `timedelta`:

```python
from datetime import date, timedelta

d1 = date(2024, 1, 1)
d2 = date(2024, 1, 8)

diff = d2 - d1        # timedelta(days=7)
diff.days             # 7
```

Додавання й віднімання інтервалів:

```python
from datetime import datetime, timedelta

dt = datetime(2024, 1, 15, 10, 0, 0)

dt + timedelta(days=7)      # 2024-01-22 10:00:00
dt - timedelta(days=1)      # 2024-01-14 10:00:00
dt + timedelta(hours=3)     # 2024-01-15 13:00:00
```

Різниця двох `datetime` (не `date`) дає точний інтервал:

```python
start = datetime(2024, 1, 15, 10, 0, 0)
end = datetime(2024, 1, 15, 10, 0, 45)
(end - start).total_seconds()   # 45.0
```

---

### 7. У QA automation

**Timestamp у назві лог-файлу:**

```python
def log_filename(dt):
    return f"test_run_{dt.strftime('%Y-%m-%d_%H-%M-%S')}.log"

log_filename(datetime(2024, 1, 15, 10, 30, 0))
# "test_run_2024-01-15_10-30-00.log"
```

**Перевірка, що дата у діапазоні:**

```python
def is_in_range(dt, start, end):
    return start <= dt <= end
```

**Обчислення тривалості тесту:**

```python
def duration_seconds(start, end):
    return (end - start).total_seconds()
```

---

## ⚠️ Типові помилки

### Плутати strftime і strptime

```python
# ❌ strftime очікує datetime, а не рядок
# datetime.strftime("2024-01-15", "%Y-%m-%d")   # помилка

# ✅ рядок → datetime це strptime
dt = datetime.strptime("2024-01-15", "%Y-%m-%d")

# ✅ datetime → рядок це strftime
s = dt.strftime("%Y-%m-%d")
```

Запам'ятайте: **strp**arse (з рядка), **strf**ormat (у рядок).

### Невірний формат-код

```python
dt = datetime(2024, 1, 15)

# ❌ %m-%d-%Y дає американський формат "01-15-2024"
dt.strftime("%m-%d-%Y")   # "01-15-2024"

# ✅ ISO-формат
dt.strftime("%Y-%m-%d")   # "2024-01-15"
```

### Порівнювати naive і aware datetime

`naive` datetime не має інформації про часовий пояс, `aware` — має. Порівнювати їх напряму не можна — буде `TypeError`. У більшості QA-задач достатньо працювати з `naive` датами (без tzinfo) і бути послідовними.

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-54-random-data`
