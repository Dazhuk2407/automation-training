"""
Вправа 1: Тернарний оператор.
Запуск: pytest exercise_1_ternary.py -v
"""


def test_status_label():
    """'ok' для 200, 'error' для іншого."""
    status = 200
    # TODO: замініть pass на:
    #   label = "ok" if status == 200 else "error"
    #   assert label == "ok"
    pass


def test_adult_or_minor():
    """'adult' якщо >= 18, інакше 'minor'."""
    age = 20
    # TODO: замініть pass на:
    #   category = "adult" if age >= 18 else "minor"
    #   assert category == "adult"
    pass


def test_plural():
    """'test' для 1, 'tests' для інших."""
    count = 5
    # TODO: замініть pass на:
    #   word = "test" if count == 1 else "tests"
    #   assert word == "tests"
    pass


def test_sign():
    """Визначити знак числа."""
    n = -3
    # TODO: замініть pass на:
    #   sign = "positive" if n > 0 else ("zero" if n == 0 else "negative")
    #   assert sign == "negative"
    pass