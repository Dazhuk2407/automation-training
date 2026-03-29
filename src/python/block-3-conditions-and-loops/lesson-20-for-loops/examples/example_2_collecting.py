"""
Приклад 2: Збір результатів через for — фільтрація та трансформація.
Запуск: pytest example_2_collecting.py -v
"""


def test_filter_errors():
    codes = [200, 301, 404, 500, 201]
    errors = []
    for code in codes:
        if code >= 400:
            errors.append(code)
    assert errors == [404, 500]


def test_transform_names():
    names = ["alice", "bob"]
    upper = []
    for name in names:
        upper.append(name.upper())
    assert upper == ["ALICE", "BOB"]


def test_sum_values():
    prices = [10.5, 20.0, 5.5]
    total = 0
    for price in prices:
        total += price
    assert total == 36.0


def test_flatten_nested():
    nested = [[1, 2], [3, 4], [5]]
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    assert flat == [1, 2, 3, 4, 5]


def test_build_dict():
    keys = ["name", "role"]
    values = ["Alice", "admin"]
    result = {}
    for key, value in zip(keys, values):
        result[key] = value
    assert result == {"name": "Alice", "role": "admin"}