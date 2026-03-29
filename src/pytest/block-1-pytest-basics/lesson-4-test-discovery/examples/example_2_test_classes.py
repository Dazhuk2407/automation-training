"""
Приклад 2: Групування тестів у класи.

Запуск: pytest example_2_test_classes.py -v
Результат: pytest знайде обидва класи та всі їхні методи.

Зверніть увагу на вивід:
  TestMath::test_add
  TestMath::test_subtract
  TestStrings::test_upper
  TestStrings::test_lower
"""


class TestMath:
    """Тести для математичних операцій."""

    def test_add(self):
        assert 2 + 3 == 5

    def test_subtract(self):
        assert 10 - 4 == 6

    def test_multiply(self):
        assert 3 * 4 == 12


class TestStrings:
    """Тести для рядкових операцій."""

    def test_upper(self):
        assert "hello".upper() == "HELLO"

    def test_lower(self):
        assert "WORLD".lower() == "world"

    def test_strip(self):
        assert "  test  ".strip() == "test"