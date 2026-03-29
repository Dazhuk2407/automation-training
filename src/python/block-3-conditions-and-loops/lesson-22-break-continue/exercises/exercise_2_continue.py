"""
Вправа 2: continue.
Запуск: pytest exercise_2_continue.py -v
"""


def test_skip_none():
    """Пропустити None значення."""
    data = [1, None, 2, None, 3]
    # TODO: замініть pass на:
    #   clean = []
    #   for item in data:
    #       if item is None:
    #           continue
    #       clean.append(item)
    #   assert clean == [1, 2, 3]
    pass


def test_only_positive():
    """Зібрати тільки позитивні числа."""
    numbers = [-3, 5, -1, 8, 0, 12]
    # TODO: замініть pass на:
    #   positive = []
    #   for n in numbers:
    #       if n <= 0:
    #           continue
    #       positive.append(n)
    #   assert positive == [5, 8, 12]
    pass


def test_valid_emails():
    """Зібрати тільки валідні email."""
    emails = ["alice@t.com", "", "bob@t.com", "invalid", "charlie@t.com"]
    # TODO: замініть pass на:
    #   valid = []
    #   for email in emails:
    #       if not email or "@" not in email:
    #           continue
    #       valid.append(email)
    #   assert valid == ["alice@t.com", "bob@t.com", "charlie@t.com"]
    pass