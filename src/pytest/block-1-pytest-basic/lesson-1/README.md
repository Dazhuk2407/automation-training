# Lesson 1: Основи Pytest

## Що таке Pytest?

Pytest - це фреймворк для написання та запуску тестів в Python. Він простіший за unittest та більш потужний.

## Встановлення

```bash
pip install pytest
```

## Основні поняття

### Тестова функція
Функція, яка починається з `test_` і містить асерти (assert).

```python
def test_addition():
    assert 2 + 2 == 4
```

### Асерти (Assertions)
```python
assert value == expected_value
assert value != unexpected_value
assert value > 0
assert value is None
assert isinstance(value, int)
```

### Запуск тестів
```bash
# Запустити всі тести
pytest

# Запустити конкретний файл
pytest test_example.py

# Запустити конкретний тест
pytest test_example.py::test_addition

# Запустити з verbose режимом
pytest -v

# Запустити з поточним виводом
pytest -s
```

## Структура тестового файлу

```python
import pytest

class TestCalculator:
    def test_addition(self):
        assert 2 + 2 == 4
    
    def test_subtraction(self):
        assert 5 - 3 == 2

def test_simple():
    assert True
```

## Приклади

Див. папку `examples/`

## Вправи

Виконайте завдання в папці `exercises/`

