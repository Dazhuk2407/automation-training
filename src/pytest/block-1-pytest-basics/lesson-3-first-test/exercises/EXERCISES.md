# Вправи — Lesson 3: Перший тест у проєкті

Всі вправи використовують структуру `src/` + `tests/`.
Створюйте файли в папці `my_project/` всередині `exercises/`.

---

## 🏋️ Вправа 1: Перший реальний тест (EASY)

**Завдання:** Створіть калькулятор і напишіть перші тести.

### Крок 1 — Структура

```
my_project/
├── src/
│   ├── __init__.py
│   └── calculator.py
└── tests/
    ├── __init__.py
    └── test_calculator.py
```

### Крок 2 — Код

`src/calculator.py`:
```python
def add(a, b):
    """Додати два числа."""
    return a + b


def subtract(a, b):
    """Відняти b від a."""
    return a - b
```

### Крок 3 — Тести

`tests/test_calculator.py`:
```python
from src.calculator import add, subtract


def test_add():
    # TODO: замініть pass на: assert add(2, 3) == 5
    pass


def test_subtract():
    # TODO: замініть pass на: assert subtract(10, 4) == 6
    pass
```

### Крок 4 — Запуск

```bash
cd my_project
pytest -v
```

**Очікуваний результат:** `2 passed`

---

## 🏋️ Вправа 2: Edge cases (EASY)

**Завдання:** Додайте тести для граничних випадків.

Допишіть у `tests/test_calculator.py`:

```python
def test_add_zeros():
    # TODO: замініть pass на: assert add(0, 0) == 0
    pass


def test_add_negative():
    # TODO: замініть pass на: assert add(-1, -1) == -2
    pass


def test_subtract_from_zero():
    # TODO: замініть pass на: assert subtract(0, 5) == -5
    pass
```

**Очікуваний результат:** `5 passed`

---

## 🏋️ Вправа 3: Нова функція + тести (MEDIUM)

**Завдання:** Додайте функцію `multiply` та напишіть для неї тести.

### Крок 1

Додайте в `src/calculator.py`:
```python
def multiply(a, b):
    """Помножити два числа."""
    return a * b
```

### Крок 2

Додайте в `tests/test_calculator.py`:
```python
from src.calculator import add, subtract, multiply


def test_multiply_positive():
    # TODO: замініть pass на: assert multiply(3, 4) == 12
    pass


def test_multiply_by_zero():
    # TODO: замініть pass на: assert multiply(100, 0) == 0
    pass
```

**Очікуваний результат:** `7 passed`

---

## 🏋️ Вправа 4: Запуск та аналіз (MEDIUM)

**Завдання:** Запустіть всі тести та проаналізуйте вивід.

```bash
cd my_project
pytest -v
```

Дайте відповідь:

1. Скільки тестів виконалось?
2. Які функції тестуються? (add, subtract, multiply)
3. Який повний шлях першого тесту? (наприклад `tests/test_calculator.py::test_add`)
4. Що означає `[14%]`, `[28%]` і т.д. у виводі?

---

## ✅ Перевірка

Запустіть автоматичну перевірку з папки `exercises/`:

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] `src/calculator.py` існує з функціями add, subtract, multiply
- [ ] `tests/test_calculator.py` існує з тестами
- [ ] Всі тести містять `assert` (не `pass`)
- [ ] Функції повертають правильні результати
- [ ] `pytest` проходить без помилок