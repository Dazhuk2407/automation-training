# Lesson 1: Встановлення Pytest

## 🎯 Learning Outcomes

Після цього уроку ви зможете:

- ✅ Встановити pytest у віртуальне середовище
- ✅ Перевірити що pytest працює
- ✅ Зафіксувати залежності в `requirements.txt`
- ✅ Відтворити середовище з нуля

---

## 📋 Передумови

Перед початком переконайтесь що у вас є:

- Python 3.8+
- Активоване віртуальне середовище (venv)

Якщо ні — див. Python курс: `block-1-python-basic/lesson-4-virtual-environment`.

---

## 📖 Теорія

### 1. Встановлення pytest

```bash
python -m pip install pytest
```

**Чому `python -m pip`, а не просто `pip`?**

`python -m pip` гарантує, що пакет встановиться саме в те середовище, де працює ваш Python. Якщо використовувати просто `pip`, він може вказувати на інший Python (глобальний, системний), і ви отримаєте `ModuleNotFoundError` при спробі запустити pytest.

---

### 2. Перевірка встановлення

```bash
# Версія pytest
pytest --version

# Довідка по командам
pytest --help

# Запуск тестів (поки що нічого не знайде — це нормально)
pytest
```

Детальний запуск тестів (файл, папка, опції `-v`, `-s`, `-x`) розглянемо у Lesson 7.

---

### 3. Фіксація залежностей у requirements.txt

Після встановлення зафіксуйте версії:

```bash
python -m pip freeze > requirements.txt
```

Результат — файл `requirements.txt`:

```txt
iniconfig==2.0.0
packaging==24.0
pluggy==1.5.0
pytest==8.3.2
```

**Навіщо фіксувати версії?**

- **Відтворюваність** — кожен, хто працює з проєктом, отримає ідентичне середовище
- **Стабільність** — нова версія бібліотеки не зламає проєкт несподівано
- **CI/CD** — серверні білди використовують `requirements.txt` для встановлення залежностей

---

### 4. Відтворення середовища

Коли інший розробник клонує проєкт, він встановлює все одною командою:

```bash
python -m pip install -r requirements.txt
```

Це стандартний production flow:

```
git clone <repo>
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
pytest
```

---

### 5. Корисні команди pip

```bash
# Встановити конкретну версію
python -m pip install pytest==8.3.2

# Оновити до останньої версії
python -m pip install --upgrade pytest

# Подивитись встановлені пакети
python -m pip list

# Подивитись інформацію про пакет
python -m pip show pytest
```

---

## ⚠️ Типові проблеми

| Проблема | Причина | Рішення |
|----------|---------|---------|
| `pytest: command not found` | venv не активований | `source venv/bin/activate` |
| `ModuleNotFoundError: No module named 'pytest'` | pytest встановлено в інше середовище | Перевірте: `which python` та `python -m pip list` |
| Стара версія pytest | Встановлено глобально, а не в venv | `python -m pip install --upgrade pytest` |
| `pip` встановлює не туди | `pip` вказує на системний Python | Завжди використовуйте `python -m pip` |

---

## 💡 Приклади

Див. папку `examples/`

## 🏋️ Вправи

Див. папку `exercises/`

## ❓ Питання

Див. `QUESTIONS.md`

---

**Далі:** `lesson-2-project-structure` — структура pytest проєкту