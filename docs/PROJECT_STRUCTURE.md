# Project Structure - Структура Проекту

Детальний опис організації проекту та як він працює.

## 📊 Загальна Структура

```
automation-training/
├── src/                    # Всі курси розташовані тут
│   ├── python/            # Категорія: Python
│   ├── pytest/            # Категорія: Pytest
│   ├── playwright/        # Категорія: Playwright
│   └── git/               # Категорія: Git
│
├── docs/                  # Документація проекту
│   ├── README.md          # Головна сторінка docs
│   ├── GETTING_STARTED.md # Швидкий старт
│   ├── PROJECT_STRUCTURE.md # (цей файл)
│   ├── HOW_TO_LEARN.md    # Рекомендації для навчання
│   ├── CONTRIBUTING.md    # Як розширювати проект
│   └── LESSON_TEMPLATE.md # Шаблон для нових уроків
│
├── README.md              # Головна сторінка проекту
├── CONTRIBUTING.md        # Правила внеску
├── requirements.txt       # Python залежності
├── conftest.py           # Конфігурація Pytest
├── pytest.ini            # Налаштування Pytest
├── .gitignore            # Git ignore rules
└── 5-schedule/           # Графік занять (від старої версії)
```

## 🎓 Категорії (src/)

### 📗 Python (src/python/)

Основи мови Python для розуміння фундаментальних концепцій.

```
src/python/
└── block-1-python-basic/        ✅ Готовий блок
    ├── README.md                # Опис блоку та 8 уроків
    ├── lesson-1/                # ✅ Lesson 1: Змінні та типи даних
    │   ├── README.md
    │   ├── QUESTIONS.md
    │   ├── examples/
    │   │   └── variables.py
    │   └── exercises/
    │       ├── exercise-1.py
    │       └── test_exercise.py
    ├── lesson-2/                # ➕ Можна додати
    └── ... lesson-8/            # ➕ Можна додати
```

**Структура урока:** Lesson 1-8 покривають:
- Lesson 1: Змінні та типи даних
- Lesson 2: Оператори та умовні конструкції
- Lesson 3: Цикли
- Lesson 4: Функції
- Lesson 5: ООП
- Lesson 6: Структури даних
- Lesson 7: Обробка помилок
- Lesson 8: Модулі та пакети

---

### 🧪 Pytest (src/pytest/)

Фреймворк для написання та запуску тестів на Python.

```
src/pytest/
└── block-1-pytest-basic/       ✅ Готовий блок
    ├── README.md
    ├── lesson-1/               # ✅ Lesson 1: Основи Pytest
    │   ├── README.md
    │   ├── QUESTIONS.md
    │   ├── examples/
    │   │   └── test_math.py
    │   └── exercises/
    │       └── test_exercises.py
    ├── lesson-2/               # ➕ Можна додати
    └── ... lesson-8/           # ➕ Можна додати
```

**Структура урока:** Lesson 1-8 покривають:
- Lesson 1: Основи Pytest
- Lesson 2: Фікстури
- Lesson 3: Параметризація
- Lesson 4: Маркери
- Lesson 5: Плагіни
- Lesson 6: Моки та патчінг
- Lesson 7: Організація тестів
- Lesson 8: Інтеграційне тестування

---

### 🎭 Playwright (src/playwright/)

Бібліотека для автоматизації взаємодії з веб-браузерами.

```
src/playwright/
└── block-1-playwright-basic/   ✅ Готовий блок
    ├── README.md
    ├── lesson-1/               # ✅ Lesson 1: Основи Playwright
    │   ├── README.md
    │   ├── QUESTIONS.md
    │   ├── examples/
    │   │   └── basic_example.py
    │   └── exercises/
    │       └── test_exercises.py
    ├── lesson-2/               # ➕ Можна додати
    └── ... lesson-8/           # ➕ Можна додати
```

**Структура урока:** Lesson 1-8 покривають:
- Lesson 1: Основи Playwright
- Lesson 2: Селектори
- Lesson 3: Взаємодія з елементами
- Lesson 4: Синхронізація та очікування
- Lesson 5: Фрейми та вікна
- Lesson 6: Скріншоти та запис
- Lesson 7: API та Network
- Lesson 8: Page Object Model

---

### 📦 Git (src/git/)

Система управління версіями Git.

