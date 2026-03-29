# Lesson 7: Запуск тестів з командного рядка

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Запускати тести різними способами (всі, файл, один тест)
- ✅ Керувати виводом pytest (`-v`, `-q`, `-s`, `--tb`)
- ✅ Фільтрувати тести за назвою (`-k`)
- ✅ Контролювати зупинку при помилках (`-x`, `--maxfail`)
- ✅ Перевіряти що pytest знайшов (`--collect-only`)

---

## 📋 Передумови

Ви вже знаєте:
- Як писати тести та assertions (Lesson 5-6)
- Як pytest знаходить тести (Lesson 4)
- Структуру проєкту: `src/` + `tests/` (Lesson 2-3)

Тепер розберемо всі способи запуску тестів з CLI.

---

## 📖 Теорія

### 1. Базовий запуск

```bash
# Запустити всі тести
pytest

# Запустити всі тести у конкретній папці
pytest tests/

# Запустити один файл
pytest tests/test_calculator.py

# Запустити один тест
pytest tests/test_calculator.py::test_add

# Запустити метод класу
pytest tests/test_calculator.py::TestAdd::test_positive
```

---

### 2. Керування виводом

```bash
# -v (verbose) — детальний вивід: назва кожного тесту + PASSED/FAILED
pytest -v

# -vv — ще детальніший: повний diff при помилках
pytest -vv

# -q (quiet) — мінімальний вивід: тільки точки та підсумок
pytest -q

# -s — показувати print() у консолі (за замовчуванням pytest їх приховує)
pytest -s
```

**Приклад виводу `-v`:**
```
tests/test_calculator.py::test_add PASSED      [25%]
tests/test_calculator.py::test_subtract PASSED  [50%]
tests/test_calculator.py::test_multiply PASSED  [75%]
tests/test_calculator.py::test_divide PASSED    [100%]

4 passed in 0.02s
```

**Приклад виводу `-q`:**
```
....                                           [100%]
4 passed in 0.02s
```

---

### 3. Керування traceback

Коли тест падає, pytest показує traceback. Його рівень деталізації можна змінити:

```bash
# Короткий traceback (рекомендовано для повсякденної роботи)
pytest --tb=short

# Повний traceback
pytest --tb=long

# Без traceback (тільки назви)
pytest --tb=no

# Тільки один рядок
pytest --tb=line
```

---

### 4. Фільтрація за назвою (`-k`)

`-k` дозволяє запускати тести, які **містять** певне слово в назві:

```bash
# Тести, що містять "login" у назві
pytest -k "login"

# Тести, що НЕ містять "slow"
pytest -k "not slow"

# Тести, що містять "login" АБО "auth"
pytest -k "login or auth"

# Тести, що містять "test" І "add"
pytest -k "test and add"
```

`-k` шукає в повному шляху: `tests/test_auth.py::TestLogin::test_valid_password` — тому `pytest -k "Login"` знайде тести з класу `TestLogin`.

---

### 5. Контроль зупинки при помилках

```bash
# Зупинитися на першому падінні
pytest -x

# Зупинитися після 3 падінь
pytest --maxfail=3
```

**Коли це корисно:**
- `-x` — коли ви фіксите баг і хочете бачити тільки першу помилку
- `--maxfail=3` — коли запускаєте великий набір тестів і не хочете чекати до кінця якщо все зламалось

---

### 6. `--collect-only` — перевірити що pytest знайшов

```bash
pytest --collect-only
```

Показує список тестів **без запуску**. Корисно коли:
- Додали новий файл — перевірити що pytest його бачить
- `0 items collected` — зрозуміти що пішло не так
- Хочете побачити структуру тестів

---

### 7. Перезапуск failed тестів

```bash
# Запустити тільки тести, що впали минулого разу
pytest --lf

# Запустити failed тести першими, потім решту
pytest --ff
```

---

### 8. Комбінування опцій

Опції можна комбінувати:

```bash
# Детально + зупинка на першому падінні
pytest -v -x

# Фільтр + verbose + show prints
pytest -k "login" -v -s

# Короткий traceback + максимум 3 падіння
pytest --tb=short --maxfail=3
```

---

### 9. Маркери (`-m`) — коротко

Pytest дозволяє позначати тести маркерами і запускати за ними:

```python
import pytest

@pytest.mark.slow
def test_heavy_computation():
    pass
```

```bash
# Тільки тести з маркером slow
pytest -m slow

# Все крім slow
pytest -m "not slow"
```

Детальніше про маркери — в наступних блоках курсу.

---

## 📋 Швидка шпаргалка

| Ситуація | Команда |
|----------|---------|
| Запустити все | `pytest` |
| Запустити один файл | `pytest tests/test_auth.py` |
| Запустити один тест | `pytest tests/test_auth.py::test_login` |
| Побачити print() | `pytest -s` |
| Більше деталей | `pytest -v` |
| Менше деталей | `pytest -q` |
| Короткий traceback | `pytest --tb=short` |
| Зупинитися на першому падінні | `pytest -x` |
| Побачити що pytest знайшов | `pytest --collect-only` |
| Фільтр за назвою | `pytest -k "login"` |
| Тільки failed тести | `pytest --lf` |
| Найповільніші тести | `pytest --durations=10` |

---

## 📦 Додатково: плагіни (preview)

Наступні команди **потребують окремих плагінів** — вони не входять у стандартний pytest:

| Команда | Плагін | Що робить |
|---------|--------|-----------|
| `pytest --cov=src` | `pytest-cov` | Покриття коду |
| `pytest -n auto` | `pytest-xdist` | Паралельний запуск |
| `pytest --html=report.html` | `pytest-html` | HTML-звіт |
| `pytest --random-order` | `pytest-random-order` | Випадковий порядок |
| `pytest --count=5` | `pytest-repeat` | Повторний запуск |

Встановлення: `python -m pip install pytest-cov pytest-xdist` тощо.

Ці плагіни розглядатимуться в наступних блоках курсу.

---

## ⚠️ Типові помилки

| Помилка | Причина | Рішення |
|---------|---------|---------|
| `0 items collected` | Неправильна назва файлу або функції | `pytest --collect-only` для дебагу |
| print() не видно | pytest приховує stdout | Додайте `-s` |
| Занадто довгий вивід | Повний traceback | Використовуйте `--tb=short` |
| Тести запускаються з іншої папки | Неправильний `testpaths` | Перевірте `pytest.ini` або запустіть з кореня |

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-8-test-output` — аналіз виводу тестів