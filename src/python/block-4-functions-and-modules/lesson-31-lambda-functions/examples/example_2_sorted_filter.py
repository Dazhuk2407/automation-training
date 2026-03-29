"""Приклад 2: Lambda з sorted, filter, min/max. Запуск: pytest example_2_sorted_filter.py -v"""


USERS = [
    {"name": "Charlie", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
]


def test_sorted_by_name():
    result = sorted(USERS, key=lambda u: u["name"])
    names = [u["name"] for u in result]
    assert names == ["Alice", "Bob", "Charlie"]


def test_sorted_by_age_desc():
    result = sorted(USERS, key=lambda u: u["age"], reverse=True)
    assert result[0]["name"] == "Bob"


def test_min_by_age():
    youngest = min(USERS, key=lambda u: u["age"])
    assert youngest["name"] == "Alice"


def test_max_by_age():
    oldest = max(USERS, key=lambda u: u["age"])
    assert oldest["name"] == "Bob"


def test_filter_positive():
    numbers = [1, -2, 3, -4, 5]
    positive = list(filter(lambda n: n > 0, numbers))
    assert positive == [1, 3, 5]


def test_map_double():
    numbers = [1, 2, 3]
    doubled = list(map(lambda n: n * 2, numbers))
    assert doubled == [2, 4, 6]