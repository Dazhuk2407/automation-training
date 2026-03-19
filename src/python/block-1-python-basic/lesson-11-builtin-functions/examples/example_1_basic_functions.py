"""
Lesson 11: Example 1 - Basic Built-in Functions
Демонстрація len(), type(), isinstance(), range(), enumerate()
"""


def demonstrate_info_functions():
    """len(), type(), isinstance() — інформація про об'єкти."""
    print("=" * 50)
    print("len(), type(), isinstance()")
    print("=" * 50)

    print(f"len([1,2,3]) = {len([1, 2, 3])}")
    print(f"len('hello') = {len('hello')}")

    print(f"\ntype(42) = {type(42)}")
    print(f"type('hello') = {type('hello')}")
    print(f"type([1,2]) = {type([1, 2])}")

    print(f"\nisinstance(42, int) = {isinstance(42, int)}")
    print(f"isinstance('hello', str) = {isinstance('hello', str)}")
    print(f"isinstance(42, (int, float)) = {isinstance(42, (int, float))}")


def demonstrate_sequences():
    """range(), enumerate() — робота з послідовностями."""
    print("\n" + "=" * 50)
    print("range(), enumerate()")
    print("=" * 50)

    print(f"list(range(5)) = {list(range(5))}")
    print(f"list(range(2, 7)) = {list(range(2, 7))}")
    print(f"list(range(0, 10, 2)) = {list(range(0, 10, 2))}")

    print("\nenumerate():")
    for i, val in enumerate(['a', 'b', 'c'], start=1):
        print(f"  {i}: {val}")


if __name__ == "__main__":
    demonstrate_info_functions()
    demonstrate_sequences()