```
src/git/
└── block-1-git-basic/          ✅ Готовий блок
    ├── README.md
    ├── lesson-1/               # ✅ Lesson 1: Основи Git
    │   ├── README.md
    │   ├── QUESTIONS.md
    │   └── exercises/
    │       └── EXERCISES.md
    ├── lesson-2/               # ➕ Можна додати
    └── ... lesson-8/           # ➕ Можна додати
```

**Структура урока:** Lesson 1-8 покривають:
- Lesson 1: Основи Git
- Lesson 2: Гілки
- Lesson 3: Merging та конфлікти
- Lesson 4: Remote repositories
- Lesson 5: Collaborative workflow
- Lesson 6: Advanced Git
- Lesson 7: Git workflows
- Lesson 8: Best practices

---

## 📖 Структура Кожного Уроку (lesson-X/)

Кожен урок слідує одній і тій же структурі для консистентності:

```
lesson-X/
├── README.md           # 📖 Теорія та матеріалу
├── QUESTIONS.md        # ❓ Питання для самоперевірки
├── examples/           # 💡 Приклади коду
│   ├── example1.py
│   ├── example2.py
│   └── ...
└── exercises/          # 🏋️ Вправи та тести
    ├── exercise-1.py
    ├── exercise-2.py
    ├── test_exercise.py
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

Содержит готові коди, которые можна запустити:
- **Синтаксис** - Показує як писати код
- **Best practices** - Правильні способи роботи
- **Результати** - Що очікувати при запуску
- **Комментарії** - Пояснення до кода

**Як використовувати:**
```bash
python examples/variables.py
pytest examples/test_math.py -v
```

### 🏋️ exercises/

Містить вправи для практики:
- **Неповні функції** - Потрібно заповнити код (pass)
- **Тестові файли** - Автоматичні тести для перевірки
- **Різні рівні** - От простих до складних завдань
- **Помилки** - Кожна помилка має бути розпізнана

**Як використовувати:**
```bash
# Прочитати вправу
cat exercises/exercise-1.py

# Написати рішення (відкрити в редакторі)
code exercises/exercise-1.py

# Запустити тести
pytest exercises/test_exercise.py -v
```

---

## 🔄 Процес Навчання

```
1. Вибрати категорію
   ↓
2. Вибрати блок
   ↓
3. Вибрати урок (lesson-1, lesson-2, ...)
   ↓
4. Прочитати README.md (теорія)
   ↓
5. Запустити приклади (examples/)
   ↓
6. Виконати вправи (exercises/)
   ↓
7. Запустити тести (pytest)
   ↓
8. Відповісти на питання (QUESTIONS.md)
   ↓
9. Перейти до наступного уроку
```

---

## 📈 Як Проект Розширюється

### Додавання нового уроку (Lesson 2-8)

```bash
# 1. Скопіювати структуру lesson-1
cp -r src/python/block-1-python-basic/lesson-1/ \
      src/python/block-1-python-basic/lesson-2/

# 2. Оновити матеріал в README.md, QUESTIONS.md
# 3. Додати нові приклади в examples/
# 4. Додати нові вправи в exercises/
```

### Додавання нового блоку

```bash
# 1. Створити нову папку блоку
mkdir src/python/block-2-python-advanced/

# 2. Скопіювати структуру з block-1
cp -r src/python/block-1-python-basic/lesson-1/ \
      src/python/block-2-python-advanced/lesson-1/

# 3. Написати новий README.md для блоку
# 4. Оновити матеріал для другого рівня складності
```

### Додавання нової категорії

```bash
# 1. Створити нову папку категорії
mkdir src/new-category/

# 2. Створити нові блоки всередину
mkdir src/new-category/block-1-new-basic/

# 3. Додати lesson-1 з повним матеріалом
```

---

## 🎯 Структура Повинна Бути Зрозумілою

- ✅ **Послідовна** - Один блок → Один урок → Один файл
- ✅ **Модульна** - Легко додавати нові блоки та уроки
- ✅ **Масштабована** - Сотні уроків в сотнях блоків
- ✅ **Логічна** - Легко знайти те, що потрібно
- ✅ **Консистентна** - Всі уроки слідують одному формату

---

## 📋 Контрольний Список при Створенні Нового Уроку

- [ ] Папка `lesson-X/` створена
- [ ] `README.md` написаний з теорією
- [ ] `QUESTIONS.md` написаний з питаннями
- [ ] `examples/` папка з 2-3 прикладами
- [ ] `exercises/` папка з вправами та тестами
- [ ] Тести проходять ✅
- [ ] Виконаний контрольний список з файлу

---

**Структура готова для розширення!** 🚀

