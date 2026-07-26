"""Приклад 2: KeyError, IndexError, ZeroDivisionError. Запуск: pytest example_2_key_index_errors.py -v"""

import pytest


def get_field(data, key, default=None):
    """Безпечний доступ до поля API-відповіді через .get()."""
    return data.get(key, default)


def safe_index(items, i, default=None):
    """Безпечний доступ до елемента списку за індексом."""
    if 0 <= i < len(items):
        return items[i]
    return default


def success_rate(passed, total):
    """Відсоток пройдених тестів без падіння на діленні на нуль."""
    if total == 0:
        return 0.0
    return passed / total * 100


def test_key_error():
    user = {"name": "Alice"}
    with pytest.raises(KeyError):
        user["age"]


def test_get_is_safe():
    user = {"name": "Alice"}
    assert get_field(user, "age") is None
    assert get_field(user, "age", 0) == 0
    assert get_field(user, "name") == "Alice"


def test_index_error():
    nums = [10, 20, 30]
    with pytest.raises(IndexError):
        nums[5]


def test_safe_index():
    nums = [10, 20, 30]
    assert safe_index(nums, 1) == 20
    assert safe_index(nums, 5) is None
    assert safe_index(nums, 5, default=-1) == -1


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        10 / 0


def test_success_rate():
    assert success_rate(3, 4) == 75.0
    assert success_rate(0, 0) == 0.0
