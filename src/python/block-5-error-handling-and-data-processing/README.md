# Block 5: Error Handling and Data Processing

Помилки — це нормальна частина роботи коду. Цей блок навчить перехоплювати винятки, читати tracebacks, створювати власні помилки та обробляти дані у форматах, з якими QA стикається щодня: текст, регулярні вирази, JSON.

## 📚 Уроки (Week 4–5)

### Lesson 35: try / except / finally
📁 Папка: `lesson-35-try-except-finally`
- Перехоплення винятків, кілька except
- else та finally, гарантоване прибирання

### Lesson 36: Common Python Errors
📁 Папка: `lesson-36-common-errors`
- ValueError, KeyError, IndexError, TypeError
- Коли і чому виникають

### Lesson 37: Reading Tracebacks
📁 Папка: `lesson-37-reading-tracebacks`
- Як читати повідомлення про помилки
- Аналіз стеку викликів

### Lesson 38: Custom Exceptions
📁 Папка: `lesson-38-custom-exceptions`
- Власні класи винятків
- Ієрархія та повідомлення

### Lesson 39: String Formatting with f-strings
📁 Папка: `lesson-39-f-strings`
- f-strings, вирази всередині
- Форматні специфікатори (числа, вирівнювання)

### Lesson 40: Introduction to Regular Expressions
📁 Папка: `lesson-40-regular-expressions`
- Модуль `re`: search, match, findall
- Групи та поширені патерни

### Lesson 41: Working with JSON Data
📁 Папка: `lesson-41-json-data`
- `json.loads` / `json.dumps`
- Парсинг API-відповідей у тестах

## 🚀 Як почати

1. Почніть з `lesson-35-try-except-finally`
2. Прочитайте README в папці уроку
3. Вивчіть файли в `examples/`
4. Виконайте вправи в `exercises/`
5. Відповідайте на питання в `QUESTIONS.md`
6. Запустіть тести: `pytest exercises/test_exercises.py -v`
