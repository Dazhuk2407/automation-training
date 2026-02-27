"""
Lesson 4: Example 2 - Test Classes
Організація тестів в класи
"""


class TestMathOperations:
    """Група тестів для математичних операцій."""

    def test_addition(self):
        """Тест додавання."""
        assert 2 + 3 == 5

    def test_subtraction(self):
        """Тест віднімання."""
        assert 10 - 4 == 6

    def test_multiplication(self):
        """Тест множення."""
        assert 3 * 4 == 12

    def test_division(self):
        """Тест ділення."""
        assert 10 / 2 == 5


class TestStringOperations:
    """Група тестів для роботи з рядками."""

    def test_uppercase(self):
        """Тест uppercase."""
        assert "hello".upper() == "HELLO"

    def test_lowercase(self):
        """Тест lowercase."""
        assert "WORLD".lower() == "world"

    def test_capitalize(self):
        """Тест capitalize."""
        assert "python".capitalize() == "Python"

    def test_strip(self):
        """Тест видалення пробілів."""
        assert "  test  ".strip() == "test"


class TestListOperations:
    """Група тестів для операцій зі списками."""

    def test_append(self):
        """Тест додавання елементу."""
        lst = [1, 2, 3]
        lst.append(4)
        assert lst == [1, 2, 3, 4]

    def test_extend(self):
        """Тест розширення списку."""
        lst = [1, 2]
        lst.extend([3, 4])
        assert lst == [1, 2, 3, 4]

    def test_remove(self):
        """Тест видалення елементу."""
        lst = [1, 2, 3, 2]
        lst.remove(2)
        assert lst == [1, 3, 2]


# Запустіть: pytest -v
# pytest знайде всі 3 класи та 11 тестів

