# Block 7: Files, Environment, and Tools

Автоматизація живе серед файлів, шляхів, змінних оточення й дат. Цей блок дає інструменти, без яких не обходиться жоден тестовий скрипт: читання/запис файлів, CSV/JSON, `pathlib`, `os`/`sys`, дати, випадкові дані, модулі та керування залежностями.

## 📚 Уроки (Week 6–7)

### Lesson 49: Reading and Writing Files
📁 Папка: `lesson-49-reading-writing-files`
- `open()`, контекст `with`
- Режими read / write / append

### Lesson 50: Working with CSV and JSON Files
📁 Папка: `lesson-50-csv-and-json-files`
- Модуль `csv` (reader, DictReader/DictWriter)
- Читання та запис JSON-файлів

### Lesson 51: Managing File Paths with pathlib
📁 Папка: `lesson-51-pathlib`
- `Path`, з'єднання шляхів `/`
- Перевірки, розширення, ітерація

### Lesson 52: Working with OS and System Modules
📁 Папка: `lesson-52-os-and-sys`
- `os` — env vars, шляхи, файли
- `sys` — argv, шляхи, вихід

### Lesson 53: Working with Dates and Time
📁 Папка: `lesson-53-dates-and-time`
- `datetime`, `date`, `timedelta`
- Форматування та парсинг

### Lesson 54: Random Data Generation
📁 Папка: `lesson-54-random-data`
- `random`, `seed`, `choice`, `sample`
- Генерація тестових даних

### Lesson 55: Modules and Packages
📁 Папка: `lesson-55-modules-and-packages`
- Власні модулі та імпорти
- Пакети, `__init__.py`

### Lesson 56: Managing Dependencies with pip
📁 Папка: `lesson-56-pip-and-requirements`
- `pip install / freeze / upgrade`
- `requirements.txt` workflow

## 🚀 Як почати

1. Почніть з `lesson-49-reading-writing-files`
2. Прочитайте README в папці уроку
3. Вивчіть файли в `examples/`
4. Виконайте вправи в `exercises/`
5. Відповідайте на питання в `QUESTIONS.md`
6. Запустіть тести: `pytest exercises/test_exercises.py -v`
