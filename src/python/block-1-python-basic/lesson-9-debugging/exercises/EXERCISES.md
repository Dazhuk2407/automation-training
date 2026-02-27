# Вправи - Lesson 9: Debugging

## 🏋️ Завдання 1: Print Debugging - Знайти помилку (EASY)

Створіть файл `exercise-1-print-debug.py`:

```python
"""
Вправа 1: Використайте print() для знаходження помилки
"""

def calculate_rectangle_area(length, width):
    """Розрахувати площу прямокутника."""
    # TODO: Додайте print() для debug
    area = length * width
    return area

def calculate_rectangle_perimeter(length, width):
    """Розрахувати периметр прямокутника."""
    # ❌ Тут є помилка - знайдіть її!
    # TODO: Додайте print() для debug
    perimeter = length + width
    return perimeter

# Тест
length = 10
width = 5

area = calculate_rectangle_area(length, width)
perimeter = calculate_rectangle_perimeter(length, width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")  # Має бути 30, але буде неправильно!

# TODO: 
# 1. Додайте print() для перевірки змінних
# 2. Знайдіть помилку в calculate_rectangle_perimeter
# 3. Виправте формулу (має бути 2 * (length + width))
```

**Очікуваний результат після виправлення:**
```
Area: 50
Perimeter: 30
```

---

## 🏋️ Завдання 2: Breakpoints - Debug у циклі (EASY)

Створіть файл `exercise-2-breakpoints.py`:

```python
"""
Вправа 2: Використайте breakpoints для debug циклу
"""

def find_first_negative(numbers):
    """Знайти перше від'ємне число."""
    # 🔴 Поставте breakpoint тут
    for i, num in enumerate(numbers):
        # 🔴 Поставте breakpoint тут (у циклі)
        if num < 0:
            return i, num
    return None, None

# Тест
numbers = [5, 10, 15, -3, 20, -7]
index, value = find_first_negative(numbers)
print(f"First negative: {value} at index {index}")

# TODO:
# 1. Поставте breakpoints
# 2. Запустіть Debug
# 3. Використайте F10 (Step Over) щоб пройти кожну ітерацію
# 4. Дивіться як змінюються i та num
# 5. Перевірте умову num < 0
```

---

## 🏋️ Завдання 3: Виправити помилку з типами (MEDIUM)

Створіть файл `exercise-3-fix-type-error.py`:

```python
"""
Вправа 3: Знайти та виправити помилку з типами даних
"""

def calculate_total(items):
    """Розрахувати загальну вартість."""
    total = 0
    for item in items:
        # ❌ Тут виникає помилка!
        total += item['price']
    return total

# Тест
items = [
    {'name': 'Laptop', 'price': 1000},
    {'name': 'Mouse', 'price': '50'},  # ❌ Помилка: ціна як string!
    {'name': 'Keyboard', 'price': 80}
]

# TODO:
# 1. Запустіть код - отримаєте TypeError
# 2. Використайте breakpoints для debug
# 3. Знайдіть де виникає помилка
# 4. Виправте: конвертуйте price в int або float
# 5. Додайте перевірку типу

try:
    total = calculate_total(items)
    print(f"Total: {total}")
except TypeError as e:
    print(f"❌ Error: {e}")
```

**Підказка:** Використайте `int(item['price'])` або `float(item['price'])`

---

## 🏋️ Завдання 4: Debug з умовами (MEDIUM)

Створіть файл `exercise-4-debug-conditions.py`:

```python
"""
Вправа 4: Debug логіки з умовами
"""

def categorize_age(age):
    """Визначити категорію віку."""
    # ❌ Тут є логічна помилка!
    if age < 0:
        return "Invalid"
    elif age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 65:
        return "Adult"
    elif age >= 65:
        return "Senior"

# Тести
test_ages = [5, 12, 13, 17, 18, 30, 64, 65, 80, -5]

for age in test_ages:
    category = categorize_age(age)
    print(f"Age {age:3d} → {category}")

# TODO:
# 1. Поставте breakpoint у функції categorize_age
# 2. Перевірте кожну умову
# 3. Знайдіть помилку (вік 65 не обробляється правильно)
# 4. Виправте умову

# Очікуваний результат:
# Age   5 → Child
# Age  12 → Child
# Age  13 → Teenager
# Age  17 → Teenager
# Age  18 → Adult
# Age  30 → Adult
# Age  64 → Adult
# Age  65 → Senior  ← Має бути Senior!
# Age  80 → Senior
# Age  -5 → Invalid
```

---

## 🏋️ Завдання 5: Debug складної функції (HARD)

Створіть файл `exercise-5-complex-debug.py`:

```python
"""
Вправа 5: Debug складної функції з кількома помилками
"""

def process_student_grades(students):
    """
    Обробити оцінки студентів та повернути статистику.
    
    ❌ У цій функції 3 помилки!
    """
    results = {
        'total_students': 0,
        'average_grade': 0,
        'passing': [],
        'failing': []
    }
    
    total_grade = 0
    
    for student in students:
        results['total_students'] += 1
        
        # ❌ BUG 1: Що якщо 'grade' немає?
        grade = student['grade']
        total_grade += grade
        
        # ❌ BUG 2: Неправильна умова
        if grade > 60:  # Має бути >= 60
            results['passing'].append(student['name'])
        else:
            results['failing'].append(student['name'])
    
    # ❌ BUG 3: Що якщо студентів немає?
    results['average_grade'] = total_grade / results['total_students']
    
    return results

# Тест
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 60},    # Має бути passing!
    {'name': 'Charlie', 'grade': 45},
    {'name': 'Diana'},                # Немає grade!
]

# TODO:
# 1. Запустіть і отримайте помилки
# 2. Використайте breakpoints
# 3. Знайдіть всі 3 помилки
# 4. Виправте:
#    - BUG 1: student.get('grade', 0)
#    - BUG 2: grade >= 60
#    - BUG 3: Перевірка перед діленням

try:
    stats = process_student_grades(students)
    print(f"Total students: {stats['total_students']}")
    print(f"Average grade: {stats['average_grade']:.2f}")
    print(f"Passing: {stats['passing']}")
    print(f"Failing: {stats['failing']}")
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")
```

---

## 🏋️ Завдання 6: Створити власний buggy код (HARD)

Створіть файл `exercise-6-create-buggy-code.py`:

```python
"""
Вправа 6: Створіть код з 3 помилками для колеги
"""

# TODO: Напишіть функцію з 3 навмисними помилками:
# 1. Помилка з типами (TypeError)
# 2. Помилка з ключами (KeyError)
# 3. Логічна помилка

def your_buggy_function():
    """
    Ваша функція з помилками.
    
    Приклад: Функція для обробки замовлень
    """
    pass  # TODO: Реалізуйте

# TODO: Додайте тести які викличуть помилки
# TODO: Додайте коментарі де поставити breakpoints

# Обмінюйтесь кодом з колегою та знайдіть помилки один одного!
```

---

## ✅ Перевірка

### Автоматична перевірка:

```bash
# Запустити всі вправи
python exercise-1-print-debug.py
python exercise-2-breakpoints.py
python exercise-3-fix-type-error.py
python exercise-4-debug-conditions.py
python exercise-5-complex-debug.py
```

### Критерії:
- [ ] Код запускається без помилок
- [ ] Всі тести проходять
- [ ] Використано print() або breakpoints
- [ ] Зрозуміло ЯК та ЧОМУ виникли помилки

---

**Готові до Lesson 10?** Якщо виправили 4+ вправи - так! 🚀

