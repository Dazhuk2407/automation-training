# Exercises - Lesson 4: Test Discovery

## Exercise 1: Correct Naming (EASY)

Визначте які з цих назв pytest знайде:

```python
# A
def test_addition():
    pass

# B  
def addition_test():
    pass

# C
def check_result():
    pass

# D
def test_check_result():
    pass
```

**Відповідь:** pytest знайде A та D (починаються з `test_`)

---

## Exercise 2: Create Test Class (EASY)

Створіть клас `TestCalculator` з 4 тестами:

```python
class TestCalculator:
    """TODO: Додайте тести"""
    
    def test_add(self):
        # TODO
        pass
    
    def test_subtract(self):
        # TODO
        pass
    
    def test_multiply(self):
        # TODO
        pass
    
    def test_divide(self):
        # TODO
        pass
```

Запустіть: `pytest -v test_calculator.py`

---

## Exercise 3: File Naming (MEDIUM)

Створіть файли з правильними назвами:

```bash
# ✅ Створіть ці файли:
touch test_math.py
touch test_strings.py
touch utils_test.py

# ❌ НЕ створюйте:
# math.py - неправильна назва
# testmath.py - без підкреслення
```

Перевірте: `pytest --collect-only`

---

## Exercise 4: Organize Tests (MEDIUM)

Створіть структуру:

```
my_project/
└── tests/
    ├── test_unit/
    │   └── test_models.py
    └── test_integration/
        └── test_api.py
```

Додайте по 2 тести в кожен файл.

Запустіть:
```bash
pytest tests/test_unit/        # тільки unit тести
pytest tests/test_integration/ # тільки integration тести
pytest tests/                  # всі тести
```

---

## Exercise 5: Mix Functions and Classes (HARD)

У файлі `test_mixed.py` створіть:

```python
# 2 окремі тестові функції
def test_function_one():
    pass

def test_function_two():
    pass

# 1 тестовий клас з 3 методами
class TestGroup:
    def test_method_one(self):
        pass
    
    def test_method_two(self):
        pass
    
    def test_method_three(self):
        pass
```

**Скільки тестів знайде pytest?**
- Відповідь: 5 (2 функції + 3 методи)

---

## Exercise 6: Custom Test Collection (HARD)

Створіть `pytest.ini`:

```ini
[pytest]
python_files = test_*.py *_test.py check_*.py
python_classes = Test* Check*
python_functions = test_* check_*
```

Тепер pytest знайде також:
- `check_calculator.py` ✅
- `class CheckResults:` ✅
- `def check_value():` ✅

Протестуйте цю конфігурацію!

---

**Run all exercises:**
```bash
pytest -v --collect-only  # показати які тести знайдено
pytest -v                 # запустити всі тести
```

