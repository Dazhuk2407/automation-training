# Lesson Template - Шаблон для Нових Уроків

Цей файл містить шаблон для швидкого створення нових уроків.

## 📋 Структура Шаблону

```
lesson-X/
├── README.md           # Теорія (Копіюйте шаблон нижче)
├── QUESTIONS.md        # Питання (Копіюйте шаблон нижче)
├── examples/           # Приклади
│   ├── example1.py
│   └── example2.py
└── exercises/          # Вправи
    ├── exercise-1.py
    ├── exercise-2.py
    └── test_exercise.py
```

---

## 📖 Шаблон README.md

```markdown
# Lesson X: Назва Теми

## Теорія

### Підрозділ 1: Основні Концепції

Пояснення...

**Приклад:**
\`\`\`python
# Код з пояснення
code_example = "value"
print(code_example)
\`\`\`

### Підрозділ 2: Синтаксис

Пояснення синтаксису...

**Приклад:**
\`\`\`python
# Як писати код
correct_syntax = True
\`\`\`

### Підрозділ 3: Best Practices

Рекомендації...

## Резюме

- Ключова точка 1
- Ключова точка 2
- Ключова точка 3

## Приклади

Див. папку `examples/`:
- `example1.py` - ...
- `example2.py` - ...

## Вправи

Виконайте завдання в папці `exercises/`:
- `exercise-1.py` - ...
- `exercise-2.py` - ...
- `test_exercise.py` - автоматичні тести

## Що дальше?

Перейдіть до Lesson X+1: [Назва]
```

---

## ❓ Шаблон QUESTIONS.md

```markdown
# Питання для самоперевірки - Lesson X: Назва

Після вивчення цього уроку ви повинні мати змогу відповісти на наступні питання:

## 🎯 Базові Концепції (5 питань)

1. **Що таке [Концепція]?**
   - Пояснення що це таке
   - Навіщо це потрібно

2. **Як [операція] працює?**
   - Синтаксис
   - Приклади

3. **Різниця між А та B**
   - Коли використовувати А
   - Коли використовувати B

4. **Назвіть 3 приклади [теми]**
   - Приклад 1
   - Приклад 2
   - Приклад 3

5. **Який порядок операцій?**
   - Послідовність дій
   - Приклад

## ✅ Практичні Навички (5-10 питань)

6. **Напишіть код для:**
   - Завдання 1
   - Завдання 2
   - Завдання 3

7. **Вирішіть проблему:**
   - Опис проблеми
   - Як подолати

8. **Модифікуйте приклад:**
   - Зробіть щось інше
   - Поясніть чому

## 🧠 Глибше Розуміння (3-5 питань)

9. **Прдійсні випадки використання**
   - Реальний світ приклад 1
   - Реальний світ приклад 2

10. **Зв'язки з іншими темами**
    - Як це стосується попередніх уроків
    - Як це буде потрібне в майбутніх уроках

---

## 📝 Рекомендації

- Напишіть письмові відповіді
- Напишіть код для кожного завдання
- Порівняйте з матеріалом
- Обговоріть з когось іншого

---

**Коли впевнено відповідаєте на більшість питань, ви готові до наступного уроку!** ✅
```

---

## 💡 Шаблон example.py

```python
"""
Example: [Опис що показує цей приклад]

Це демонструє:
- Концепція 1
- Концепція 2
- Концепція 3
"""


# Приклад 1: Базовий синтаксис
def example_1():
    """Пояснення що робить цей приклад"""
    result = "value"
    print(f"Результат: {result}")
    return result


# Приклад 2: Більш складний приклад
def example_2():
    """Пояснення що робить цей приклад"""
    data = [1, 2, 3, 4, 5]
    result = sum(data)
    print(f"Сума: {result}")
    return result


# Приклад 3: Best practice
def example_3():
    """Пояснення що робить цей приклад"""
    # Добра практика
    value = 42
    
    # Перевірити результат
    assert value == 42
    print("Все готово!")
    return value


if __name__ == "__main__":
    print("=" * 50)
    print("Example 1: Базовий синтаксис")
    print("=" * 50)
    example_1()
    
    print("\n" + "=" * 50)
    print("Example 2: Більш складний приклад")
    print("=" * 50)
    example_2()
    
    print("\n" + "=" * 50)
    print("Example 3: Best practice")
    print("=" * 50)
    example_3()
```

