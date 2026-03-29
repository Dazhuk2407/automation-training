"""
Вправа 1: break.
Запуск: pytest exercise_1_break.py -v
"""


def test_find_first_error():
    """Знайти перший код >= 400."""
    codes = [200, 200, 404, 500]
    # TODO: замініть pass на:
    #   first_error = None
    #   for code in codes:
    #       if code >= 400:
    #           first_error = code
    #           break
    #   assert first_error == 404
    pass


def test_find_user():
    """Знайти user з name == 'Bob'."""
    users = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
    # TODO: замініть pass на:
    #   found = None
    #   for user in users:
    #       if user["name"] == "Bob":
    #           found = user
    #           break
    #   assert found == {"name": "Bob"}
    pass


def test_stop_at_limit():
    """Додавати числа поки сума <= 100."""
    numbers = [30, 25, 40, 50, 10]
    # TODO: замініть pass на:
    #   total = 0
    #   count = 0
    #   for n in numbers:
    #       if total + n > 100:
    #           break
    #       total += n
    #       count += 1
    #   assert total == 95
    #   assert count == 3
    pass