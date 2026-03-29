"""
Вправа 4: Порівняння float через pytest.approx.

Замініть pass на assert з pytest.approx.
Запуск: pytest exercise_4_float.py -v
"""

import pytest


def test_float_sum():
    """0.1 + 0.2 має приблизно дорівнювати 0.3."""
    # TODO: замініть pass на: assert 0.1 + 0.2 == pytest.approx(0.3)
    pass


def test_division():
    """1 / 3 має приблизно дорівнювати 0.333."""
    # TODO: замініть pass на: assert 1 / 3 == pytest.approx(0.333, abs=0.001)
    pass


def test_pi():
    """22 / 7 має приблизно дорівнювати 3.14."""
    # TODO: замініть pass на: assert 22 / 7 == pytest.approx(3.14, abs=0.01)
    pass