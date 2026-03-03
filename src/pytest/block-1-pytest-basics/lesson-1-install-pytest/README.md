# Lesson 1: Install Pytest

## 🎯 Learning Outcomes

- ✅ Встановити pytest через pip
- ✅ Перевірити версію pytest
- ✅ Налаштувати віртуальне середовище для pytest
- ✅ Зрозуміти базову структуру pytest проєкту

---

## 📖 Теорія

### 1. Що таке Pytest?

**Pytest** - це фреймворк для тестування Python коду. Це один з найпопулярніших інструментів для написання та запуску тестів.

**Переваги pytest:**
- ✅ Простий синтаксис
- ✅ Потужні assertions
- ✅ Автоматичне виявлення тестів
- ✅ Багато плагінів
- ✅ Детальний вивід помилок

---

### 2. Встановлення Pytest

#### Крок 1: Переконайтеся що Python встановлений

```bash
python --version
# або
python3 --version
```

Потрібна версія Python 3.8+

#### Крок 2: Створіть віртуальне середовище (рекомендовано)

```bash
# Створити venv
python -m venv venv

# Активувати
# На macOS/Linux:
source venv/bin/activate

# На Windows:
venv\Scripts\activate
```

#### Крок 3: Встановіть pytest

```bash
pip install pytest
```

#### Крок 4: Перевірте встановлення

```bash
pytest --version
```

**Очікуваний результат:**
```
pytest 7.4.3
```

---

### 3. Альтернативні способи встановлення

#### Встановити конкретну версію:

```bash
pip install pytest==7.4.3
```

#### Встановити з requirements.txt:

```bash
# requirements.txt
pytest==7.4.3
pytest-cov==4.1.0

# Встановити
pip install -r requirements.txt
```

#### Оновити pytest:

```bash
pip install --upgrade pytest
```

---

### 4. Перевірка встановлення

Після встановлення перевірте що pytest працює:

```bash
# Показати версію
pytest --version

# Показати допомогу
pytest --help

# Показати встановлені плагіни
pytest --version --verbose
```

---

### 5. Базова команда pytest

```bash
# Запустити всі тести в поточній директорії
pytest

# Запустити конкретний файл
pytest tests/test_example.py

# Запустити з виводом print statements
pytest -s

# Запустити з детальним виводом
pytest -v
```

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

