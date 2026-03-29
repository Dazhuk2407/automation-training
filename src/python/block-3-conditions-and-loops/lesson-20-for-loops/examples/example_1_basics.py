"""
Приклад 1: Базові for loops.
Запуск: pytest example_1_basics.py -v
"""


def test_iterate_list():
    result = []
    for code in [200, 301, 404]:
        result.append(code)
    assert result == [200, 301, 404]


def test_iterate_string():
    chars = []
    for c in "abc":
        chars.append(c)
    assert chars == ["a", "b", "c"]


def test_iterate_dict_keys():
    config = {"host": "localhost", "port": 8080}
    keys = []
    for key in config:
        keys.append(key)
    assert "host" in keys
    assert "port" in keys


def test_iterate_dict_items():
    user = {"name": "Alice", "role": "admin"}
    pairs = []
    for key, value in user.items():
        pairs.append((key, value))
    assert ("name", "Alice") in pairs


def test_enumerate():
    items = ["a", "b", "c"]
    result = []
    for i, item in enumerate(items):
        result.append((i, item))
    assert result == [(0, "a"), (1, "b"), (2, "c")]


def test_range_loop():
    squares = []
    for i in range(1, 6):
        squares.append(i ** 2)
    assert squares == [1, 4, 9, 16, 25]