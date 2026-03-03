# Lesson 1: Git Basics - Практичні завдання

## Завдання 1: Налаштування Git

**Завдання:**
1. Встановіть Git (якщо ще не встановлено): `git --version`
2. Налаштуйте своє ім'я та email:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
3. Перевірте налаштування:
```bash
git config --global user.name
git config --global user.email
```

## Завдання 2: Інітіалізація репозиторію

**Завдання:**
1. Створіть нову папку для проєкту:
```bash
mkdir my-first-repo
cd my-first-repo
```

2. Ініціалізуйте Git репозиторій:
```bash
git init
```

3. Перевірте, що `.git` папка створена:
```bash
ls -la
```

## Завдання 3: Перший коміт

**Завдання:**
1. Створіть файл `README.md`:
```bash
echo "# My First Project" > README.md
```

2. Перевірте статус репозиторію:
```bash
git status
```

3. Додайте файл до staging area:
```bash
git add README.md
```

4. Створіть перший коміт:
```bash
git commit -m "Initial commit: Add README.md"
```

5. Перевірте лог комітів:
```bash
git log
```

## Завдання 4: Множественні файли та комміти

**Завдання:**
1. Створіть файл `hello.py`:
```bash
echo "print('Hello World')" > hello.py
```

2. Додайте файл:
```bash
git add hello.py
```

3. Створіть коміт:
```bash
git commit -m "Add Python hello script"
```

## Завдання 5: Модифікація файлу та новий коміт

**Завдання:**
1. Модифікуйте `README.md`:
```bash
echo "## Description" >> README.md
```

2. Перевірте різниці:
```bash
git diff
```

3. Додайте та закомітуйте:
```bash
git add README.md
git commit -m "Update README with description"
```

4. Перегляньте всю історію комітів:
```bash
git log --oneline
```

