# Вправи — Lesson 4: Test Discovery

---

## 🏋️ Вправа 1: Що знайде pytest? (EASY) — ручна демонстрація

**Файл:** `exercise_1_what_pytest_finds.py`

Це вправа на розуміння discovery. Вона **не перевіряється автоматично** через `test_exercises.py` — ви перевіряєте її самі.

Подивіться на код у файлі та спрогнозуйте: які функції pytest знайде, а які — ні.

```python
def test_a():
    assert True

def a_test():
    assert True

def check():
    assert True

def test_b():
    assert True

def verify_test():
    assert True
```

**Завдання:**
1. Спочатку запишіть свій прогноз: скільки тестів знайде pytest?
2. Запустіть: `pytest exercise_1_what_pytest_finds.py -v`
3. Порівняйте результат з вашим прогнозом
4. Заповніть блок `ВІДПОВІДЬ` у файлі

---

## 🏋️ Вправа 2: Створити тестовий файл (EASY)

**Завдання:** Створіть структуру і напишіть тести.

```
my_project/
├── src/
│   ├── __init__.py
│   └── math_utils.py
└── tests/
    ├── __init__.py
    └── test_math_utils.py
```

`src/math_utils.py`:
```python
def square(n):
    """Піднести до квадрату."""
    return n ** 2

def is_positive(n):
    """Перевірити чи число позитивне."""
    return n > 0

def absolute(n):
    """Повернути абсолютне значення."""
    return abs(n)
```

`tests/test_math_utils.py` — напишіть мінімум 3 тести (по одному на кожну функцію).

Перевірте:
```bash
cd my_project
pytest --collect-only
pytest -v
```

---

## 🏋️ Вправа 3: Тестовий клас (EASY)

**Завдання:** Додайте в `tests/test_math_utils.py` клас `TestSquare` з тестами:

```python
class TestSquare:
    def test_positive(self):
        # TODO: замініть pass на: assert square(3) == 9
        pass

    def test_zero(self):
        # TODO: замініть pass на: assert square(0) == 0
        pass

    def test_negative(self):
        # TODO: замініть pass на: assert square(-4) == 16
        pass
```

Перевірте через `pytest --collect-only` — мають бути і функції, і клас.

---

## 🏋️ Вправа 4: collect-only (MEDIUM)

**Завдання:** Запустіть `pytest --collect-only` з папки `my_project/` і дайте відповіді:

```bash
cd my_project
pytest --collect-only
```

1. Скільки тестів знайдено всього?
2. Які файли pytest знайшов?
3. Як відображаються тести з класу TestSquare порівняно з простими функціями?
4. Як виглядає повний шлях тесту з класу? (наприклад `tests/test_math_utils.py::TestSquare::test_positive`)

---

## 🏋️ Вправа 5: Зламати discovery (MEDIUM) — ручна демонстрація

**Завдання:** Створіть файл з **неправильною** назвою і переконайтесь що pytest його не бачить.

Ця вправа — **ручна демонстрація через `pytest --collect-only`**. Автоматична перевірка (`test_exercises.py`) оцінює вже фінальний результат у Вправі 6.

1. Створіть `tests/math_checks.py`:
   ```python
   def test_square_five():
       assert 5 ** 2 == 25
   ```

2. Запустіть:
   ```bash
   pytest --collect-only
   ```

3. Переконайтесь: тест з `math_checks.py` **НЕ** з'явився у списку.

**Чому?** Файл не відповідає патерну `test_*.py` і не відповідає `*_test.py`.

---

## 🏋️ Вправа 6: Виправити discovery (MEDIUM)

**Завдання:** Виправте проблему з Вправи 5.

1. Перейменуйте `tests/math_checks.py` → `tests/test_math_checks.py`
2. Запустіть:
   ```bash
   pytest --collect-only
   ```
3. Переконайтесь: тепер pytest **бачить** новий тест.

---

## ✅ Перевірка

```bash
pytest test_exercises.py -v
```

### Критерії:

- [ ] `my_project/tests/test_math_utils.py` існує
- [ ] Є мінімум 3 тестові функції
- [ ] Є клас `TestSquare` з мінімум 3 методами
- [ ] Всі тести містять `assert`
- [ ] `my_project/tests/test_math_checks.py` існує (виправлена назва)
- [ ] Функції `square`, `is_positive`, `absolute` працюють коректно