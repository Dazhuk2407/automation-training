"""
Lesson 8: Example 2 - Використання Black для форматування
Демонстрація автоматичного форматування коду
"""

# === КОД ДО ФОРМАТУВАННЯ (НЕОХАЙНИЙ) ===

def process_user_data(name,age,city,email,phone):
    user={'name':name,'age':age,'city':city,'email':email,'phone':phone}
    if age>=18:status='adult'
    else:status='minor'
    user['status']=status
    return user

def calculate_discount(price,discount_percent,is_member,purchase_count):
    if is_member:base_discount=discount_percent*1.5
    else:base_discount=discount_percent
    if purchase_count>10:bonus=5
    elif purchase_count>5:bonus=3
    else:bonus=0
    total_discount=base_discount+bonus;final_price=price*(1-total_discount/100)
    return final_price


# === КОД ПІСЛЯ ФОРМАТУВАННЯ BLACK (ЧИСТИЙ) ===


def process_user_data_formatted(name, age, city, email, phone):
    """
    Обробити дані користувача.

    Args:
        name: Ім'я
        age: Вік
        city: Місто
        email: Email
        phone: Телефон

    Returns:
        Словник з даними користувача
    """
    user = {
        "name": name,
        "age": age,
        "city": city,
        "email": email,
        "phone": phone,
    }

    if age >= 18:
        status = "adult"
    else:
        status = "minor"

    user["status"] = status
    return user


def calculate_discount_formatted(
    price, discount_percent, is_member, purchase_count
):
    """
    Розрахувати знижку.

    Args:
        price: Базова ціна
        discount_percent: Відсоток знижки
        is_member: Чи є членом
        purchase_count: Кількість покупок

    Returns:
        Фінальна ціна зі знижкою
    """
    if is_member:
        base_discount = discount_percent * 1.5
    else:
        base_discount = discount_percent

    if purchase_count > 10:
        bonus = 5
    elif purchase_count > 5:
        bonus = 3
    else:
        bonus = 0

    total_discount = base_discount + bonus
    final_price = price * (1 - total_discount / 100)

    return final_price


# === ДЕМОНСТРАЦІЯ ===


if __name__ == "__main__":
    print("=" * 70)
    print("ДЕМОНСТРАЦІЯ BLACK ФОРМАТУВАННЯ")
    print("=" * 70)

    # Тестування функції
    user = process_user_data_formatted(
        name="Іван",
        age=25,
        city="Київ",
        email="ivan@example.com",
        phone="+380123456789"
    )

    print("\n✅ Відформатовані дані користувача:")
    for key, value in user.items():
        print(f"  {key}: {value}")

    # Розрахунок знижки
    original_price = 1000
    final_price = calculate_discount_formatted(
        price=original_price,
        discount_percent=10,
        is_member=True,
        purchase_count=12
    )

    print(f"\n✅ Розрахунок знижки:")
    print(f"  Базова ціна: {original_price} грн")
    print(f"  Фінальна ціна: {final_price:.2f} грн")
    print(f"  Заощаджено: {original_price - final_price:.2f} грн")

    print("\n" + "=" * 70)
    print("ЯК ВИКОРИСТОВУВАТИ BLACK:")
    print("=" * 70)
    print("1. Встановити: pip install black")
    print("2. Форматувати файл: black example-2-formatting-tools.py")
    print("3. Перевірити без змін: black --check example-2-formatting-tools.py")
    print("4. Форматувати всю папку: black .")

