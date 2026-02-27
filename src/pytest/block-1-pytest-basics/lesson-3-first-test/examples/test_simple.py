"""
Lesson 3: Example 1 - First Simple Test
"""

def test_simple_math():
    """Тест простої математики."""
    assert 2 + 2 == 4
    assert 10 - 5 == 5
    assert 3 * 4 == 12
    assert 8 / 2 == 4


def test_string_operations():
    """Тест операцій з рядками."""
    name = "pytest"
    assert name.upper() == "PYTEST"
    assert name.lower() == "pytest"
    assert len(name) == 6


def test_list_operations():
    """Тест операцій зі списками."""
    numbers = [1, 2, 3]
    assert len(numbers) == 3
    assert numbers[0] == 1
    assert 2 in numbers


if __name__ == "__main__":
    # Можна запустити як звичайний Python файл для перевірки
    test_simple_math()
    test_string_operations()
    test_list_operations()
    print("✅ All tests passed!")

