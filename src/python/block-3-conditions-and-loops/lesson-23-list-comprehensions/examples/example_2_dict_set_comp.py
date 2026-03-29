"""
Приклад 2: Dict та set comprehensions.
Запуск: pytest example_2_dict_set_comp.py -v
"""


def test_dict_from_zip():
    keys = ["name", "role", "active"]
    values = ["Alice", "admin", True]
    user = {k: v for k, v in zip(keys, values)}
    assert user == {"name": "Alice", "role": "admin", "active": True}


def test_invert_dict():
    original = {"a": 1, "b": 2, "c": 3}
    inverted = {v: k for k, v in original.items()}
    assert inverted == {1: "a", 2: "b", 3: "c"}


def test_filter_dict():
    config = {"host": "localhost", "port": 8080, "debug": False, "verbose": False}
    truthy = {k: v for k, v in config.items() if v}
    assert "host" in truthy
    assert "debug" not in truthy


def test_set_comprehension():
    emails = ["alice@gmail.com", "bob@yahoo.com", "charlie@gmail.com"]
    domains = {e.split("@")[1] for e in emails}
    assert domains == {"gmail.com", "yahoo.com"}


def test_set_unique_roles():
    users = [{"role": "admin"}, {"role": "user"}, {"role": "user"}]
    roles = {u["role"] for u in users}
    assert roles == {"admin", "user"}