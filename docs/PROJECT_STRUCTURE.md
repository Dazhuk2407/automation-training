# Project Structure - Структура Проєкту

Детальний опис організації проєкту та як він працює.

## 📊 Загальна Структура

```
automation-training/
├── src/                    # Всі курси розташовані тут
│   ├── python/            # Категорія: Python
│   ├── pytest/            # Категорія: Pytest
│   ├── playwright/        # Категорія: Playwright
│   ├── git/               # Категорія: Git
│   └── linux/             # Категорія: Linux
│
├── docs/                  # Документація проєкту
│   ├── README.md          # Головна сторінка docs
│   ├── GETTING_STARTED.md # Швидкий старт
│   └── PROJECT_STRUCTURE.md # (цей файл)
│
├── README.md              # Головна сторінка проєкту
├── CONTRIBUTING.md        # Правила внеску
├── requirements.txt       # Python залежності
├── conftest.py           # Конфігурація Pytest
├── pytest.ini            # Налаштування Pytest
└── .gitignore            # Git ignore rules
```

## 🎓 Категорії (src/)

### 📗 Python (src/python/)

Основи мови Python для розуміння фундаментальних концепцій.

```
src/python/
└── block-1-python-basic/        ✅ Готовий блок (12 уроків)
    ├── README.md                # Опис блоку та всіх уроків
    ├── lesson-1-install-python/         # ✅ Встановлення Python
    │   ├── README.md
    │   ├── QUESTIONS.md
    │   ├── examples/
    │   │   ├── README.md
    │   │   └── hello_world.py
    │   └── exercises/
    │       └── README.md
    ├── lesson-2-setup-ide/              # ✅ Налаштування IDE
    ├── lesson-3-running-code/           # ✅ Запуск Python коду
    ├── lesson-4-virtual-environment/    # ✅ Віртуальне оточення
    ├── lesson-5-pip-packages/           # ✅ Робота з pip
    ├── lesson-6-requirements/           # ✅ requirements.txt
    ├── lesson-7-basic-syntax/           # ✅ Базовий синтаксис
    ├── lesson-8-pep8-style/             # ✅ PEP 8 та форматування
    ├── lesson-9-debugging/              # ✅ Відлагодження коду
    ├── lesson-10-data-types/            # ✅ Типи даних
    ├── lesson-11-builtin-functions/     # ✅ Вбудовані функції
    └── lesson-12-python-typing/         # ✅ Python Typing
```

**Структура блоку:** 12 уроків покривають:
- Lesson 1: Встановлення Python та перевірка
- Lesson 2: Налаштування IDE (PyCharm/VS Code)
- Lesson 3: Запуск Python коду з терміналу та IDE
- Lesson 4: Створення та використання віртуального оточення
- Lesson 5: Встановлення пакетів через pip
- Lesson 6: Робота з requirements.txt
- Lesson 7: Базовий синтаксис Python
- Lesson 8: PEP 8 стиль та форматування коду
- Lesson 9: Основи відлагодження (debugging)
- Lesson 10: Типи даних та конвертація
- Lesson 11: Вбудовані функції Python
- Lesson 12: Typing та анотація типів

---

### 🧪 Pytest (src/pytest/)

Фреймворк для написання та запуску тестів на Python.

```
src/pytest/
└── block-1-pytest-basics/       ✅ Готовий блок (8 уроків)
    ├── README.md                # Опис блоку
    ├── lesson-1-install-pytest/         # ✅ Встановлення Pytest
    │   ├── README.md
    │   ├── QUESTIONS.md
    │   ├── examples/
    │   └── exercises/
    ├── lesson-2-project-structure/      # ✅ Структура проєкту
    ├── lesson-3-first-test/             # ✅ Перший тест
    ├── lesson-4-test-discovery/         # ✅ Test Discovery
    ├── lesson-5-simple-tests/           # ✅ Прості тести
    ├── lesson-6-assertions/             # ✅ Assertions
    ├── lesson-7-run-tests/              # ✅ Запуск тестів
    └── lesson-8-test-output/            # ✅ Аналіз результатів
```

**Структура блоку:** 8 уроків покривають:
- Lesson 1: Встановлення Pytest
- Lesson 2: Структура тестового проєкту
- Lesson 3: Створення першого тесту
- Lesson 4: Правила Test Discovery
- Lesson 5: Написання простих тестів
- Lesson 6: Основи assertions
- Lesson 7: Запуск тестів з CLI
- Lesson 8: Читання та розуміння test output

