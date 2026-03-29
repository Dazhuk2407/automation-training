"""
Приклад 2: zip() та enumerate().

Запуск: pytest example_2_zip_enumerate.py -v
"""


def test_zip_basic():
    """zip об'єднує попарно."""
    names = ["Alice", "Bob"]
    roles = ["admin", "user"]
    pairs = list(zip(names, roles))
    assert pairs == [("Alice", "admin"), ("Bob", "user")]


def test_zip_to_dict():
    """Створення словника з двох списків."""
    keys = ["name", "role", "active"]
    values = ["Alice", "admin", True]
    user = dict(zip(keys, values))
    assert user == {"name": "Alice", "role": "admin", "active": True}


def test_zip_shortest():
    """zip зупиняється на найкоротшій колекції."""
    a = [1, 2, 3, 4]
    b = ["x", "y"]
    result = list(zip(a, b))
    assert result == [(1, "x"), (2, "y")]


def test_enumerate_basic():
    """enumerate повертає (індекс, елемент)."""
    items = ["a", "b", "c"]
    result = list(enumerate(items))
    assert result == [(0, "a"), (1, "b"), (2, "c")]


def test_enumerate_start():
    """enumerate з початковим індексом."""
    items = ["first", "second", "third"]
    result = list(enumerate(items, start=1))
    assert result == [(1, "first"), (2, "second"), (3, "third")]