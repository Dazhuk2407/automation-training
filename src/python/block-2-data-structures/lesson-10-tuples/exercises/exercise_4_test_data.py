"""
Вправа 4: Tuples як тестові дані.
Запуск: pytest exercise_4_test_data.py -v
"""

import pytest


VALID_CODES = (200, 201, 204)
ERROR_CODES = (400, 401, 403, 404, 500, 502, 503)


def double(n):
    """Подвоїти число."""
    return n * 2


def test_valid_codes():
    """200 є в VALID_CODES."""
    # TODO: замініть pass на: assert 200 in VALID_CODES
    pass


def test_error_codes():
    """500 є в ERROR_CODES."""
    # TODO: замініть pass на: assert 500 in ERROR_CODES
    pass


def test_code_not_in_errors():
    """200 НЕ є в ERROR_CODES."""
    # TODO: замініть pass на: assert 200 not in ERROR_CODES
    pass


@pytest.mark.parametrize("input_val, expected", [
    (1, 2),
    (5, 10),
    (0, 0),
    (-3, -6),
])
def test_double(input_val, expected):
    """Parametrize тест для функції double."""
    # TODO: замініть pass на: assert double(input_val) == expected
    pass