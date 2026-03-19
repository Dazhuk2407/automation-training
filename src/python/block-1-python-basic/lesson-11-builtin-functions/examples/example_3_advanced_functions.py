"""
Lesson 11: Example 3 - Advanced Built-in Functions
Демонстрація sorted(), zip(), all(), any(), reversed()
"""


def demonstrate_sorted():
    """sorted() — сортування без зміни оригіналу."""
    print("=" * 50)
    print("sorted()")
    print("=" * 50)

    print(f"sorted([3,1,4,1,5]) = {sorted([3, 1, 4, 1, 5])}")
    print(f"sorted([3,1,2], reverse=True) = {sorted([3, 1, 2], reverse=True)}")

    words = ['banana', 'apple', 'cherry']
    print(f"sorted({words}, key=len) = {sorted(words, key=len)}")


def demonstrate_zip():
    """zip() — об'єднання послідовностей."""
    print("\n" + "=" * 50)
    print("zip()")
    print("=" * 50)

    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]

    for name, age in zip(names, ages):
        print(f"  {name}: {age}")

    print(f"\ndict(zip(names, ages)) = {dict(zip(names, ages))}")


def demonstrate_all_any():
    """all(), any() — перевірка умов."""
    print("\n" + "=" * 50)
    print("all(), any()")
    print("=" * 50)

    print(f"all([True, True, True]) = {all([True, True, True])}")
    print(f"all([True, False, True]) = {all([True, False, True])}")
    print(f"any([False, False, True]) = {any([False, False, True])}")
    print(f"any([False, False, False]) = {any([False, False, False])}")

    numbers = [2, 4, 6, 8]
    print(f"\nall(n % 2 == 0 for n in {numbers}) = {all(n % 2 == 0 for n in numbers)}")

    print(f"\nlist(reversed([1,2,3])) = {list(reversed([1, 2, 3]))}")


if __name__ == "__main__":
    demonstrate_sorted()
    demonstrate_zip()
    demonstrate_all_any()