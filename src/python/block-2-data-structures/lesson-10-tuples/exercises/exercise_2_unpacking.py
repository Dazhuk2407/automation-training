"""
Вправа 2: Unpacking tuples.
Запуск: pytest exercise_2_unpacking.py -v
"""


def test_basic_unpacking():
    """Розпакувати (10, 20) у x, y."""
    point = (10, 20)
    # TODO: замініть pass на:
    #   x, y = point
    #   assert x == 10
    #   assert y == 20
    pass


def test_three_values():
    """Розпакувати ("Alice", "admin", True)."""
    user_data = ("Alice", "admin", True)
    # TODO: замініть pass на:
    #   name, role, active = user_data
    #   assert name == "Alice"
    #   assert role == "admin"
    #   assert active is True
    pass


def test_ignore_value():
    """Розпакувати (200, "OK") ігноруючи message."""
    response = (200, "OK")
    # TODO: замініть pass на:
    #   code, _ = response
    #   assert code == 200
    pass


def test_star_unpacking():
    """first, *rest = (1, 2, 3, 4)."""
    numbers = (1, 2, 3, 4)
    # TODO: замініть pass на:
    #   first, *rest = numbers
    #   assert first == 1
    #   assert rest == [2, 3, 4]
    pass


def test_swap():
    """Обміняти a, b через tuple unpacking."""
    a, b = 1, 2
    # TODO: замініть pass на:
    #   a, b = b, a
    #   assert a == 2
    #   assert b == 1
    pass