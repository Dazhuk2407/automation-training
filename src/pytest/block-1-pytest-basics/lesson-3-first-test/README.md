# Lesson 3: Перший тест у проєкті

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Створити код у `src/` та тест у `tests/`
- ✅ Імпортувати функцію з `src/` у тестовий файл
- ✅ Написати та запустити реальний тест
- ✅ Зрозуміти вивід pytest у контексті проєкту

---

## 📋 Передумови

Ви вже знаєте:
- Що таке pytest, assert, pytest.raises (Lesson 0)
- Як встановити pytest (Lesson 1)
- Як виглядає структура проєкту (Lesson 2)

Тепер ми **з'єднаємо все разом** і напишемо перший реальний тест.

---

## 📖 Теорія

### 1. Що ми будемо робити

Повний цикл:

```
1. Створити функцію в src/calculator.py
2. Створити тест у tests/test_calculator.py
3. Імпортувати функцію у тест
4. Написати assert
5. Запустити pytest
6. Побачити PASSED
```

Це те, що ви робитимете щодня як QA Automation Engineer.

---

### 2. Крок 1 — Код у src/

Створіть файл `src/calculator.py`:

```python
def add(a, b):
    """Додати два числа."""
    return a + b


def subtract(a, b):
    """Відняти b від a."""
    return a - b
```

Це код, який ми будемо тестувати. У реальному проєкті цей код пише розробник, а ви — тести.

---

### 3. Крок 2 — Тест у tests/

Створіть файл `tests/test_calculator.py`:

```python
from src.calculator import add, subtract


def test_add():
    """add(2, 3) повинна повернути 5."""
    result = add(2, 3)
    assert result == 5


def test_subtract():
    """subtract(10, 4) повинна повернути 6."""
    result = subtract(10, 4)
    assert result == 6
```

**Зверніть увагу:**
- Імпорт з `src.calculator` — ми тестуємо реальний модуль, а не копіюємо код у тест
- Кожен тест — окрема функція з одним `assert`
- Назви тестів описують **що перевіряється**

---

### 4. Крок 3 — Запуск

З кореня проєкту:

```bash
pytest
```

Вивід:

```
tests/test_calculator.py::test_add PASSED       [50%]
tests/test_calculator.py::test_subtract PASSED   [100%]

===================== 2 passed in 0.01s =====================
```

- `PASSED` — тест пройшов, функція працює правильно
- `2 passed` — обидва тести успішні
- `tests/test_calculator.py::test_add` — повний шлях до тесту

---

### 5. Імпорт з src — як це працює

```python
from src.calculator import add, subtract
```

Щоб цей імпорт працював, потрібно:
1. `src/__init__.py` — існує (порожній файл)
2. `tests/__init__.py` — існує (порожній файл)
3. Запускати `pytest` з **кореня проєкту** (де лежить `src/`)

Якщо імпорт не працює — перевірте ці три речі.

---

### 6. Структура тесту: Arrange → Act → Assert

Кожен хороший тест складається з трьох частин:

```python
def test_add_positive():
    # Arrange — підготовка даних
    a = 3
    b = 5

    # Act — виконання дії
    result = add(a, b)

    # Assert — перевірка результату
    assert result == 8
```

Для простих тестів це можна записати в один рядок:

```python
def test_add_positive():
    assert add(3, 5) == 8
```

Обидва варіанти правильні. Використовуйте Arrange-Act-Assert коли тест складніший.

---

## ⚠️ Типові помилки

| Помилка | Причина | Рішення |
|---------|---------|---------|
| `ModuleNotFoundError: No module named 'src'` | Немає `__init__.py` або запуск не з кореня | Створіть `src/__init__.py`, запускайте `pytest` з папки проєкту |
| `ImportError` | Неправильний шлях імпорту | Перевірте: `from src.calculator import add` |
| `0 items collected` | Тестовий файл не починається з `test_` | Перейменуйте файл: `test_calculator.py` |

---

## 💡 Приклади

Див. папку `examples/` — готовий міні-проєкт з тестами.

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-4-test-discovery` — як pytest знаходить тести