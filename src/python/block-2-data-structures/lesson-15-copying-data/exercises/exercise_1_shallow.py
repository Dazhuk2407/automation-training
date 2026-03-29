"""
Вправа 1: Shallow copy.
Запуск: pytest exercise_1_shallow.py -v
"""


def test_list_copy():
    """Shallow copy списку — оригінал не змінюється."""
    original = [1, 2, 3]
    # TODO: замініть pass на:
    #   copy = original.copy()
    #   copy.append(4)
    #   assert original == [1, 2, 3]
    #   assert copy == [1, 2, 3, 4]
    pass


def test_dict_copy():
    """Shallow copy словника — оригінал не змінюється."""
    user = {"name": "Alice", "role": "admin"}
    # TODO: замініть pass на:
    #   copy = user.copy()
    #   copy["role"] = "user"
    #   assert user["role"] == "admin"
    pass


def test_spread_copy():
    """Spread створює копію з додатковим ключем."""
    config = {"host": "localhost", "port": 8080}
    # TODO: замініть pass на:
    #   copy = {**config, "debug": True}
    #   assert "debug" not in config
    #   assert copy["debug"] is True
    pass