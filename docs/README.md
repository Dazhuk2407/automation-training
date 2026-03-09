# Документація Проєкту

Ласкаво просимо до **Automation Training** - комплексного курсу по вивченню автоматизації тестування на Python!

## 📑 Зміст документації

1. **[GETTING_STARTED.md](GETTING_STARTED.md)** - Швидкий старт для новачків
2. **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Опис структури проєкту
3. **[LESSON_TEMPLATE.md](LESSON_TEMPLATE.md)** - Шаблон для створення нових уроків

## 🚀 Швидкий Старт

```bash
# 1. Встановіть залежності
pip install -r requirements.txt

# 2. Виберіть категорію та урок
cd src/python/block-1-python-basic/lesson-1/

# 3. Прочитайте теорію
cat README.md

# 4. Вивчіть приклади
python python examples/example_2_variables.py

# 5. Виконайте вправи
pytest exercises/test_exercises.py -v

# 6. Перевір себе
cat QUESTIONS.md
```

## 📚 Основні Категорії

| Категорія | Папка | Опис |
|-----------|-------|------|
| **Python** | `src/python/` | Основи мови Python |
| **Pytest** | `src/pytest/` | Фреймворк для тестування |
| **Playwright** | `src/playwright/` | Автоматизація браузера |
| **Git** | `src/git/` | Контроль версій |

## 📖 Структура Уроку

Кожен урок (`lesson-1`, `lesson-2` тощо) містить:

```
lesson-X/
├── README.md           # 📖 Теорія та основна інформація
├── QUESTIONS.md        # ❓ Питання для самоперевірки
├── examples/           # 💡 Приклади коду
│   └── *.py           # Готові до запуску приклади
└── exercises/          # 🏋️ Практичні вправи та тести
    ├── exercise-*.py   # Завдання для вирішення
    └── test_*.py       # Тести для перевірки
```

## ✅ Файли в Уроці

### 📖 README.md
- Теоретичний матеріал
- Кодові приклади
- Посилання на інші ресурси

### ❓ QUESTIONS.md
- 10-20 питань для самоперевірки
- Практичні завдання
- Контрольні питання для розуміння

### 💡 examples/
- Готові до запуску приклади
- Демонстрація концепцій
- Best practices

### 🏋️ exercises/
- Вправи для закріплення матеріалу
- Автоматичні тести
- Задачі різних рівнів складності

## 🎯 Як Використовувати Курс

1. **Виберіть категорію** (Python, Pytest, Playwright, Git)
2. **Виберіть блок** (block-1-python-basic, block-2-python-advanced тощо)
3. **Виберіть урок** (lesson-1, lesson-2 тощо)
4. **Дотримуйтесь процесу:**
   - Прочитайте `README.md`
   - Запустіть приклади з `examples/`
   - Виконайте вправи з `exercises/`
   - Відповідайте на питання з `QUESTIONS.md`

## 📊 Структура для Розширення

Проект спеціально структурований для масштабування:

```
src/
├── python/
│   ├── block-1-python-basic/     (✅ Готовий)
│   │   └── lesson-1/
│   ├── block-2-python-advanced/  (➕ Можна додати)
│   │   ├── lesson-1/
│   │   └── lesson-2/
│   └── block-3-python-oop/       (➕ Можна додати)
│
├── pytest/
│   ├── block-1-pytest-basic/     (✅ Готовий)
│   └── block-2-pytest-advanced/  (➕ Можна додати)
│
├── playwright/
│   ├── block-1-playwright-basic/ (✅ Готовий)
│   └── block-2-playwright-pom/   (➕ Можна додати)
│
└── git/
    ├── block-1-git-basic/        (✅ Готовий)
    └── block-2-git-advanced/     (➕ Можна додати)
```

## ❓ Часті Питання
**Q: З чого почати?**
A: Почніть з `src/python/block-1-python-basic/lesson-1/`

**Q: Як запустити приклади?**
A: `python examples/variables.py`
---

**Успіхів в навчанні!** 🚀

