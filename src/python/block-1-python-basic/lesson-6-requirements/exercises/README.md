# Вправи - Lesson 6: requirements.txt

## Завдання 1: Встановіть пакети

```bash
# Активуйте venv (якщо потрібно)
source venv/bin/activate

# Встановіть пакети
pip install requests pytest numpy pandas
```

## Завдання 2: Генеруйте requirements.txt

```bash
# Зберегти список залежностей
pip freeze > requirements.txt

# Перегляньте вміст
cat requirements.txt
```

## Завдання 3: Видаліть пакети

```bash
# Видаліть всі встановлені пакети
pip uninstall -r requirements.txt -y
```

## Завдання 4: Встановіть з файлу

```bash
# Встановіть всі пакети з файлу
pip install -r requirements.txt

# Перевірте
pip list
```

## Завдання 5: Оновіть залежності

```bash
# Оновіть пакети
pip install --upgrade -r requirements.txt

# Оновіть файл
pip freeze > requirements.txt
```

## Завдання 6: Ручна редакція

Відредагуйте `requirements.txt` за бажанням:

```
requests>=2.25.0
pytest>=7.0
numpy>=1.20.0
pandas
```

Встановіть:
```bash
pip install -r requirements.txt
```

---

**✅ Коли requirements.txt працює правильно - переходьте до Lesson 7**
