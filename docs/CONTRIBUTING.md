# Contributing - Як Розширювати Проект

Цей документ описує як додавати нові уроки, блоки та категорії до проекту.

## 📋 Вимоги до Нового Матеріалу

### Якість Контенту

- ✅ **Точність** - Матеріал повинен бути технічно правильним
- ✅ **Ясність** - Концепції пояснені простою мовою
- ✅ **Практичність** - Приклади мають реальну цінність
- ✅ **Повнота** - Охоплює тему досить детально
- ✅ **Актуальність** - Використовує актуальні версії

### Структура

- ✅ **Послідовність** - Логічна послідовність тем
- ✅ **Прогресія** - От простого до складного
- ✅ **Зв'язність** - Теми пов'язані одна з одною
- ✅ **Модульність** - Кожен урок незалежний

---

## ➕ Додавання Нового Уроку (Lesson 2-8)

### Крок 1: Скопіюйте Структуру

```bash
# Приклад: Додати Lesson 2 для Python
cp -r src/python/block-1-python-basic/lesson-1/ \
      src/python/block-1-python-basic/lesson-2/
```

### Крок 2: Оновіть README.md

```markdown
# Lesson 2: Оператори та умовні конструкції

## Теорія
- Поясніть основні концепції
- Дайте 2-3 кодові приклади
- Посилання на документацію

## Приклади
- Див. папку `examples/`

## Вправи
- Виконайте завдання в папці `exercises/`
```

### Крок 3: Додайте Приклади

Файл: `lesson-2/examples/operators.py`

```python
# Арифметичні оператори
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000

# Логічні оператори
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Умовні конструкції
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

### Крок 4: Додайте Вправи

Файл: `lesson-2/exercises/exercise-1.py`

```python
def is_even(number):
    """Check if number is even"""
    # TODO: Напишіть код
    pass


def grade_from_score(score):
    """Return grade based on score"""
    # TODO: if score >= 90: return 'A'
    # TODO: if score >= 80: return 'B'
    # TODO: ...
    pass


def categorize_age(age):
    """Categorize age into groups"""
    # TODO: Напишіть код використовуючи if/elif/else
    pass
```

Файл: `lesson-2/exercises/test_exercise.py`

```python
import pytest
from exercise_1 import is_even, grade_from_score, categorize_age


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True


def test_grade_from_score():
    assert grade_from_score(95) == 'A'
    assert grade_from_score(85) == 'B'
    assert grade_from_score(75) == 'C'


def test_categorize_age():
    assert categorize_age(5) == 'Child'
    assert categorize_age(15) == 'Teenager'
    assert categorize_age(30) == 'Adult'
```

### Крок 5: Додайте Питання

Файл: `lesson-2/QUESTIONS.md`

```markdown
# Питання для самоперевірки - Lesson 2

## 🎯 Оператори

1. **Арифметичні оператори**
   - Назвіть всі 7 операторів
   - Приклади для кожного

2. **Логічні оператори**
   - `and`, `or`, `not`
   - Таблиця істинності

## ✅ Умовні Конструкції

3. **if-elif-else**
   - Структура
   - Indentation в Python
   - Скільки `elif` може бути?

## 💡 Практичні Завдання

4. **Напишіть код для:**
   - Перевірити чи число парне
   - Визначити оцінку за середнім балом
```

### Крок 6: Перевірте все

```bash
# Перейдіть в папку урока
cd src/python/block-1-python-basic/lesson-2/

# Запустіть приклади
python examples/operators.py

# Запустіть тести
pytest exercises/test_exercise.py -v

# Перевірте чи все змістовне
cat README.md
cat QUESTIONS.md
```

---

## 🏗️ Додавання Нового Блоку

### Крок 1: Створіть Структуру

```bash
# Приклад: Додати block-2-python-advanced
mkdir -p src/python/block-2-python-advanced/lesson-1/

# Створіть папки
mkdir -p src/python/block-2-python-advanced/lesson-1/{examples,exercises}
```

### Крок 2: Додайте README для Блоку

Файл: `src/python/block-2-python-advanced/README.md`

```markdown
# Block 2: Python Advanced

Продвинуті концепції Python для експертів.

## 📚 Уроки (8 занять)

### Lesson 1: Декоратори
- Синтаксис декораторів
- Параметризовані декоратори
- Практичні приклади

### Lesson 2: Генератори
- yield та генератор функції
- Списки vs генератори
- Оптимізація пам'яті

### ... Lesson 3-8

## 🚀 Як почати

