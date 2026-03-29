# Block 1: Pytest Basics

Основи тестування з pytest для автоматизації QA.

## 📚 Уроки (9 занять)

### Lesson 0: Знайомство з Pytest
📁 Папка: `lesson-0-pytest-intro`
- Що таке pytest і навіщо він потрібен
- Перший тест, assert, pytest.raises
- **Час: 20-40 хв** (вступний урок)

### Lesson 1: Install Pytest
📁 Папка: `lesson-1-install-pytest`
- Встановлення pytest через pip
- Перевірка версії pytest
- Налаштування середовища

### Lesson 2: Project Structure
📁 Папка: `lesson-2-project-structure`
- Створення tests/ директорії
- Налаштування requirements.txt
- Структура pytest проєкту

### Lesson 3: First Test File
📁 Папка: `lesson-3-first-test`
- Створення tests/test_basic.py
- Структура тестового файлу
- Перший простий тест

### Lesson 4: Test Discovery Rules
📁 Папка: `lesson-4-test-discovery`
- Правила пошуку тестів (test_*.py, *_test.py)
- Класи Test*
- Функції test_*

### Lesson 5: Simple Tests
📁 Папка: `lesson-5-simple-tests`
- Тести для чисел
- Тести для рядків
- Тести для списків

### Lesson 6: Assertions
📁 Папка: `lesson-6-assertions`
- Базові assertions (assert)
- Assert з повідомленнями
- Складні перевірки

### Lesson 7: Run Tests from CLI
📁 Папка: `lesson-7-run-tests`
- Запуск pytest
- Опції: -q, -s, -v
- Контроль виконання (--maxfail)

### Lesson 8: Test Output
📁 Папка: `lesson-8-test-output`
- Читання виводу тестів
- Розуміння pass/fail
- Аналіз traceback

## 🚀 Як почати

1. Почніть з `lesson-0-pytest-intro` (вступний урок)
2. Прочитайте README в папці уроку
3. Вивчіть файли в `examples/`
4. Виконайте вправи в `exercises/`
5. Відповідайте на питання в `QUESTIONS.md`
6. Запустіть тести: `pytest exercises/test_exercises.py -v`

## ⏰ Рекомендований час

- Всього: ~22-28 годин
- Рекомендовано: Тижні 1-2

### Детальний розподіл:

| Урок | Назва                | Час       |
|------|----------------------|-----------|
| 0    | Знайомство з Pytest  | 20-40 хв  |
| 1    | Install Pytest       | 1-2 год   |
| 2    | Project Structure    | 2-3 год   |
| 3    | First Test           | 2-3 год   |
| 4    | Test Discovery       | 2-3 год   |
| 5    | Simple Tests         | 3-4 год   |
| 6    | Assertions           | 3-4 год   |
| 7    | Run Tests CLI        | 2-3 год   |
| 8    | Test Output          | 2-3 год   |

## 📊 Прогрес

```
[ ] Lesson 0: Знайомство з Pytest — lesson-0-pytest-intro
[ ] Lesson 1: Install Pytest — lesson-1-install-pytest
[ ] Lesson 2: Project Structure — lesson-2-project-structure
[ ] Lesson 3: First Test — lesson-3-first-test
[ ] Lesson 4: Test Discovery — lesson-4-test-discovery
[ ] Lesson 5: Simple Tests — lesson-5-simple-tests
[ ] Lesson 6: Assertions — lesson-6-assertions
[ ] Lesson 7: Run Tests CLI — lesson-7-run-tests
[ ] Lesson 8: Test Output — lesson-8-test-output
```

## 📖 Що ви вивчите

Після завершення Block 1 ви вмітимете:
- ✅ Встановлювати та налаштовувати pytest
- ✅ Створювати структуру тестового проєкту
- ✅ Писати прості тести
- ✅ Використовувати assertions
- ✅ Запускати тести з командного рядка
- ✅ Аналізувати результати тестів

## 🎯 Передумови

- Python 3.8+ встановлений
- Базові знання Python (змінні, функції, списки)
- Знайомство з командним рядком

## 📦 Необхідні пакети

```bash
pip install pytest
```