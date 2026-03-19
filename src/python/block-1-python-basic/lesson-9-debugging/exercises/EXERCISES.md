# Вправи - Lesson 9: Debugging

## 🏋️ Завдання 1: Print Debugging - Знайти помилку (EASY)

Створіть файл `exercise_1_print_debug.py`:

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

Створіть файл `exercise_2_breakpoints.py`:

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

Створіть файл `exercise_3_fix_type_error.py`:

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

## 🏋️ Завдання 4: Debug з умовами — off-by-one (MEDIUM)

Створіть файл `exercise_4_debug_conditions.py`:

```python
"""
Вправа 4: Debug логіки з умовами (off-by-one error)
"""


def categorize_age(age):
    """Визначити категорію віку."""
    # ❌ Тут є логічна помилка на межі значень!
    if age < 0:
        return "Invalid"
    elif age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age <= 65:
        return "Adult"
    else:
        return "Senior"


# Тести
test_ages = [5, 12, 13, 17, 18, 30, 64, 65, 80, -5]

for age in test_ages:
    category = categorize_age(age)
    print(f"Age {age:3d} → {category}")

# TODO:
# 1. Поставте breakpoint у функції categorize_age
# 2. Запустіть з age=65 та age=64
# 3. Простежте яка гілка if/elif спрацьовує
# 4. Знайдіть: age=65 потрапляє в "Adult", а має бути "Senior"
# 5. Виправте умову (має бути age < 65, а не age <= 65)

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

Створіть файл `exercise_5_complex_debug.py`:

```python
"""
Вправа 5: Debug складної функції з кількома помилками
"""


def process_student_grades(students):
    """
    Обробити оцінки студентів та повернути статистику.

    Якщо у студента відсутня оцінка — вважаємо що він не склав (grade=0).

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

        # ❌ BUG 1: KeyError якщо 'grade' відсутній
        grade = student['grade']
        total_grade += grade

        # ❌ BUG 2: grade=60 має бути passing, але потрапляє в failing
        if grade > 60:
            results['passing'].append(student['name'])
        else:
            results['failing'].append(student['name'])

    # ❌ BUG 3: ZeroDivisionError якщо список порожній
    results['average_grade'] = total_grade / results['total_students']

    return results


# Тест
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 60},    # Має бути passing!
    {'name': 'Charlie', 'grade': 45},
    {'name': 'Diana'},                # Немає grade — вважаємо 0
]

# TODO:
# 1. Запустіть і отримайте KeyError на Diana
# 2. Виправте BUG 1: student.get('grade', 0) замість student['grade']
# 3. Запустіть знову — Bob потрапляє в failing. Виправте BUG 2: >= 60
# 4. Протестуйте з порожнім списком. Виправте BUG 3: перевірка перед діленням

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

## 🏋️ Завдання 6: Debug функції обробки замовлень (HARD)

Створіть файл `exercise_6_debug_orders.py`:

```python
"""
Вправа 6: Знайдіть та виправте 3 помилки у функції обробки замовлень

Функція має:
- Порахувати загальну вартість (price * quantity)
- Застосувати знижку якщо total > 100
- Повернути підсумок
"""


def process_order(order_items, discount_percent=10):
    """
    Обробити замовлення та повернути підсумок.

    Args:
        order_items: список товарів [{'name': ..., 'price': ..., 'quantity': ...}]
        discount_percent: знижка у відсотках (за замовчуванням 10%)

    Returns:
        dict з 'items_count', 'subtotal', 'discount', 'total'
    """
    subtotal = 0

    for item in order_items:
        # ❌ BUG 1: що якщо quantity відсутній?
        cost = item['price'] * item['quantity']
        subtotal += cost

    # ❌ BUG 2: знижка рахується неправильно
    if subtotal > 100:
        discount = subtotal * discount_percent
    else:
        discount = 0

    # ❌ BUG 3: total має бути subtotal - discount, не навпаки
    total = discount - subtotal

    return {
        'items_count': len(order_items),
        'subtotal': subtotal,
        'discount': round(discount, 2),
        'total': round(total, 2)
    }


# Тест
order = [
    {'name': 'Book', 'price': 25, 'quantity': 2},
    {'name': 'Pen', 'price': 5},            # Немає quantity!
    {'name': 'Notebook', 'price': 15, 'quantity': 3},
]

# TODO:
# 1. Запустіть — отримаєте KeyError на Pen
#    FIX: item.get('quantity', 1)
# 2. Після виправлення — discount буде 950 замість 9.5
#    FIX: discount_percent / 100
# 3. Після виправлення — total буде від'ємним
#    FIX: subtotal - discount

try:
    result = process_order(order)
    print(f"Items: {result['items_count']}")
    print(f"Subtotal: ${result['subtotal']}")
    print(f"Discount: ${result['discount']}")
    print(f"Total: ${result['total']}")
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")

# Очікуваний результат після виправлення:
# Items: 3
# Subtotal: $100
# Discount: $0
# Total: $100.0
```

---

## ✅ Перевірка

### Автоматична перевірка:

```bash
pytest test_exercises.py -v
```

### Критерії:
- [ ] Код запускається без помилок
- [ ] Всі тести проходять
- [ ] Використано print() або breakpoints
- [ ] Зрозуміло ЯК та ЧОМУ виникли помилки

---