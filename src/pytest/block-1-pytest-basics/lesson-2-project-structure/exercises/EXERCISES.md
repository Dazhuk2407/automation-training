# Вправи — Lesson 2: Структура pytest проєкту

---

## 🏋️ Вправа 1: Створити структуру проєкту (EASY)

**Завдання:** Створіть стандартну структуру pytest проєкту.

Створіть папку `my_project/` з такою структурою:

```
my_project/
├── src/
│   └── __init__.py
├── tests/
│   └── __init__.py
└── requirements.txt
```

Через термінал:
```bash
mkdir -p my_project/src my_project/tests
touch my_project/src/__init__.py
touch my_project/tests/__init__.py
touch my_project/requirements.txt
```

Або створіть вручну в IDE.

---

## 🏋️ Вправа 2: Створити pytest.ini (EASY)

**Завдання:** Додайте конфігурацію pytest у ваш проєкт.

Створіть файл `my_project/pytest.ini`:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --tb=short
```

---

## 🏋️ Вправа 3: Створити conftest.py (EASY)

**Завдання:** Додайте conftest.py у папку `tests/`.

Створіть файл `my_project/tests/conftest.py`:

```python
"""
conftest.py — конфігурація pytest.

Цей файл автоматично підхоплюється pytest.
Тут буде спільна конфігурація та фікстури (розглянемо пізніше).
"""
```

---

## 🏋️ Вправа 4: Перевірити структуру (MEDIUM)

**Завдання:** Переконайтесь що ваша структура правильна.

Фінальна структура має виглядати так:

```
my_project/
├── src/
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   └── conftest.py
├── requirements.txt
└── pytest.ini
```

Запустіть автоматичну перевірку:

```bash
pytest test_exercises.py -v
```

---

## ✅ Перевірка

### Критерії:

- [ ] `my_project/src/` існує з `__init__.py`
- [ ] `my_project/tests/` існує з `__init__.py`
- [ ] `my_project/pytest.ini` існує з секцією `[pytest]`
- [ ] `my_project/tests/conftest.py` існує
- [ ] `my_project/requirements.txt` існує
- [ ] `test_exercises.py` проходить повністю