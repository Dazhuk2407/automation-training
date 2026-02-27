# Приклади - Lesson 6: requirements.txt

## Генерування файлу

```bash
# 1. Встановіть кілька пакетів
pip install requests pytest numpy

# 2. Генеруйте requirements.txt
pip freeze > requirements.txt

# 3. Перегляньте вміст
cat requirements.txt
```

Вміст файлу:
```
certifi==2023.7.22
charset-normalizer==3.3.2
idna==3.4
numpy==1.24.3
pytest==7.4.3
requests==2.31.0
urllib3==2.0.6
```

## Встановлення з файлу

```bash
# На новій машині
pip install -r requirements.txt

# Всі залежності встановляться автоматично
```

## Оновлення залежностей

```bash
# Оновити всі пакети
pip install --upgrade -r requirements.txt

# Генеруйте новий requirements.txt
pip freeze > requirements.txt
```

## Ручна редакція

```
# requirements.txt
requests>=2.25.0,<3.0
pytest>=7.0
numpy>=1.20.0
```

Встановлення:
```bash
pip install -r requirements.txt
```
