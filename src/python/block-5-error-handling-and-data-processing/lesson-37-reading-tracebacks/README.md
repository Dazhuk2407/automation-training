# Lesson 37: Reading Tracebacks

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Читати traceback згори донизу і знаходити **реальне** місце помилки (останній рядок стеку)
- ✅ Розуміти тип винятку і повідомлення в останньому рядку
- ✅ Читати ланцюг викликів (call stack): функція A → B → C
- ✅ Використовувати модуль `traceback` для логування в `except`
- ✅ Локалізувати баг за traceback у падаючих тестах

---

## 📋 Передумови

Ви вже знаєте:
- Типи помилок і винятків (Lesson 36)
- Функції, аргументи, return (Lesson 26-34)

---

## 📖 Теорія

### 1. Що таке traceback і як його читати

**Traceback** — це «слід» (звіт), який Python друкує, коли виняток не був оброблений.
Він показує весь шлях викликів від точки старту до місця, де стався виняток.

Розглянемо приклад:

```
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    main()
  File "app.py", line 9, in main
    result = divide(10, 0)
  File "app.py", line 5, in divide
    return a / b
ZeroDivisionError: division by zero
```

Розбираємо рядок за рядком:

- `Traceback (most recent call last):` — заголовок. Ключова підказка: **most recent call last** означає, що найсвіжіший (найглибший) виклик — **внизу**.
- `File "app.py", line 12, in <module>` — де саме: файл, номер рядка, у якій функції (`<module>` = верхній рівень скрипта).
- Наступний рядок — сам код цього рядка (`main()`).
- Далі кожна пара рядків — це наступний вкладений виклик.
- **Останній рядок** — `ZeroDivisionError: division by zero` — це `тип_винятку: повідомлення`. Саме тут відповідь на питання «що зламалося».

---

### 2. Найважливіший рядок — ОСТАННІЙ

Читайте traceback **знизу вгору**, коли хочете швидко зрозуміти проблему:

1. **Найнижчий рядок** — тип винятку і повідомлення (`ZeroDivisionError: division by zero`). Це «діагноз».
2. **Передостанній блок `File ... line ...`** — місце, де виняток реально стався, і рядок вашого коду (`return a / b`).

Ці два факти майже завжди дають відповідь: *який* виняток і *де* саме.

```
...
  File "app.py", line 5, in divide   ← ДЕ впало (ваш код)
    return a / b
ZeroDivisionError: division by zero  ← ЩО впало (тип + меседж)
```

---

### 3. Ланцюг викликів (call stack)

Traceback показує, **як** програма дійшла до помилки. У прикладі вище:

```
<module>  →  main()  →  divide(10, 0)  →  a / b  💥
```

Це і є call stack: `main` викликав `divide`, а `divide` виконав ділення на нуль.
Верхні рядки — «звідки прийшли», нижні — «де зупинилися». Якщо баг не в останньому
рядку (наприклад, там код бібліотеки), піднімайтеся вгору до **першого рядка з вашим файлом**.

---

### 4. Модуль `traceback`: логування в `except`

Іноді потрібно не «впасти», а **залогувати** traceback і продовжити роботу.
Для цього є модуль `traceback` і функція `traceback.format_exc()`, яка повертає
весь traceback як рядок:

```python
import traceback

def safe_run(func):
    try:
        return func()
    except Exception:
        log = traceback.format_exc()
        # log містить тип винятку, повідомлення та весь стек
        return log
```

`format_exc()` повертає той самий текст, який Python надрукував би сам —
з назвою типу, повідомленням та іменами функцій у стеку.

---

### 5. Chained exceptions (ланцюжок винятків)

Якщо один виняток стався під час обробки іншого, Python показує **обидва**:

```
Traceback (most recent call last):
  ...
KeyError: 'user_id'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  ...
ValueError: invalid config
```

- `During handling of the above exception...` — новий виняток стався всередині `except`.
- `The above exception was the direct cause...` — з'являється при `raise ... from ...`.

У таких випадках читайте **найнижчий** traceback (те, що впало останнім), але
пам'ятайте про першопричину вище.

---

### 6. У QA automation: traceback з CI-логу

Коли тест падає в CI, у логу ви бачите traceback. Алгоритм читання:

1. Знайдіть **останній рядок** — тип винятку (`AssertionError`, `KeyError`, ...).
2. Підніміться до **рядка з іменем тесту** (`in test_login`) — це підкаже, *який* тест впав.
3. Знайдіть рядок з вашим кодом/асертом — це *чому* він впав.

```
  File "tests/test_login.py", line 21, in test_login
    assert response.status_code == 200
AssertionError: assert 500 == 200
```

Звідси одразу видно: тест `test_login`, асерт на статус-код, отримали `500` замість `200`.

---

## ⚠️ Типові помилки

### Читати traceback згори замість знизу

```python
# ❌ Дивитися лише на перший рядок "Traceback (most recent call last)"
#    і намагатися шукати помилку там

# ✅ Читати ОСТАННІЙ рядок (тип + меседж) і підніматися до свого коду
```

### Ігнорувати назву файлу і номер рядка

```python
# ❌ "Просто ValueError десь у коді"
# ✅ File "service.py", line 42, in parse — конкретний файл і рядок
```

### Панікувати від довжини стеку

```python
# ❌ 40 рядків стеку → "все зламалося, нічого не зрозуміло"
# ✅ Довгий стек = багато вкладених викликів (часто бібліотечних).
#    Шукайте ОСТАННІЙ рядок і НАЙНИЖЧИЙ рядок зі СВОЇМ файлом.
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-38-custom-exceptions`
