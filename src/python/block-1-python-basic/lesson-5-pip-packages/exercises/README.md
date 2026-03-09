# Вправи - Lesson 5: pip

## Завдання 1: Активуйте venv

```bash
source venv/bin/activate  # macOS/Linux
```

## Завдання 2: Оновіть pip

```bash
python3 -m pip install --upgrade pip
```

## Завдання 3: Встановіть пакети

```bash
pip install requests
pip install pytest
```

## Завдання 4: Перевірте встановлення

```bash
pip list
# Повинні бути requests, pytest, numpy

pip show requests
# Показує деталі пакету
```

## Завдання 5: Використайте пакет

Створіть файл `test_requests.py`:

```python
import requests

response = requests.get('https://api.github.com')
print(f"Status: {response.status_code}")
```

Запустіть:
```bash
python3 test_requests.py
```

## Завдання 6: Видаліть пакет

```bash
pip uninstall requests -y
```
