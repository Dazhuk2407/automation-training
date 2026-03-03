# Вправи - Lesson 1: Install Python

## Завдання 1: Перевірити встановлення

```bash
# Запустіть ці команди в терміналі:
python3 --version
pip3 --version
which python3
```

Результат має бути версія 3.12+

## Завдання 2: Дізнатися де встановлено Python

```bash
python3 -c "import sys; print(sys.executable)"
```

## Завдання 3: Запустити простий скрипт

```bash
python3 -c "print('Python works!')"
```

## Завдання 4: Перевірити доступні модулі

```bash
python3 -c "import sys; print('\n'.join(sys.path[:3]))"
```

---

