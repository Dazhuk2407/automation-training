"""
Вправа 5: Edge cases — граничні випадки.

Кожен тест перевіряє одну граничну умову.
Запуск: pytest exercise_5_edge_cases.py -v
"""


def test_empty_list():
    """Порожній список має довжину 0."""
    # TODO: замініть pass на: assert len([]) == 0
    pass


def test_empty_string():
    """Порожній рядок має довжину 0."""
    # TODO: замініть pass на: assert len("") == 0
    pass


def test_empty_dict():
    """Порожній словник має довжину 0."""
    # TODO: замініть pass на: assert len({}) == 0
    pass


def test_empty_is_falsy():
    """Порожній список — False у boolean контексті."""
    # TODO: замініть pass на: assert not []
    pass


def test_set_removes_duplicates():
    """Множина {1, 1, 2, 2, 3} має 3 елементи."""
    # TODO: замініть pass на: assert len({1, 1, 2, 2, 3}) == 3
    pass


def test_none_check():
    """None is None має бути True."""
    value = None
    # TODO: замініть pass на: assert value is None
    pass