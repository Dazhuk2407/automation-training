# Lesson 6: Working with requirements.txt (install, freeze, update)

## Мета уроку

Навчитися працювати з requirements.txt для керування залежностями.

## 📚 Корисні посилання

- [Офіційна документація pip requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/)

## План

### 1.6 Working with requirements.txt
- Створення requirements.txt
- pip freeze
- pip install -r
- Оновлення залежностей

## Генерування requirements.txt

```bash
# Зберегти всі встановлені пакети
pip freeze > requirements.txt
```

## Встановлення з файлу

```bash
# Встановити всі залежності
pip install -r requirements.txt

# З конкретної версії Python
python3.12 -m pip install -r requirements.txt
```

## Ручна редакція

```
# requirements.txt
requests==2.28.2
pytest>=7.0.0
numpy>=1.20.0
```

## Оновлення

```bash
# Оновити пакети з файлу
pip install --upgrade -r requirements.txt
```

## Приклади

Див. папку `examples/`

## Вправи

Див. папку `exercises/`
