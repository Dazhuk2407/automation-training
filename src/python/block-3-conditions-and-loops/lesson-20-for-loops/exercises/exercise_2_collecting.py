"""
Вправа 2: Фільтрація та трансформація через for.
Запуск: pytest exercise_2_collecting.py -v
"""


def test_filter_positive():
    """Залишити тільки позитивні числа."""
    numbers = [-3, 5, -1, 8, 0, 12]
    # TODO: замініть pass на:
    #   positive = []
    #   for n in numbers:
    #       if n > 0:
    #           positive.append(n)
    #   assert positive == [5, 8, 12]
    pass


def test_uppercase_names():
    """Перетворити всі імена в upper case."""
    names = ["alice", "bob", "charlie"]
    # TODO: замініть pass на:
    #   upper = []
    #   for name in names:
    #       upper.append(name.upper())
    #   assert upper == ["ALICE", "BOB", "CHARLIE"]
    pass


def test_extract_ids():
    """Дістати id з кожного словника."""
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    # TODO: замініть pass на:
    #   ids = []
    #   for user in users:
    #       ids.append(user["id"])
    #   assert ids == [1, 2]
    pass