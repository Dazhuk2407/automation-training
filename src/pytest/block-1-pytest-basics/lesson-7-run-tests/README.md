# Lesson 7: Run Tests from CLI

## 🎯 Learning Outcomes

- ✅ Запускати тести з командного рядка
- ✅ Використовувати різні опції pytest
- ✅ Контролювати виконання тестів
- ✅ Фільтрувати та вибирати тести

---

## 📖 Теорія

### 1. Базовий Запуск

```bash
# Запустити всі тести в поточній директорії
pytest

# Запустити з детальним виводом
pytest -v

# Запустити один файл
pytest tests/test_example.py

# Запустити один тест
pytest tests/test_example.py::test_function

# Запустити тесты в класі
pytest tests/test_example.py::TestClass::test_method
```

---

### 2. Опції Виводу

```bash
# -v (verbose) - детальний вивід
pytest -v

# -q (quiet) - мінімальний вивід
pytest -q

# -s (show) - показувати print() виводи
pytest -s

# -vv - більш детальний вивід
pytest -vv

# --tb=short - коротка трасування
pytest --tb=short

# --tb=no - без трасування
pytest --tb=no
```

---

### 3. Фільтрування Тестів

```bash
# Запустити тесты що містять "login" в назві
pytest -k "login"

# Запустити НЕ містять "slow"
pytest -k "not slow"

# Запустити що містять "login" або "auth"
pytest -k "login or auth"

# Запустити тільки останньо failed тесты
pytest --lf

# Запустити failed тесты перше
pytest --ff
```

---

### 4. Контроль Виконання

```bash
# Зупинити на першій помилці
pytest -x

# Зупинити після N помилок
pytest --maxfail=3

# Запустити з паузою на помилці
pytest -s --pdb

# Запустити тесты у випадковому порядку
pytest --random-order

# Запустити N разів
pytest --count=5
```

---

### 5. Марковані Тесты

```bash
import pytest

@pytest.mark.slow
def test_slow_operation():
    pass

@pytest.mark.skip
def test_not_ready():
    pass

@pytest.mark.xfail
def test_expected_to_fail():
    pass
```

```bash
# Запустити тільки slow тесты
pytest -m slow

# Пропустити slow тесты
pytest -m "not slow"
```

---

### 6. Виміри та Звіти

```bash
# Показати 10 найповільніших тестів
pytest --durations=10

# Покриття коду (потрібно: pip install pytest-cov)
pytest --cov=src

# Вивід в HTML
pytest --html=report.html

# Паралельне виконання (потрібно: pip install pytest-xdist)
pytest -n auto
```

---

### 7. Конфігурація з pytest.ini

```ini
[pytest]
# Шляхи до тестів
testpaths = tests

# Параметри командного рядка за замовчуванням
addopts = -v --tb=short

# Маркери
markers =
    slow: позначити тест як повільний
    integration: integration тест
```

---

### 8. Приклади Команд

```bash
# Базовий запуск
pytest

# Детальний вивід
pytest -v

# З print() виводами
pytest -s

# Однотесту
pytest tests/test_module.py::test_function -v

# За ключовим словом
pytest -k "test_login" -v

# На перший fail
pytest -x

# На 3 fails
pytest --maxfail=3

# Останні failed
pytest --lf -v

# З покриттям
pytest --cov=src --cov-report=html

# Паралельно
pytest -n 4
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