1. Почніть з `lesson-1`
2. Прочитайте README в уроці
3. Вивчіть приклади
4. Виконайте вправи
```

### Крок 3: Додайте Lesson 1 для Блоку

Скопіюйте структуру та оновіть для нової теми:

```bash
cp -r src/python/block-1-python-basic/lesson-1/* \
      src/python/block-2-python-advanced/lesson-1/
```

Потім оновіть вміст для нової теми (декоратори тощо)

---

## 🆕 Додавання Нової Категорії

### Крок 1: Створіть Структуру

```bash
# Приклад: Додати нову категорію "Docker"
mkdir -p src/docker/block-1-docker-basic/lesson-1/{examples,exercises}
```

### Крок 2: Додайте Основні Файли

Файл: `src/docker/README.md`

```markdown
# Docker Training

Вивчення Docker для контейнеризації.

## Блоки

- block-1-docker-basic
- block-2-docker-advanced (можна додати)
```

### Крок 3: Наповніть Lesson 1

Як в п. "Додавання Нового Уроку"

---

## ✅ Контрольний Список при Додаванні Матеріалу

### Для Нового Уроку

- [ ] Папка `lesson-X` створена
- [ ] `README.md` написаний і містить теорію
- [ ] `QUESTIONS.md` написаний з 10-20 питаннями
- [ ] `examples/` папка з 2-3 прикладами
- [ ] `exercises/` папка з вправами
- [ ] `test_*.py` файл з автоматичними тестами
- [ ] Всі тести проходять (PASSED ✅)
- [ ] README.md има посилання на examples/ та exercises/
- [ ] QUESTIONS.md має практичні завдання
- [ ] Код має коментарі поясняючи логіку

### Для Нового Блоку

- [ ] Папка `block-X-name` створена
- [ ] `README.md` описує блок та всі 8 уроків
- [ ] `lesson-1` повністю реалізований
- [ ] Можна скопіювати структуру для lesson-2-8
- [ ] Логічна послідовність тем

### Для Нової Категорії

- [ ] Папка категорії створена в `src/`
- [ ] `README.md` описує категорію
- [ ] `block-1-basic` повністю реалізований
- [ ] Можна розширювати додавання нових блоків

---

## 📝 Написання Хорошого README.md

### Структура

```markdown
# Lesson X: Назва Теми

## Теорія
- Основні концепції
- 2-3 кодові приклади з пояснення

## Синтаксис
- Показати синтаксис
- Пояснити кожну частину

## Приклади
- Посилання на файли в examples/

## Вправи
- Посилання на exercises/

## Резюме
- Ключові моменти
- Що дальше?
```

### Поради

- ✅ Не копіюйте весь код в README - посилайтесь на файли
- ✅ Використовуйте кодові блоки з мовою: \`\`\`python
- ✅ Поясніть як запустити код
- ✅ Додайте посилання на документацію

---

## 🧪 Написання Хороших Тестів

### Структура Тесту

```python
import pytest
from exercise_1 import my_function


def test_my_function_success():
    """Test normal case"""
    assert my_function(1, 2) == 3


def test_my_function_edge_case():
    """Test edge case"""
    assert my_function(0, 0) == 0


def test_my_function_error():
    """Test error handling"""
    with pytest.raises(ValueError):
        my_function(-1, 2)
```

### Поради

- ✅ Кожен тест повинен тестувати одне
- ✅ Назви тестів мають бути описовими
- ✅ Додавайте docstring що пояснює тест
- ✅ Не залежайте від порядку виконання тестів

---

## 🔍 Перевірка Якості

Перед тим як commit нове матеріал:

```bash
# 1. Перевірте синтаксис Python
python -m py_compile lesson-X/examples/*.py
python -m py_compile lesson-X/exercises/*.py

# 2. Запустіть всі тести
pytest lesson-X/exercises/ -v

# 3. Перевірте читаність README
cat lesson-X/README.md

# 4. Перевірте питання
cat lesson-X/QUESTIONS.md

# 5. Запустіть приклади
python lesson-X/examples/example1.py
```

---

## 🚀 Pull Request Process

1. **Fork** репозиторій
2. **Створіть нову гілку:** `git checkout -b feature/new-lesson`
3. **Додайте зміни** (новий урок, блок або категорію)
4. **Перевірте якість** (тести, синтаксис, формат)
5. **Commit:** `git commit -m "Add: Lesson X - Topic Name"`
6. **Push:** `git push origin feature/new-lesson`
7. **Створіть Pull Request** з описом змін

---

## 💡 Ідеї для Розширення

### Нові Блоки

- block-2-python-advanced (Декоратори, генератори, async)
- block-2-python-oop (Наслідування, поліморфізм, design patterns)
- block-2-pytest-advanced (Плагіни, конфіги, CI/CD)
- block-2-playwright-advanced (POM, API тестування, E2E)
- block-2-git-advanced (Rebase, cherry-pick, workflows)

### Нові Категорії

- Docker (Контейнеризація)
- Kubernetes (Оркестрація)
- CI/CD (GitHub Actions, GitLab CI)
- REST API (Тестування API)
- Database Testing (SQL, NoSQL)

---

## 🤝 Спільнота та Підтримка

- 💬 Запитуйте на GitHub Issues
- 📧 Зв'язуйтесь з maintainers
- 👥 Ділитесь вашими матеріалами
- ✨ Будьте добрі до новачків

---

**Дякуємо за допомогу в розвитку проекту!** 🙏

