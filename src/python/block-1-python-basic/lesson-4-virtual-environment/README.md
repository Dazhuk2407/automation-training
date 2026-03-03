# Lesson 4: Create and use a virtual environment (venv)

## Мета уроку

Навчитися створювати та використовувати віртуальні середовища Python.

## План

### 1.4 Create and use a virtual environment
- Навіщо потрібен venv?
- Створення venv
- Активація та деактивація
- Ізоляція залежностей

## Навіщо потрібен venv?

- Ізоляція залежностей проєкту
- Різні версії пакетів для різних проєктів
- Безпека та чистота системи

## Створення venv

```bash
# Створити venv
python3 -m venv venv

# Або з іншою назвою
python3 -m venv .venv
```

## Активація

```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

## Деактивація

```bash
deactivate
```

## Приклади

Див. папку `examples/`

## Вправи

Див. папку `exercises/`
