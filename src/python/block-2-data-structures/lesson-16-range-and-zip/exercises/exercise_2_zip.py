"""
Вправа 2: zip() та enumerate().
Запуск: pytest exercise_2_zip.py -v
"""


def test_zip_pairs():
    """zip двох списків → list of tuples."""
    names = ["Alice", "Bob"]
    roles = ["admin", "user"]
    # TODO: замініть pass на:
    #   pairs = list(zip(names, roles))
    #   assert pairs == [("Alice", "admin"), ("Bob", "user")]
    pass


def test_zip_to_dict():
    """dict(zip(keys, values)) → словник."""
    keys = ["name", "age"]
    values = ["Alice", 25]
    # TODO: замініть pass на:
    #   result = dict(zip(keys, values))
    #   assert result == {"name": "Alice", "age": 25}
    pass


def test_enumerate_indices():
    """enumerate повертає (індекс, елемент)."""
    items = ["a", "b", "c"]
    # TODO: замініть pass на:
    #   result = list(enumerate(items))
    #   assert result == [(0, "a"), (1, "b"), (2, "c")]
    pass


def test_enumerate_start():
    """enumerate з start=1."""
    items = ["first", "second"]
    # TODO: замініть pass на:
    #   result = list(enumerate(items, start=1))
    #   assert result == [(1, "first"), (2, "second")]
    pass