# Lesson 5: Install packages with pip

## Мета уроку

Навчитися встановлювати пакети через pip та оновлювати його.

## План

### 1.5 Install packages with pip
- Оновлення pip
- Встановлення пакетів
- Перевірка встановлених пакетів
- Видалення пакетів

## Оновлення pip

```bash
# macOS/Linux
python3 -m pip install --upgrade pip

# Windows
python -m pip install --upgrade pip
```

## Встановлення пакету

```bash
# Встановити останню версію
pip install requests

# Встановити конкретну версію
pip install requests==2.28.0

# Встановити мінімальну версію
pip install "requests>=2.25.0"
```

## Перегляд встановлених пакетів

```bash
# Список всіх встановлених
pip list

# Інформація про пакет
pip show requests
```

## Видалення пакету

```bash
pip uninstall requests
```

## Приклади

Див. папку `examples/`

## Вправи

Див. папку `exercises/`
