"""
Вправа 1: Основи tuples.
Запуск: pytest exercise_1_basics.py -v
"""

import pytest


def test_create_tuple():
    """(10, 20, 30) має довжину 3."""
    point = (10, 20, 30)
    # TODO: замініть pass на: assert len(point) == 3
    pass


def test_single_element():
    """(42,) — tuple, а (42) — int."""
    real_tuple = (42,)
    not_tuple = (42)
    # TODO: замініть pass на:
    #   assert isinstance(real_tuple, tuple)
    #   assert isinstance(not_tuple, int)
    pass


def test_first_element():
    """Перший елемент (200, 'OK') == 200."""
    status = (200, "OK")
    # TODO: замініть pass на: assert status[0] == 200
    pass


def test_last_element():
    """Останній елемент через [-1]."""
    codes = (200, 301, 404, 500)
    # TODO: замініть pass на: assert codes[-1] == 500
    pass


def test_membership():
    """404 є в tuple кодів."""
    codes = (200, 301, 404, 500)
    # TODO: замініть pass на: assert 404 in codes
    pass


def test_immutable():
    """Спроба змінити tuple кидає TypeError."""
    point = (10, 20)
    # TODO: замініть pass на:
    #   with pytest.raises(TypeError):
    #       point[0] = 30
    pass