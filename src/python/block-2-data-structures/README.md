# Block 2: Python Data Structures

Структури даних Python для роботи з тестовими даними, API-відповідями та конфігураціями.

## 📚 Уроки (9 занять)

### Lesson 9: Lists
📁 Папка: `lesson-9-lists`
- Створення, доступ, slicing
- Методи: append, extend, pop, remove
- Використання списків у тестах

### Lesson 10: Tuples
📁 Папка: `lesson-10-tuples`
- Immutable колекції
- Unpacking
- Коли tuple замість list

### Lesson 11: Dictionaries
📁 Папка: `lesson-11-dictionaries`
- Створення, доступ, модифікація
- keys(), values(), items()
- Словники як тестові дані

### Lesson 12: Safe Dictionary Access
📁 Папка: `lesson-12-safe-dict-access`
- .get() та default values
- Обробка відсутніх ключів
- Типові баги з KeyError у тестах

### Lesson 13: Sets
📁 Папка: `lesson-13-sets`
- Унікальні значення
- Операції: union, intersection, difference
- Перевірки у тестах

### Lesson 14: Mutable vs Immutable
📁 Папка: `lesson-14-mutable-vs-immutable`
- list vs tuple vs dict vs set
- Side effects при передачі в функції
- Проблеми мутабельності в тестах

### Lesson 15: Copying Data
📁 Папка: `lesson-15-copying-data`
- Shallow copy vs deep copy
- copy(), deepcopy()
- Типові баги з копіюванням

### Lesson 16: range() and zip()
📁 Папка: `lesson-16-range-and-zip`
- range() для генерації послідовностей
- zip() для об'єднання колекцій
- Практичні приклади в тестах

### Lesson 17: Working with Test Data Structures
📁 Папка: `lesson-17-test-data-structures`
- Вкладені структури (dict + list)
- Реальні API responses
- Перевірки складних даних у тестах

## 🚀 Як почати

1. Почніть з `lesson-9-lists`
2. Прочитайте README в папці уроку
3. Вивчіть файли в `examples/`
4. Виконайте вправи в `exercises/`
5. Відповідайте на питання в `QUESTIONS.md`
6. Запустіть тести: `pytest exercises/test_exercises.py -v`

## ⏰ Рекомендований час

- Всього: ~35-45 годин
- На урок: 3-5 годин в середньому
- Рекомендовано: Тижні 3-6

### Детальний розподіл:

| Урок | Назва                    | Час      |
|------|--------------------------|----------|
| 9    | Lists                    | 4-5 год  |
| 10   | Tuples                   | 3-4 год  |
| 11   | Dictionaries             | 4-5 год  |
| 12   | Safe Dict Access         | 3-4 год  |
| 13   | Sets                     | 3-4 год  |
| 14   | Mutable vs Immutable     | 4-5 год  |
| 15   | Copying Data             | 3-4 год  |
| 16   | range() and zip()        | 3-4 год  |
| 17   | Test Data Structures     | 5-6 год  |

## 📊 Прогрес

```
[ ] Lesson 9: Lists — lesson-9-lists
[ ] Lesson 10: Tuples — lesson-10-tuples
[ ] Lesson 11: Dictionaries — lesson-11-dictionaries
[ ] Lesson 12: Safe Dict Access — lesson-12-safe-dict-access
[ ] Lesson 13: Sets — lesson-13-sets
[ ] Lesson 14: Mutable vs Immutable — lesson-14-mutable-vs-immutable
[ ] Lesson 15: Copying Data — lesson-15-copying-data
[ ] Lesson 16: range() and zip() — lesson-16-range-and-zip
[ ] Lesson 17: Test Data Structures — lesson-17-test-data-structures
```

## 🎯 Передумови

- Block 1: Python Basics (змінні, типи, функції, typing)
- Базове знайомство з pytest (вміти запускати тести)

## 📦 Необхідні пакети

```bash
python -m pip install pytest
```