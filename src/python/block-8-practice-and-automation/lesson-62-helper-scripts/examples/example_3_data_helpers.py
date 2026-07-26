"""Приклад 3: data helpers. Запуск: pytest example_3_data_helpers.py -v"""


def safe_get(d, *keys, default=None):
    cur = d
    for key in keys:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur

def pick(d, keys):
    return {k: d[k] for k in keys if k in d}

def invert(d):
    return {v: k for k, v in d.items()}

def test_safe_get_deep():
    data = {"user": {"profile": {"name": "Alice"}}}
    assert safe_get(data, "user", "profile", "name") == "Alice"

def test_safe_get_missing():
    data = {"user": {"profile": {"name": "Alice"}}}
    assert safe_get(data, "user", "email") is None
    assert safe_get(data, "user", "email", default="n/a") == "n/a"

def test_pick():
    data = {"a": 1, "b": 2, "c": 3}
    assert pick(data, ["a", "c"]) == {"a": 1, "c": 3}
    assert pick(data, ["x"]) == {}

def test_invert():
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
