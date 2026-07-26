# Lesson 55: Modules and Packages

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Розуміти, що **модуль** — це будь-який `.py` файл
- ✅ Створювати власний модуль і імпортувати з нього функції
- ✅ Розуміти, що **пакет** — це тека з `__init__.py`
- ✅ Імпортувати з пакета (`from package.module import name`)
- ✅ Використовувати `if __name__ == "__main__":`

---

## 📋 Передумови

Ви вже знаєте:
- Import system: import / from-import / as (Lesson 34)
- Функції (Lesson 26-29)

Цей урок — про **створення власних** модулів і пакетів, а не лише про синтаксис імпорту.

---

## 📖 Теорія

### 1. Модуль = .py файл

Будь-який твій файл — це модуль. Файл `helpers.py` з функціями можна імпортувати:

```python
# helpers.py
def greet(name):
    return f"Hello, {name}"

# інший файл
import helpers
helpers.greet("Alice")   # "Hello, Alice"
```

---

### 2. Способи імпорту (рефреш з Lesson 34)

```python
import helpers                    # helpers.greet(...)
from helpers import greet         # greet(...)
from helpers import greet as g     # g(...)
```

---

### 3. `if __name__ == "__main__":`

`__name__` дорівнює `"__main__"`, коли файл запускають напряму, і імені модуля — коли його **імпортують**. Код під цим guard не виконується при імпорті:

```python
# helpers.py
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    # виконається лише при `python helpers.py`, не при import
    print(greet("World"))
```

---

### 4. Пакет = тека з `__init__.py`

Пакет групує пов'язані модулі. Мінімальна структура:

```
mypackage/
├── __init__.py       # робить теку пакетом
├── calc.py
└── strings.py
```

Файл `__init__.py` може бути порожнім або реекспортувати імена.

---

### 5. Імпорт із пакета

```python
from mypackage.calc import add        # конкретна функція
from mypackage import calc            # цілий модуль
import mypackage.strings as strings

add(2, 3)                # 5
calc.multiply(2, 4)      # 8
```

Якщо `__init__.py` містить `from .calc import add`, то доступно й `from mypackage import add`.

---

### 6. У QA

Тестовий фреймворк організовують у пакети: `pages/` (Page Objects), `api/` (клієнти), `helpers/` (утиліти). Це тримає код структурованим і повторно використовуваним.

---

## ⚠️ Типові помилки

### Код верхнього рівня виконується при імпорті

```python
# ❌ print("loaded")  на верхньому рівні спрацює при кожному import
# ✅ сховай демо-код під  if __name__ == "__main__":
```

### Плутати модуль і пакет

```python
# модуль = файл (calc.py) ; пакет = тека з __init__.py (mypackage/)
```

### Циклічні імпорти

Якщо `a.py` імпортує `b.py`, а `b.py` — `a.py`, буде помилка імпорту. Розривайте цикл, виносячи спільне у третій модуль.

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-56-pip-and-requirements`
