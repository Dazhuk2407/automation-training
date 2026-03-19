"""
Lesson 11: Example 2 - Math Built-in Functions
Демонстрація sum(), min(), max(), abs(), round(), pow()
"""


def demonstrate_aggregate_functions():
    """sum(), min(), max() — агрегатні функції."""
    print("=" * 50)
    print("sum(), min(), max()")
    print("=" * 50)

    numbers = [5, 2, 9, 1, 7, 3]
    print(f"numbers = {numbers}")
    print(f"sum(numbers) = {sum(numbers)}")
    print(f"min(numbers) = {min(numbers)}")
    print(f"max(numbers) = {max(numbers)}")

    words = ['apple', 'pie', 'zoo']
    print(f"\nmin({words}, key=len) = {min(words, key=len)}")
    print(f"max({words}, key=len) = {max(words, key=len)}")


def demonstrate_math_functions():
    """abs(), round(), pow() — математичні функції."""
    print("\n" + "=" * 50)
    print("abs(), round(), pow()")
    print("=" * 50)

    print(f"abs(-10) = {abs(-10)}")
    print(f"abs(10) = {abs(10)}")

    print(f"\nround(3.14159) = {round(3.14159)}")
    print(f"round(3.14159, 2) = {round(3.14159, 2)}")

    print(f"\npow(2, 3) = {pow(2, 3)}")
    print(f"2 ** 3 = {2 ** 3}")


if __name__ == "__main__":
    demonstrate_aggregate_functions()
    demonstrate_math_functions()