"""
Lesson 9: Example 2 - Breakpoints in IDE
Демонстрація використання breakpoints для debugging

ІНСТРУКЦІЇ:
1. Відкрийте цей файл у PyCharm або VS Code
2. Поставте breakpoints на рядки з позначкою 🔴
3. Запустіть у Debug режимі (Shift+F9 у PyCharm, F5 у VS Code)
4. Використовуйте F10 (Step Over), F11 (Step Into)
"""


def calculate_bmi(weight, height):
    """
    Розрахувати індекс маси тіла (BMI).

    Args:
        weight: Вага в кілограмах
        height: Зріст в метрах

    Returns:
        BMI значення та категорія
    """
    # 🔴 BREAKPOINT 1: Поставте тут breakpoint
    # Перевірте значення weight та height у Variables панелі
    bmi = weight / (height ** 2)

    # 🔴 BREAKPOINT 2: Поставте тут breakpoint
    # Перевірте значення bmi
    if bmi < 18.5:
        category = "Недостатня вага"
    elif bmi < 25:
        category = "Нормальна вага"
    elif bmi < 30:
        category = "Надмірна вага"
    else:
        category = "Ожиріння"

    # 🔴 BREAKPOINT 3: Поставте тут breakpoint
    # Перевірте значення category
    return round(bmi, 2), category


def validate_user_data(name, age, email):
    """
    Валідувати дані користувача.

    Args:
        name: Ім'я користувача
        age: Вік
        email: Email адреса

    Returns:
        Tuple (is_valid, errors)
    """
    errors = []

    # 🔴 BREAKPOINT 4: Поставте тут
    # Перевірте початковий стан errors

    # Перевірка імені
    if not name or len(name) < 2:
        errors.append("Ім'я має містити мінімум 2 символи")

    # 🔴 BREAKPOINT 5: Поставте тут
    # Після перевірки імені подивіться на errors

    # Перевірка віку
    if not isinstance(age, int) or age < 0 or age > 150:
        errors.append("Вік має бути від 0 до 150")

    # Перевірка email
    if "@" not in email or "." not in email:
        errors.append("Email має містити @ та .")

    # 🔴 BREAKPOINT 6: Поставте тут
    # Перевірте всі errors перед return

    is_valid = len(errors) == 0
    return is_valid, errors


def process_numbers(numbers):
    """
    Обробити список чисел - знайти суму парних та непарних.

    Args:
        numbers: Список чисел

    Returns:
        Dict з сумами парних та непарних чисел
    """
    # 🔴 BREAKPOINT 7: Поставте тут
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        # 🔴 BREAKPOINT 8: Поставте тут (у циклі)
        # Використовуйте F10 щоб пройти кожну ітерацію
        # Дивіться як змінюються even_sum та odd_sum

        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    # 🔴 BREAKPOINT 9: Поставте тут
    # Перевірте фінальні значення

    return {
        "even_sum": even_sum,
        "odd_sum": odd_sum,
        "total": even_sum + odd_sum
    }


# === ДЕМОНСТРАЦІЯ ===


if __name__ == "__main__":
    print("=" * 70)
    print("ПРИКЛАД 2: BREAKPOINTS DEBUGGING")
    print("=" * 70)
    print("\n📖 ІНСТРУКЦІЇ:")
    print("1. Поставте breakpoints на всі рядки з 🔴")
    print("2. Запустіть Debug (Shift+F9 або F5)")
    print("3. Використовуйте:")
    print("   - F10: Step Over (наступний рядок)")
    print("   - F11: Step Into (увійти в функцію)")
    print("   - Shift+F11: Step Out (вийти з функції)")
    print("   - F9: Resume (продовжити до наступного breakpoint)")

    print("\n" + "=" * 70)
    print("TEST 1: BMI Calculator")
    print("=" * 70)

    # 🔴 BREAKPOINT 10: Поставте тут перед викликом функції
    bmi, category = calculate_bmi(70, 1.75)
    print(f"BMI: {bmi}, Категорія: {category}")

    print("\n" + "=" * 70)
    print("TEST 2: User Validation")
    print("=" * 70)

    # Тест з валідними даними
    is_valid, errors = validate_user_data("Іван", 25, "ivan@example.com")
    print(f"Valid: {is_valid}, Errors: {errors}")

    # Тест з невалідними даними
    is_valid, errors = validate_user_data("I", 200, "invalid-email")
    print(f"Valid: {is_valid}, Errors: {errors}")

    print("\n" + "=" * 70)
    print("TEST 3: Process Numbers")
    print("=" * 70)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = process_numbers(numbers)
    print(f"Even sum: {result['even_sum']}")
    print(f"Odd sum: {result['odd_sum']}")
    print(f"Total: {result['total']}")

    print("\n" + "=" * 70)
    print("💡 ПІДКАЗКИ:")
    print("=" * 70)
    print("✅ Variables панель показує всі змінні")
    print("✅ Watch додайте вирази для спостереження (напр. num % 2)")
    print("✅ Call Stack показує порядок викликів функцій")
    print("✅ Evaluate Expression (Alt+F8) - обчислити будь-який вираз")

