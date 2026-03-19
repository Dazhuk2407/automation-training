"""
Lesson 10: Example 2 - Type Conversion
"""


def demonstrate_string_conversion():
    """str() - конвертація в рядок."""
    print("=== str() conversion ===")
    print(f"str(42) = {str(42)!r}")
    print(f"str(3.14) = {str(3.14)!r}")
    print(f"str(True) = {str(True)!r}")
    print(f"str(None) = {str(None)!r}")


def demonstrate_int_conversion():
    """int() - конвертація в ціле число."""
    print("\n=== int() conversion ===")
    print(f"int('42') = {int('42')}")
    print(f"int(3.99) = {int(3.99)}")
    print(f"int(True) = {int(True)}")
    print(f"int(False) = {int(False)}")

    # Помилки конверсії
    for value in ["hello", "3.14", None]:
        try:
            result = int(value)
            print(f"int({value!r}) = {result}")
        except (ValueError, TypeError) as e:
            print(f"int({value!r}) -> ERROR: {e}")


def demonstrate_float_conversion():
    """float() - конвертація в число з комою."""
    print("\n=== float() conversion ===")
    print(f"float('3.14') = {float('3.14')}")
    print(f"float(42) = {float(42)}")
    print(f"float(True) = {float(True)}")


def demonstrate_bool_conversion():
    """bool() - конвертація в логічне значення."""
    print("\n=== bool() conversion ===")
    print("Falsy values:")
    for value in [0, 0.0, "", [], {}, None]:
        print(f"  bool({value!r}) = {bool(value)}")

    print("Truthy values:")
    for value in [1, -1, 3.14, "hello", [1, 2], {"a": 1}]:
        print(f"  bool({value!r}) = {bool(value)}")


def safe_int(value, default=0):
    """Безпечна конверсія в int."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


if __name__ == "__main__":
    demonstrate_string_conversion()
    demonstrate_int_conversion()
    demonstrate_float_conversion()
    demonstrate_bool_conversion()

    print("\n=== safe_int() ===")
    print(f"safe_int('42') = {safe_int('42')}")
    print(f"safe_int('hello') = {safe_int('hello')}")
    print(f"safe_int(None) = {safe_int(None)}")