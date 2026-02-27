"""
Lesson 10: Example 1 - Working with All Data Types
Демонстрація роботи з усіма 5 основними типами даних
"""


def demonstrate_all_types():
    """Показати всі типи даних."""
    print("=" * 70)
    print("1. STRING (str) - Текст")
    print("=" * 70)

    name = "Alice"
    greeting = 'Hello, World!'
    multiline = """This is
    a multiline
    string"""

    print(f"name = {name!r}, type = {type(name)}")
    print(f"greeting = {greeting!r}, type = {type(greeting)}")
    print(f"multiline = {multiline!r}")

    print("\n" + "=" * 70)
    print("2. INTEGER (int) - Ціле число")
    print("=" * 70)

    age = 25
    negative = -10
    big_number = 1_000_000

    print(f"age = {age}, type = {type(age)}")
    print(f"negative = {negative}, type = {type(negative)}")
    print(f"big_number = {big_number:,}, type = {type(big_number)}")

    print("\n" + "=" * 70)
    print("3. FLOAT (float) - Число з комою")
    print("=" * 70)

    price = 19.99
    temperature = -5.5
    scientific = 1.5e10

    print(f"price = {price}, type = {type(price)}")
    print(f"temperature = {temperature}, type = {type(temperature)}")
    print(f"scientific = {scientific}, type = {type(scientific)}")

    print("\n" + "=" * 70)
    print("4. BOOLEAN (bool) - Логічне значення")
    print("=" * 70)

    is_active = True
    is_empty = False
    is_valid = 1 > 0

    print(f"is_active = {is_active}, type = {type(is_active)}")
    print(f"is_empty = {is_empty}, type = {type(is_empty)}")
    print(f"is_valid = {is_valid}, type = {type(is_valid)}")

    print("\n" + "=" * 70)
    print("5. NONE (NoneType) - Відсутність значення")
    print("=" * 70)

    result = None
    data = None

    print(f"result = {result}, type = {type(result)}")
    print(f"data = {data}, type = {type(data)}")


def check_types_with_isinstance():
    """Перевірка типів за допомогою isinstance()."""
    print("\n" + "=" * 70)
    print("ПЕРЕВІРКА ТИПІВ З isinstance()")
    print("=" * 70)

    values = [
        42,
        "hello",
        3.14,
        True,
        None,
        [1, 2, 3],
        {"key": "value"}
    ]

    for value in values:
        checks = []
        if isinstance(value, int) and not isinstance(value, bool):
            checks.append("int")
        if isinstance(value, str):
            checks.append("str")
        if isinstance(value, float):
            checks.append("float")
        if isinstance(value, bool):
            checks.append("bool")
        if value is None:
            checks.append("None")
        if isinstance(value, list):
            checks.append("list")
        if isinstance(value, dict):
            checks.append("dict")

        print(f"{str(value):20s} → {', '.join(checks)}")


# === ДЕМОНСТРАЦІЯ ===


if __name__ == "__main__":
    demonstrate_all_types()
    check_types_with_isinstance()

    print("\n" + "=" * 70)
    print("💡 ПІДКАЗКИ:")
    print("=" * 70)
    print("✅ Використовуйте type() для отримання типу")
    print("✅ Використовуйте isinstance() для перевірки типу")
    print("✅ Bool є підкласом int (True=1, False=0)")
    print("✅ None - спеціальний singleton об'єкт")

