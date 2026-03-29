"""
Приклад 1: List comprehensions — базові та з фільтрацією.
Запуск: pytest example_1_list_comp.py -v
"""


def test_basic_comprehension():
    squares = [n ** 2 for n in range(1, 6)]
    assert squares == [1, 4, 9, 16, 25]


def test_with_filter():
    codes = [200, 301, 404, 500, 201]
    errors = [c for c in codes if c >= 400]
    assert errors == [404, 500]


def test_transform_strings():
    names = ["alice", "bob", "charlie"]
    upper = [name.upper() for name in names]
    assert upper == ["ALICE", "BOB", "CHARLIE"]


def test_filter_and_transform():
    """Фільтр + трансформація."""
    users = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False},
        {"name": "Charlie", "active": True},
    ]
    active_names = [u["name"] for u in users if u["active"]]
    assert active_names == ["Alice", "Charlie"]


def test_ternary_in_comprehension():
    """if/else для трансформації (тернарний)."""
    codes = [200, 404, 500]
    labels = ["OK" if c < 400 else "ERROR" for c in codes]
    assert labels == ["OK", "ERROR", "ERROR"]


def test_flatten():
    """Вкладений comprehension для flatten."""
    nested = [[1, 2], [3, 4], [5]]
    flat = [item for sublist in nested for item in sublist]
    assert flat == [1, 2, 3, 4, 5]