---

### 🎭 Playwright (src/playwright/)

Бібліотека для автоматизації взаємодії з веб-браузерами.

```
src/playwright/
└── block-1-playwright-basic/   ⚠️  В розробці
    ├── README.md
    └── lesson-1/               # ⚠️  Базова структура
        ├── README.md
        ├── QUESTIONS.md
        ├── examples/
        └── exercises/
```

**Заплановано:** 8 уроків покриватимуть:
- Lesson 1: Встановлення Playwright
- Lesson 2: Перший тест
- Lesson 3: Селектори
- Lesson 4: Взаємодія з елементами
- Lesson 5: Синхронізація та очікування
- Lesson 6: Скріншоти та запис
- Lesson 7: API тестування
- Lesson 8: Page Object Model

---

### 📦 Git (src/git/)

Система управління версіями Git.

```
src/git/
└── block-1-git-basic/          ⚠️  В розробці
    ├── README.md
    └── lesson-1/               # ⚠️  Базова структура
        ├── README.md
        ├── QUESTIONS.md
        └── exercises/
            └── EXERCISES.md
```

**Заплановано:** 10 уроків покриватимуть:
- Lesson 1: Встановлення Git
- Lesson 2: Конфігурація Git user
- Lesson 3: Ініціалізація репозиторію
- Lesson 4: Структура репозиторію
- Lesson 5: Working directory vs staging vs repository
- Lesson 6: git status
- Lesson 7: git add
- Lesson 8: git commit
- Lesson 9: git log
- Lesson 10: git diff

---

### 🐧 Linux (src/linux/)

Основи роботи з командним рядком Linux/Unix.

```
src/linux/
└── block-1-linux-basic/        ⚠️  В розробці
    ├── README.md
    └── lesson-1/               # ⚠️  Базова структура
        ├── README.md
        ├── QUESTIONS.md
        ├── examples/
        │   └── commands.sh
        └── exercises/
            └── EXERCISES.md
```

**Заплановано:** Уроки покриватимуть основні команди Linux та навігацію файловою системою.

---

## 📖 Структура Кожного Уроку (lesson-X/)

Кожен урок слідує одній і тій же структурі для консистентності:

```
lesson-X-topic-name/
├── README.md           # 📖 Теорія та матеріали
├── QUESTIONS.md        # ❓ Питання для самоперевірки
├── examples/           # 💡 Приклади коду
│   ├── README.md       # Пояснення та інструкції
│   ├── example-1.py
│   ├── example-2.py
│   └── ...
└── exercises/          # 🏋️ Вправи та тести
    ├── README.md       # Інструкції до вправ
    ├── EXERCISES.md    # Опис завдань
    ├── exercise-1.py
    ├── exercise-2.py
    ├── test_exercises.py
    └── ...
```

### 📖 README.md

Містить:
- **Теорія** - Основні концепції та пояснення
- **Приклади кода** - Код в README показує синтаксис
- **Корисні посилання** - На документацію та ресурси
- **Вказівки** - Як перейти до наступного розділу

### ❓ QUESTIONS.md

Містить:
- **10-20 питань** - Для самоперевірки розуміння
- **Практичні завдання** - Написати код, розв'язати проблему
- **Контрольні питання** - Глибше розуміння теми
- **Рекомендації** - Як краще вивчати матеріал

### 💡 examples/

Містить готові коди, які можна запустити:
- **README.md** - Інструкції як запускати приклади
- **Синтаксис** - Показує як писати код
- **Best practices** - Правильні способи роботи
- **Результати** - Що очікувати при запуску
- **Коментарі** - Пояснення до коду

**Як використовувати:**
```bash
# Python приклади
python3 examples/example-1.py

# Pytest приклади
pytest examples/test_math.py -v
```

### 🏋️ exercises/

Містить вправи для практики:
- **README.md** - Інструкції до виконання вправ
- **EXERCISES.md** - Детальний опис завдань
- **Неповні функції** - Потрібно заповнити код (pass)
- **Тестові файли** - Автоматичні тести для перевірки
- **Різні рівні** - Від простих до складних завдань
- **Помилки** - Кожна помилка має бути розпізнана

**Як використовувати:**
```bash
# Прочитати вправу
cat exercises/EXERCISES.md

# Написати рішення (відкрити в редакторі)
code exercises/exercise-1.py

# Запустити тести
pytest exercises/test_exercises.py -v
```
