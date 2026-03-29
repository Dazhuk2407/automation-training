"""Приклад 2: Кілька значень та early return. Запуск: pytest example_2_multiple.py -v"""


def min_max(numbers):
    return min(numbers), max(numbers)

def validate_email(email):
    if not email:
        return "empty"
    if "@" not in email:
        return "no_at"
    return "valid"

def test_min_max_unpacking():
    lo, hi = min_max([5, 2, 8, 1])
    assert lo == 1
    assert hi == 8

def test_min_max_as_tuple():
    assert min_max([3, 7]) == (3, 7)

def test_validate_early_returns():
    assert validate_email("") == "empty"
    assert validate_email("no-at") == "no_at"
    assert validate_email("a@b.com") == "valid"