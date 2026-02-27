# Приклади - Lesson 4: venv

## Пошагово: Створення та активація venv

```bash
# 1. Перейдіть в папку проекту
cd ~/my-python-project

# 2. Створіть venv
python3 -m venv venv

# 3. Активуйте на macOS/Linux
source venv/bin/activate

# 4. Перевірте активацію
which python3
# Output: /home/user/my-python-project/venv/bin/python3

# 5. Переконайтеся що інтерпретатор з venv
python3 --version

# 6. Коли готово - деактивуйте
deactivate
```

## На Windows

```bash
# Створення
python -m venv venv

# Активація
venv\Scripts\activate

# Деактивація
deactivate
```

## Знаки активної venv

Коли venv активна, у терміналі ви побачите:
```
(venv) user@computer:~/my-python-project$
```

Префікс `(venv)` показує що середовище активне.
