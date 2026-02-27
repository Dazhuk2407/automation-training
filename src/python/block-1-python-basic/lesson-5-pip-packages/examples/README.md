# Приклади - Lesson 5: pip

## Встановлення пакетів

```bash
# 1. Оновіть pip (рекомендовано)
python3 -m pip install --upgrade pip

# 2. Встановіть популярні пакети
pip install requests
pip install numpy
pip install pandas
pip install pytest

# 3. Встановіть конкретну версію
pip install requests==2.28.0

# 4. Встановіть діапазон версій
pip install "requests>=2.25.0,<3.0"
```

## Перегляд пакетів

```bash
# Список всіх встановлених
pip list

# Інформація про конкретний пакет
pip show requests
# Output:
# Name: requests
# Version: 2.28.2
# Summary: Python HTTP for Humans.
# Location: /path/to/venv/lib/python3.9/site-packages
```

## Видалення

```bash
# Видалити один пакет
pip uninstall requests

# Видалити кілька
pip uninstall requests numpy pandas
```
