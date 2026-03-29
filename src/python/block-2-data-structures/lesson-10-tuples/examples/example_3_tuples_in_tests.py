"""
Приклад 3: Tuples у pytest — parametrize та тестові дані.

Запуск: pytest example_3_tuples_in_tests.py -v
"""

import pytest


def calculate_discount(price, percent):
    """Розрахувати ціну зі знижкою."""
    return price * (1 - percent / 100)


# --- parametrize з tuples ---

@pytest.mark.parametrize("price, percent, expected", [
    (100, 10, 90.0),
    (200, 25, 150.0),
    (50, 0, 50.0),
    (100, 100, 0.0),
])
def test_discount(price, percent, expected):
    """Тест знижки з різними параметрами."""
    result = calculate_discount(price, percent)
    assert result == expected


# --- Tuple як immutable test data ---

VALID_STATUS_CODES = (200, 201, 204)
ERROR_STATUS_CODES = (400, 401, 403, 404, 500)


def test_success_codes():
    """Перевірка що 200 — успішний код."""
    assert 200 in VALID_STATUS_CODES


def test_error_codes():
    """Перевірка що 404 — код помилки."""
    assert 404 in ERROR_STATUS_CODES


def test_codes_are_immutable():
    """Тестові дані не можна випадково змінити."""
    with pytest.raises(TypeError):
        VALID_STATUS_CODES[0] = 999