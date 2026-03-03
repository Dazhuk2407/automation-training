# Lesson 2: Project Structure

## 🎯 Learning Outcomes

- ✅ Створити структуру pytest проєкту
- ✅ Організувати директорію tests/
- ✅ Налаштувати requirements.txt
- ✅ Зрозуміти pytest.ini та conftest.py

---

## 📖 Теорія

### 1. Рекомендована Структура Проєкту

```
my_project/
├── src/                    # Код програми
│   ├── __init__.py
│   └── calculator.py
├── tests/                  # Тести
│   ├── __init__.py
│   ├── conftest.py        # Конфігурація pytest
│   └── test_calculator.py
├── requirements.txt        # Залежності
├── pytest.ini             # Налаштування pytest
└── README.md
```

---

### 2. Створення Структури

```bash
# Створити директорії
mkdir -p my_project/src
mkdir -p my_project/tests

# Створити __init__.py
touch my_project/src/__init__.py
touch my_project/tests/__init__.py

# Створити requirements.txt
echo "pytest>=7.4.0" > my_project/requirements.txt
```

---

### 3. requirements.txt

```txt
# Testing framework
pytest==7.4.3

# Coverage
pytest-cov==4.1.0

# Parallel execution
pytest-xdist==3.3.1
```

---

### 4. pytest.ini

```ini
[pytest]
# Test paths
testpaths = tests

# Python files and directories
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*

# Output options
addopts = -v --tb=short
```

---

### 5. conftest.py

```python
"""
Конфігурація pytest та фікстури.
Цей файл автоматично завантажується pytest.
"""

import pytest

@pytest.fixture
def sample_data():
    """Фікстура з тестовими даними."""
    return {"name": "Test", "value": 42}
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

