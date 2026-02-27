# Exercises - Lesson 7: Run Tests from CLI

## Exercise 1: Basic Commands (EASY)

Запустіть наступні команди:

```bash
# Базовий запуск
pytest

# Детальний вивід
pytest -v

# Мінімальний вивід
pytest -q

# Зі скріниотами
pytest -s

# Один файл
pytest tests/test_example.py
```

---

## Exercise 2: Filtering Tests (EASY)

```bash
# Тесты що містять "login" в назві
pytest -k "login"

# Тесты що НЕ містять "slow"
pytest -k "not slow"

# Один конкретний тест
pytest tests/test_auth.py::test_login -v
```

---

## Exercise 3: Stop on Failures (MEDIUM)

```bash
# Зупинити на першій помилці
pytest -x

# Зупинити після 3 помилок
pytest --maxfail=3

# Запустити спочатку failed тесты
pytest --ff
```

---

## Exercise 4: Mark Tests (MEDIUM)

Создайте файл `test_marked.py`:

```python
import pytest

@pytest.mark.slow
def test_slow():
    pass

@pytest.mark.fast
def test_fast():
    pass

@pytest.mark.unit
def test_unit():
    pass
```

Запустіть:

```bash
# Тільки slow
pytest -m slow -v

# Без slow
pytest -m "not slow" -v

# Unit та fast
pytest -m "unit or fast" -v
```

---

## Exercise 5: Verbosity Levels (HARD)

```bash
# Різні рівні деталізації:
pytest                   # Normal
pytest -v               # Verbose
pytest -vv              # Very verbose
pytest -q               # Quiet

# З tracebacks:
pytest --tb=short
pytest --tb=long
pytest --tb=no
```

---

## Exercise 6: Create pytest.ini (HARD)

Создайте `pytest.ini`:

```ini
[pytest]
testpaths = tests
addopts = -v --tb=short
markers =
    slow: slow test
    unit: unit test
    integration: integration test
```

Потім запустіть:

```bash
pytest  # Автоматично буде використовувати налаштування з pytest.ini
```

---

**Practice these commands!**

