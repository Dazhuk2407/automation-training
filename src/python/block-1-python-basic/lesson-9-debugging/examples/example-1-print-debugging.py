"""
Lesson 9: Example 1 - Print Debugging
Демонстрація debugging за допомогою print()
"""


def calculate_discount(price, discount_percent, member_bonus=0):
    """
    Розрахувати знижку для товару.

    Args:
        price: Ціна товару
        discount_percent: Відсоток знижки
        member_bonus: Додаткова знижка для членів (%)

    Returns:
        Фінальна ціна після знижок
    """
    # 🔍 DEBUG: Перевірка вхідних даних
    print(f"🔍 DEBUG: Input values:")
    print(f"  price = {price}")
    print(f"  discount_percent = {discount_percent}")
    print(f"  member_bonus = {member_bonus}")

    # Розрахунок базової знижки
    base_discount = price * (discount_percent / 100)
    print(f"\n🔍 DEBUG: base_discount = {base_discount}")

    # Розрахунок знижки для члена
    if member_bonus > 0:
        member_discount = price * (member_bonus / 100)
        print(f"🔍 DEBUG: member_discount = {member_discount}")
    else:
        member_discount = 0
        print(f"🔍 DEBUG: No member discount")

    # Загальна знижка
    total_discount = base_discount + member_discount
    print(f"\n🔍 DEBUG: total_discount = {total_discount}")

    # Фінальна ціна
    final_price = price - total_discount
    print(f"🔍 DEBUG: final_price = {final_price}")

    return final_price


def find_max_value(numbers):
    """
    Знайти максимальне значення в списку.

    Args:
        numbers: Список чисел

    Returns:
        Максимальне число
    """
    print(f"\n🔍 DEBUG: Finding max in {numbers}")

    if not numbers:
        print("🔍 DEBUG: List is empty, returning None")
        return None

    max_value = numbers[0]
    print(f"🔍 DEBUG: Initial max_value = {max_value}")

    for i, num in enumerate(numbers[1:], start=1):
        print(f"🔍 DEBUG: Step {i}: checking {num}")
        if num > max_value:
            print(f"🔍 DEBUG:   {num} > {max_value}, updating max_value")
            max_value = num
        else:
            print(f"🔍 DEBUG:   {num} <= {max_value}, no change")

    print(f"🔍 DEBUG: Final max_value = {max_value}")
    return max_value


# === ДЕМОНСТРАЦІЯ ===


if __name__ == "__main__":
    print("=" * 70)
    print("ПРИКЛАД 1: PRINT DEBUGGING")
    print("=" * 70)

    # Тест 1: Розрахунок знижки
    print("\n📝 TEST 1: Звичайна знижка")
    print("-" * 70)
    result = calculate_discount(1000, 20)
    print(f"\n✅ Result: {result} грн\n")

    # Тест 2: Знижка з бонусом
    print("\n📝 TEST 2: Знижка з бонусом для члена")
    print("-" * 70)
    result = calculate_discount(1000, 20, member_bonus=5)
    print(f"\n✅ Result: {result} грн\n")

    # Тест 3: Пошук максимального значення
    print("\n📝 TEST 3: Пошук максимуму")
    print("-" * 70)
    numbers = [5, 12, 3, 9, 15, 7]
    max_num = find_max_value(numbers)
    print(f"\n✅ Maximum: {max_num}\n")

    print("=" * 70)
    print("💡 ПІДКАЗКИ:")
    print("=" * 70)
    print("1. Використовуйте 🔍 DEBUG: для позначення debug виводів")
    print("2. Виводьте значення змінних на кожному кроці")
    print("3. Перевіряйте умови (if/else)")
    print("4. Після знаходження помилки - видаліть print()")

