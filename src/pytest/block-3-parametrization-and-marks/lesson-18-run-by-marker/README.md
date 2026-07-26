# Lesson 18: Run Tests by Marker (pytest -m)

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Запускати тести за маркером: `pytest -m smoke`
- ✅ Використовувати логічні вирази: `-m "smoke and not slow"`, `-m "smoke or regression"`
- ✅ Розуміти як `-m` фільтрує набір тестів (selected / deselected)
- ✅ Комбінувати маркери для точного відбору
- ✅ Будувати CI-набори через `-m` (pre-commit, nightly)

---

## 📋 Передумови

Ви вже знаєте:
- Що таке маркери та як їх ставити через `@pytest.mark.<name>` (Lesson 17)
- Як реєструвати маркери у `pytest.ini` (`markers = ...`) (Lesson 17)

Тепер ми навчимося **запускати** підмножину тестів за цими маркерами через прапорець `-m`.

---

## 📖 Теорія

### 1. `pytest -m smoke` — запустити ЛИШЕ тести з маркером

Прапорець `-m` каже pytest: збери всі тести, але **виконай тільки ті**, що мають цей маркер.

```bash
# Запустити тільки тести з маркером smoke
pytest -m smoke
```

Якщо у файлі є тести з різними маркерами:

```python
import pytest

@pytest.mark.smoke
def test_login():
    ...

@pytest.mark.regression
def test_edge_case():
    ...
```

то `pytest -m smoke` виконає лише `test_login`, а `test_edge_case` буде **deselected** (пропущений на етапі відбору, не запущений).

---

### 2. Логічні вирази

`-m` приймає не тільки одне ім'я, а **булевий вираз** з `and`, `or`, `not`:

```bash
# Тільки smoke, але НЕ slow
pytest -m "smoke and not slow"

# Усе, крім slow
pytest -m "not slow"

# smoke АБО regression
pytest -m "smoke or regression"

# Складний вираз з дужками
pytest -m "(smoke or regression) and not slow"
```

Вирази читаються як звичайна логіка Python: `and` — обидва, `or` — хоча б один, `not` — заперечення.

---

### 3. Що бачимо у виводі: selected / deselected

pytest у підсумковому рядку показує, скільки тестів **відібрано**, а скільки **відкинуто**:

```
$ pytest -m smoke
collected 5 items / 3 deselected / 2 selected

test_login.py::test_login PASSED
test_login.py::test_signup PASSED

===== 2 passed, 3 deselected =====
```

- `collected` — скільки тестів знайдено всього
- `deselected` — скільки відкинуто фільтром `-m`
- `selected` / `passed` — скільки реально запущено

Це головний спосіб перевірити, що ваш вираз відбирає саме те, що потрібно.

---

### 4. `-m` працює із зареєстрованими маркерами

Через `--strict-markers` (увімкнено у нашому `pytest.ini`) невідомий маркер призведе до **помилки**, а не тихого пропуску:

```bash
pytest -m smoek   # друкарська помилка -> ERROR: unknown marker
```

Тому маркери спершу реєструють у `pytest.ini`:

```ini
[pytest]
markers =
    smoke: smoke tests
    regression: regression tests
    slow: slow running tests
```

У цьому уроці `smoke`, `regression`, `slow` вже зареєстровані глобально.

---

### 5. У QA: набори через `-m`

`-m` — це основний інструмент побудови CI-наборів:

| Сценарій | Команда | Ідея |
|----------|---------|------|
| Pre-commit / PR | `pytest -m smoke` | Швидка перевірка ключового функціоналу |
| Швидкий прогін | `pytest -m "not slow"` | Усе, крім довгих тестів |
| Nightly CI | `pytest -m regression` | Повний регрес уночі |
| Реліз-кандидат | `pytest -m "smoke or regression"` | Об'єднаний набір |

Один і той самий код тестів дає різні набори — залежно від виразу `-m`.

---

## ⚠️ Типові помилки

### `-m` з незареєстрованим маркером

```bash
# ❌ Маркер не зареєстрований у pytest.ini -> помилка при --strict-markers
pytest -m smoketest

# ✅ Спершу зареєструйте маркер, потім використовуйте точне ім'я
pytest -m smoke
```

### Плутати `-m` (маркери) і `-k` (імена)

```bash
# ❌ -m очікує МАРКЕР, а не частину імені тесту
pytest -m test_login

# ✅ -m для маркерів
pytest -m smoke
# ✅ -k для фільтра за іменем (тема Lesson 19)
pytest -k login
```

### Складні вирази без дужок

```bash
# ❌ Неоднозначно: що з чим комбінується?
pytest -m "smoke or regression and not slow"

# ✅ Дужки роблять намір явним
pytest -m "(smoke or regression) and not slow"
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-19-filter-by-name`
