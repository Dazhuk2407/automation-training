"""
Приклад 1: range() — генерація послідовностей.

Запуск: pytest example_1_range.py -v
"""


def test_range_basic():
    """range(n) — від 0 до n-1."""
    assert list(range(5)) == [0, 1, 2, 3, 4]


def test_range_start_stop():
    """range(start, stop) — від start до stop-1."""
    assert list(range(1, 6)) == [1, 2, 3, 4, 5]


def test_range_step():
    """range з кроком."""
    assert list(range(0, 10, 2)) == [0, 2, 4, 6, 8]
    assert list(range(0, 10, 3)) == [0, 3, 6, 9]


def test_range_reverse():
    """Зворотна послідовність."""
    assert list(range(5, 0, -1)) == [5, 4, 3, 2, 1]


def test_range_is_not_list():
    """range() повертає ітератор, не список."""
    r = range(5)
    assert isinstance(r, range)
    assert 3 in r  # але in працює