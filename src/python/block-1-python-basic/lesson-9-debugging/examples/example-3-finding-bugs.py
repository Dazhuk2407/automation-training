"""
Lesson 9: Example 3 - Finding and Fixing Bugs
Складніший приклад з реальними помилками для debugging

❌ Цей код містить 5 помилок - знайдіть їх за допомогою debugger!
"""


def calculate_average_grade(grades):
    """
    Розрахувати середній бал.

    Args:
        grades: Список оцінок

    Returns:
        Середній бал
    """
    # 🔴 BREAKPOINT: Поставте тут
    # 🐛 BUG 1: Що якщо grades порожній?
    total = sum(grades)
    average = total / len(grades)  # ❌ ZeroDivisionError якщо grades = []
    return average


def filter_passing_students(students):
    """
    Відфільтрувати студентів які склали (оцінка >= 60).

    Args:
        students: Список словників з даними студентів

    Returns:
        Список студентів які склали
    """
    # 🔴 BREAKPOINT: Поставте тут
    passing = []

    for student in students:
        # 🐛 BUG 2: Що якщо ключа 'grade' немає?
        if student['grade'] >= 60:  # ❌ KeyError якщо немає 'grade'
            passing.append(student)

    return passing


def calculate_total_price(items):
    """
    Розрахувати загальну вартість товарів.

    Args:
        items: Список товарів з цінами

    Returns:
        Загальна вартість
    """
    # 🔴 BREAKPOINT: Поставте тут
    total = 0

    for item in items:
        # 🐛 BUG 3: Неправильний тип даних
        price = item['price']  # Якщо price = "100" (string)?
        total = total + price  # ❌ TypeError: int + str

    return total


def get_student_rank(grade):
    """
    Визначити ранг студента на основі оцінки.

    Args:
        grade: Оцінка студента (0-100)

    Returns:
        Ранг: A, B, C, D, F
    """
    # 🔴 BREAKPOINT: Поставте тут
    # 🐛 BUG 4: Логічна помилка в умовах
    if grade >= 90:
        return "A"
    elif grade > 80:  # ❌ Має бути >= 80
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


def count_word_occurrences(text, word):
    """
    Порахувати скільки разів слово зустрічається в тексті.

    Args:
        text: Текст для пошуку
        word: Слово яке шукаємо

    Returns:
        Кількість входжень
    """
    # 🔴 BREAKPOINT: Поставте тут
    # 🐛 BUG 5: Не враховується регістр
    words = text.split()
    count = words.count(word)  # ❌ "Hello" != "hello"
    return count


# === ТЕСТИ (З ПОМИЛКАМИ) ===


if __name__ == "__main__":
    print("=" * 70)
    print("ПРИКЛАД 3: ЗНАЙДІТЬ ТА ВИПРАВТЕ ПОМИЛКИ")
    print("=" * 70)

    print("\n🐛 BUG 1: Empty list")
    print("-" * 70)
    try:
        result = calculate_average_grade([])  # ❌ Помилка!
        print(f"Average: {result}")
    except Exception as e:
        print(f"❌ ERROR: {type(e).__name__}: {e}")
        print("💡 FIX: Перевірте чи список не порожній")

    print("\n🐛 BUG 2: Missing key")
    print("-" * 70)
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob"},  # ❌ Немає 'grade'
    ]
    try:
        passing = filter_passing_students(students)
        print(f"Passing: {passing}")
    except Exception as e:
        print(f"❌ ERROR: {type(e).__name__}: {e}")
        print("💡 FIX: Використайте .get('grade', 0)")

    print("\n🐛 BUG 3: Type mismatch")
    print("-" * 70)
    items = [
        {"name": "Laptop", "price": 1000},
        {"name": "Mouse", "price": "50"},  # ❌ String замість int
    ]
    try:
        total = calculate_total_price(items)
        print(f"Total: {total}")
    except Exception as e:
        print(f"❌ ERROR: {type(e).__name__}: {e}")
        print("💡 FIX: Конвертуйте price в int або float")

    print("\n🐛 BUG 4: Logic error")
    print("-" * 70)
    # Оцінка 80 має бути "B", але функція поверне "C"
    rank = get_student_rank(80)
    print(f"Grade 80 → Rank: {rank}")
    print(f"Очікується: B, Отримано: {rank}")
    if rank != "B":
        print("❌ Логічна помилка! Умова має бути >= 80")

    print("\n🐛 BUG 5: Case sensitivity")
    print("-" * 70)
    text = "Hello world Hello Python hello"
    count = count_word_occurrences(text, "hello")
    print(f"Count of 'hello': {count}")
    print(f"Очікується: 3, Отримано: {count}")
    if count != 3:
        print("❌ Не враховується регістр!")
        print("💡 FIX: text.lower().split()")

    print("\n" + "=" * 70)
    print("🎯 ЗАВДАННЯ:")
    print("=" * 70)
    print("1. Використайте breakpoints для кожної помилки")
    print("2. Інспектуйте змінні в кожній точці")
    print("3. Зрозумійте ЧОМУ виникає помилка")
    print("4. Виправте код")
    print("5. Перевірте що всі тести проходять")

