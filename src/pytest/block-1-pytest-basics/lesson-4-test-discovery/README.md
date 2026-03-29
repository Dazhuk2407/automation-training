# Lesson 4: Як pytest знаходить тести (Test Discovery)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Називати файли, функції та класи так, щоб pytest знаходив їх автоматично
- ✅ Використовувати `pytest --collect-only` для дебагу discovery
- ✅ Групувати тести в класи
- ✅ Діагностувати чому pytest не бачить тест

---

## 📖 Теорія

### 1. Як pytest реально шукає тести

Коли ви запускаєте `pytest`, він автоматично сканує проєкт за такими правилами:

**Файли** — назва відповідає патерну `test_*.py` або `*_test.py`:

```
tests/
├── test_calculator.py        ✅ знайде (test_*.py)
├── calculator_test.py        ✅ знайде (*_test.py)
├── calculator.py             ❌ НЕ знайде
├── testcalculator.py         ❌ НЕ знайде (немає підкреслення)
└── my_tests.py               ❌ НЕ знайде (не test_*.py і не *_test.py)
```

**Функції** — назва починається з `test_`:

```python
def test_add():        # ✅ знайде
    assert 2 + 2 == 4

def add_test():        # ❌ НЕ знайде
    assert 2 + 2 == 4

def check_add():       # ❌ НЕ знайде
    assert 2 + 2 == 4
```

**Класи** — назва починається з `Test`, **без `__init__`**:

```python
class TestCalculator:  # ✅ знайде
    def test_add(self):
        assert 2 + 2 == 4

class Calculator:      # ❌ НЕ знайде (не починається з Test)
    def test_add(self):
        assert 2 + 2 == 4
```

---

### 2. pytest --collect-only (головний інструмент дебагу)

Команда `--collect-only` показує **що pytest знайшов**, але **не запускає** тести:

```bash
pytest --collect-only
```

Вивід:

```
<Module tests/test_calculator.py>
  <Function test_add>
  <Function test_subtract>
<Module tests/test_edge_cases.py>
  <Function test_add_zeros>
  <Function test_add_negative>

4 tests collected
```

**Коли використовувати:**
- Pytest каже `0 items collected` — перевірте що він бачить
- Додали новий тестовий файл — переконайтесь що pytest його знайшов
- Підозрюєте проблему з назвами — швидко перевірити

Це перший інструмент, до якого ви звертаєтесь коли "тести не запускаються".

---

### 3. Тестові класи

Клас — це спосіб **логічно згрупувати** пов'язані тести:

```python
from src.calculator import add, subtract


class TestAdd:
    """Тести для функції add."""

    def test_positive(self):
        assert add(2, 3) == 5

    def test_negative(self):
        assert add(-1, -1) == -2

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    """Тести для функції subtract."""

    def test_positive(self):
        assert subtract(10, 4) == 6

    def test_to_negative(self):
        assert subtract(3, 10) == -7
```

**Переваги класів:**
- Групування: всі тести для `add` — в `TestAdd`, для `subtract` — в `TestSubtract`
- Читабельність: зрозуміло що до чого відноситься
- Вивід pytest: `TestAdd::test_positive`, `TestSubtract::test_positive` — не плутаються

**Чому без `__init__`:**
pytest сам створює екземпляри тестових класів. Якщо додати `__init__`, pytest може не розпізнати клас як тестовий.

**Коли використовувати класи, а коли функції:**
- Мало тестів у файлі (3-5) → функції достатньо
- Багато тестів для різних функцій → групуйте в класи

---

### 4. Рекурсивний пошук

Pytest шукає тести **рекурсивно** — заходить у всі підпапки:

```
tests/
├── test_calculator.py          ✅ знайде
├── unit/
│   └── test_math.py            ✅ знайде
└── integration/
    └── test_api.py             ✅ знайде
```

Можна запускати тести з конкретної папки:

```bash
pytest tests/unit/          # тільки unit тести
pytest tests/integration/   # тільки integration тести
pytest tests/               # всі тести
```

---

### 5. Зв'язок discovery та pytest.ini

Правила discovery можна змінити через `pytest.ini`:

```ini
[pytest]
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*
```

Це стандартні значення — pytest використовує їх за замовчуванням, навіть якщо `pytest.ini` не існує. Їх можна перевизначити (наприклад, додати `check_*.py`), але для початківців краще дотримуватись стандартних конвенцій.

**Про `tests/__init__.py`:** цей файл не є обов'язковим для pytest. Pytest знайде тести і без нього. Але в навчальному курсі ми додаємо його для стабільності імпортів між тестовими файлами та більш передбачуваної структури.

---

### 6. Коли pytest НЕ бачить тест — чеклист

Якщо `pytest --collect-only` показує `0 items collected`:

| Перевірте | Правило |
|-----------|---------|
| Назва файлу | відповідає `test_*.py` або `*_test.py` |
| Назва функції | починається з `test_` |
| Назва класу | починається з `Test`, без `__init__` |
| Метод класу | починається з `test_` |
| Розташування | pytest запущений з правильної директорії |
| `pytest.ini` → `testpaths` | вказує на правильну папку |

---

## ⚠️ Типові помилки

| Помилка | Чому не працює |
|---------|---------------|
| `testcalculator.py` | Немає підкреслення: потрібно `test_calculator.py` |
| `def add_test():` | Не починається з `test_`: потрібно `test_add()` |
| `class Calculator_Test:` | Не починається з `Test`: потрібно `TestCalculator` |
| `class TestCalc:` з `__init__` | pytest не створить екземпляр |

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-5-simple-tests` — написання різних тестів