---

## 🏋️ Шаблон exercise-X.py

```python
"""
Exercise X: [Опис завдання]

Завдання:
- Завдання 1
- Завдання 2
- Завдання 3
"""


def function_1(param1, param2):
    """
    Пояснення що повинна робити функція.
    
    Args:
        param1: Опис параметра 1
        param2: Опис параметра 2
    
    Returns:
        Опис що повертається
    
    Example:
        >>> function_1(1, 2)
        3
    """
    # TODO: Напишіть код
    pass


def function_2(data):
    """
    Пояснення що повинна робити функція.
    
    Args:
        data: Опис параметра
    
    Returns:
        Опис що повертається
    """
    # TODO: Напишіть код
    pass


def function_3(value):
    """
    Пояснення що повинна робити функція.
    
    Args:
        value: Опис параметра
    
    Returns:
        Опис що повертається
    
    Raises:
        ValueError: Коли ...
    """
    # TODO: Напишіть код
    pass
```

---

## 🧪 Шаблон test_exercise.py

```python
"""
Tests for Exercise X

Запустити: pytest test_exercise.py -v
"""

import pytest
from exercise_1 import function_1, function_2, function_3


class TestFunction1:
    """Tests for function_1"""
    
    def test_function_1_basic(self):
        """Test basic case"""
        result = function_1(1, 2)
        assert result == 3
    
    def test_function_1_zero(self):
        """Test with zero"""
        result = function_1(0, 0)
        assert result == 0
    
    def test_function_1_negative(self):
        """Test with negative numbers"""
        result = function_1(-1, -2)
        assert result == -3


class TestFunction2:
    """Tests for function_2"""
    
    def test_function_2_list(self):
        """Test with list"""
        result = function_2([1, 2, 3])
        assert result == 6
    
    def test_function_2_empty(self):
        """Test with empty list"""
        result = function_2([])
        assert result == 0


class TestFunction3:
    """Tests for function_3"""
    
    def test_function_3_valid(self):
        """Test valid input"""
        result = function_3(10)
        assert result is not None
    
    def test_function_3_error(self):
        """Test error handling"""
        with pytest.raises(ValueError):
            function_3(-1)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

---

## ⚡ Швидкий Start для Нового Уроку

### 1. Скопіюйте структуру

```bash
cp -r lesson-1/ lesson-X/
cd lesson-X/
```

### 2. Оновіть README.md

```bash
# Відкрийте в редакторі та оновіть
code README.md
```

### 3. Оновіть QUESTIONS.md

```bash
code QUESTIONS.md
```

### 4. Додайте приклади

```bash
code examples/example1.py
code examples/example2.py
```

### 5. Додайте вправи

```bash
code exercises/exercise-1.py
code exercises/test_exercise.py
```

### 6. Перевірте все

```bash
# Запустіть приклади
python examples/example1.py

# Запустіть тести
pytest exercises/test_exercise.py -v
```

---

## 📝 Чек-лист Новго Уроку

Перед тим як закінчити урок:

- [ ] README.md написаний з теорією та прикладами
- [ ] QUESTIONS.md написаний з 10-20 питаннями
- [ ] examples/ папка з 2-3 робочими прикладами
- [ ] exercises/ папка з вправами та тестами
- [ ] Всі тести проходять (pytest exercises/test_exercise.py)
- [ ] Код має коментарі
- [ ] Немає синтаксичних помилок
- [ ] README має посилання на examples/ та exercises/
- [ ] QUESTIONS.md має практичні завдання

---

## 🎯 Поради

- ✅ Почніть з простих прикладів
- ✅ Прогресуйте до складніших
- ✅ Завжди показуйте output
- ✅ Додавайте коментарі до коду
- ✅ Тестуйте перед публікацією
- ✅ Просьте feedback від інших

---

## 📚 Приклади добрих уроків

- `src/python/block-1-python-basic/lesson-1/` - Змінні та типи даних
- `src/pytest/block-1-pytest-basic/lesson-1/` - Основи Pytest
- `src/playwright/block-1-playwright-basic/lesson-1/` - Основи Playwright
- `src/git/block-1-git-basic/lesson-1/` - Основи Git

---

**Готові створити новий урок? Скопіюйте цей шаблон!** 🚀

