# Getting Started - Швидкий Старт

Це посібник для першого запуску проекту та вибору курсу для навчання.

## ⚙️ Встановлення та Налаштування

### 1. Клонуйте репозиторій

```bash
git clone https://github.com/your-username/automation-training.git
cd automation-training
```

### 2. Встановіть Python (3.8+)

```bash
python --version  # Перевірте версію
```

### 3. Встановіть залежності

```bash
pip install -r requirements.txt
```

### 4. Перевірте встановлення

```bash
pytest --version
playwright --version
```

## 🎯 Виберіть Категорію для Навчання

### 📗 Python Basics
**Для початківців, які хочуть вивчити Python**

```bash
cd src/python/block-1-python-basic/lesson-1/
cat README.md
```

**Що вивчіте:**
- Змінні та типи даних
- Оператори та умовні конструкції
- Цикли та функції
- ООП, структури даних
- Обробка помилок

**Час:** ~20 годин | **Рівень:** Початківець

---

### 🧪 Pytest Framework
**Для тих, хто хочу навчитися писати тести**

```bash
cd src/pytest/block-1-pytest-basic/lesson-1/
cat README.md
```

**Що вивчіте:**
- Написання простих тестів
- Фікстури та параметризація
- Мокування та патчінг
- Плагіни для Pytest
- Структурування тестів

**Час:** ~20 годин | **Рівень:** Середній

**Передумова:** Знання Python Basics

---

### 🎭 Playwright Automation
**Для тих, хто хочу автоматизувати браузер**

```bash
cd src/playwright/block-1-playwright-basic/lesson-1/
cat README.md
```

**Що вивчіте:**
- Запуск браузера та навігація
- Пошук елементів та взаємодія
- Синхронізація та очікування
- Page Object Model
- End-to-end тестування

**Час:** ~20 годин | **Рівень:** Середній/Продвинутий

**Передумова:** Знання Python та Pytest

---

### 📦 Git Version Control
**Для всіх, хто хочу оволодіти Git**

```bash
cd src/git/block-1-git-basic/lesson-1/
cat README.md
```

**Що вивчіте:**
- Основи Git та репозиторій
- Гілки та merging
- Remote repositories
- Collaborative workflow
- Git best practices

**Час:** ~16 годин | **Рівень:** Початківець

---

## 📚 Рекомендований Порядок Навчання

### Варіант 1: Повний курс (8 тижнів)
```
Тиждень 1-2:   Python Basics
Тиждень 3-4:   Pytest Framework
Тиждень 5-6:   Playwright Automation
Тиждень 7-8:   Git Version Control
```

### Варіант 2: Тільки Автоматизація (6 тижнів)
```
Тиждень 1-2:   Python Basics
Тиждень 3-4:   Pytest Framework
Тиждень 5-6:   Playwright Automation
```

### Варіант 3: Тільки контроль версій (1 тиждень)
```
Тиждень 1:     Git Version Control
```

## 🚀 Первий Урок - Step by Step

### Крок 1: Перейдіть в папку уроку

```bash
cd src/python/block-1-python-basic/lesson-1/
```

### Крок 2: Прочитайте теорію

```bash
cat README.md
# або відкрийте в редакторі
code README.md
```

### Крок 3: Запустіть приклади

```bash
# Python
python examples/variables.py

# Pytest
pytest examples/test_math.py -v

# Playwright
python examples/basic_example.py
```

### Крок 4: Виконайте вправи

```bash
# Прочитайте вправи
cat exercises/exercise-1.py

# Напишіть вирішення
# (відкрийте файл у редакторі)

# Запустіть тести
pytest exercises/test_exercise.py -v
```

### Крок 5: Проверьте себе

```bash
# Прочитайте питання
cat QUESTIONS.md

# Дайте письмові відповіді на питання
# Поясніть концепції своїми словами
```

## 💡 Поради для Успішного Навчання

1. **Не поспішайте** - виділяйте 2-3 години на один урок
2. **Практикуйте код** - перипишіть приклади самостійно
3. **Робіть перерви** - кожні 50 хвилин робіть 10-хвилинну перерву
4. **Відповідайте на питання** - перевіряйте своє розуміння
5. **Експериментуйте** - модифікуйте код та бачите результати
6. **Не пропускайте** - кожна тема будує на попередній

## 🔧 Корисні Команди

```bash
# Переглянути список файлів в уроці
ls -la

# Запустити Python файл
python filename.py

# Запустити Pytest з verbose режимом
pytest exercises/ -v

# Запустити з виводом
pytest exercises/ -v -s

# Перевірити поточну папку
pwd

# Повернутися на рівень вище
cd ..
```

## 📁 Структура Уроку

```
lesson-1/
├── README.md           # 👈 Почніть отут - теорія
├── QUESTIONS.md        # Питання для самоперевірки
├── examples/           # Приклади коду
│   ├── variables.py
│   └── ...
└── exercises/          # Ваші вправи
    ├── exercise-1.py
    ├── test_exercise.py
    └── ...
```

## ✅ Контрольний Список

- [ ] Python встановлено (v3.8+)
- [ ] Залежності встановлені (`pip install -r requirements.txt`)
- [ ] Вибрали категорію для навчання
- [ ] Прочитали `README.md` в уроці
- [ ] Запустили приклади
- [ ] Виконали вправи
- [ ] Відповіли на питання

## 🆘 Якщо щось не працює

1. **Перевірте версію Python:** `python --version`
2. **Перевірте встановлення залежностей:** `pip list`
3. **Прочитайте повідомлення про помилку** - вона часто каже де проблема
4. **Шукайте на Google** - вам не перший, хто наткнувся на таку помилку
5. **Питайте у спільноті** - GitHub issues або форуми

## 📞 Потрібна допомога?

- 📖 Див. [Project Structure](PROJECT_STRUCTURE.md) для деталей
- 💡 Див. [How to Learn](HOW_TO_LEARN.md) для рекомендацій
- 🤝 Див. [Contributing](CONTRIBUTING.md) для питань та пропозицій

---

**Готові почати? 🚀**

```bash
cd src/python/block-1-python-basic/lesson-1/
cat README.md
```

**Успіхів!** 🎉

