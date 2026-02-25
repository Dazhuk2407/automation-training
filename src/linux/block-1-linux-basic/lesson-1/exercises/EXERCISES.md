# Lesson 1: Linux Basics - Практичні завдання

## Завдання 1: Навігація

**Завдання:**
1. Показати поточну папку:
```bash
pwd
```

2. Перейти в домашню папку:
```bash
cd ~
```

3. Перелістити файли з деталями:
```bash
ls -l
```

4. Перейти на рівень вище:
```bash
cd ..
```

## Завдання 2: Створення Структури Папок

**Завдання:**
1. Створити основну папку:
```bash
mkdir automation-training
```

2. Перейти в папку:
```bash
cd automation-training
```

3. Створити підпапки:
```bash
mkdir python pytest playwright git linux
```

4. Всередину `python` створити вкладену структуру:
```bash
mkdir -p python/lesson-1/examples
mkdir -p python/lesson-1/exercises
```

5. Перевірити структуру:
```bash
ls -la
```

## Завдання 3: Робота з Файлами

**Завдання:**
1. Створити файл:
```bash
touch notes.txt
```

2. Додати текст:
```bash
echo "Linux Basics - Lesson 1" > notes.txt
```

3. Переглянути вміст:
```bash
cat notes.txt
```

4. Додати ще один рядок:
```bash
echo "Learning Linux commands" >> notes.txt
```

5. Скопіювати файл:
```bash
cp notes.txt notes_backup.txt
```

6. Перевірити що обидва існують:
```bash
ls -l *.txt
```

## Завдання 4: Очищення

**Завдання:**
1. Видалити один файл:
```bash
rm notes_backup.txt
```

2. Перевірити:
```bash
ls -l notes*
```

3. Видалити папку (якщо потрібно):
```bash
rm -r automation-training
```

## Завдання 5: Пошук Файлів

**Завдання:**
1. Створити кілька файлів:
```bash
touch file1.txt file2.txt script.py
```

2. Пошук .txt файлів:
```bash
find . -name "*.txt"
```

3. Пошук всіх файлів:
```bash
find . -type f
```

## Завдання 6: Комбінування Команд

**Завдання:**
1. Перейти, створити, переглянути:
```bash
mkdir test-folder
cd test-folder
touch README.md
echo "# Test Project" > README.md
cat README.md
cd ..
```

2. Видалити папку:
```bash
rm -r test-folder
```

## Завдання 7: Спеціальні Символи

**Завдання:**
1. Розумійте символи:
```bash
~          # Домашня папка
.          # Поточна папка
..         # Папка на рівень вище
*          # Будь-які символи
?          # Один символ
```

2. Приклад з wildcard:
```bash
ls *.txt   # Всі .txt файли
ls file?   # file1, file2, file3 тощо
```

---

**Успіхів! Перейдіть до Lesson 2** 🚀

