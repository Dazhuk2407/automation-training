# Lesson 4: Test Discovery Rules

## 🎯 Learning Outcomes

- ✅ Розуміти як pytest знаходить тести
- ✅ Знати правила naming для тестів
- ✅ Організувати тести правильно
- ✅ Використовувати Test classes

---

## 📖 Теорія

### 1. Правила Test Discovery

Pytest автоматично знаходить тести за правилами:

**Файли:**
- `test_*.py` - файли що починаються з `test_`
- `*_test.py` - файли що закінчуються на `_test`

**Функції:**
- `test_*()` - функції що починаються з `test_`

**Класи:**
- `Test*` - класи що починаються з `Test` (без `__init__`)

**Методи:**
- `test_*()` - методи класів що починаються з `test_`

---

### 2. Приклади Naming

✅ **ПРАВИЛЬНО:**
```python
# test_calculator.py ✅
# calculator_test.py ✅

def test_addition():  # ✅
    pass

class TestCalculator:  # ✅
    def test_add(self):  # ✅
        pass
```

❌ **НЕПРАВИЛЬНО:**
```python
# calculator.py ❌ (не починається з test_)
# testcalculator.py ❌ (без підкреслення)

def add_test():  # ❌ (не починається з test_)
    pass

class Calculator_Test:  # ❌ (не починається з Test)
    pass
```

---

### 3. Test Classes

```python
class TestCalculator:
    """Група тестів для Calculator."""
    
    def test_add(self):
        assert 2 + 2 == 4
    
    def test_subtract(self):
        assert 5 - 3 == 2
    
    def test_multiply(self):
        assert 3 * 4 == 12
```

**Переваги класів:**
- Групування пов'язаних тестів
- Спільні setup/teardown методи
- Організація коду

---

### 4. Структура Проекту

```
tests/
├── test_unit/
│   ├── test_calculator.py
│   └── test_parser.py
├── test_integration/
│   └── test_api.py
└── conftest.py
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`
