"""
Приклад 3: Правильний спосіб тестувати винятки — pytest.raises.

Запуск: pytest example_3_pytest_raises.py -v
Результат: 3 passed.

Порівняйте з example_2: там помилки — це ERROR (код зламався).
Тут — це PASSED (ми очікували помилку і перевірили її).
"""

import pytest


def test_zero_division_expected():
    """Очікуємо ZeroDivisionError — тест пройде."""
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0


def test_key_error_expected():
    """Очікуємо KeyError — тест пройде."""
    with pytest.raises(KeyError):
        user = {"name": "Alice"}
        _ = user["email"]


def test_type_error_expected():
    """Очікуємо TypeError — тест пройде."""
    with pytest.raises(TypeError):
        result = "hello" + 5