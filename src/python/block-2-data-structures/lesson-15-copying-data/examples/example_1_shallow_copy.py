"""
Приклад 1: Shallow copy — копіювання плоских структур.

Запуск: pytest example_1_shallow_copy.py -v
"""


def test_list_copy():
    """Три способи shallow copy списку."""
    original = [1, 2, 3]

    copy1 = original.copy()
    copy2 = list(original)
    copy3 = original[:]

    copy1.append(4)
    assert original == [1, 2, 3]  # не змінився


def test_dict_copy():
    """Shallow copy словника."""
    user = {"name": "Alice", "role": "admin"}
    copy = user.copy()
    copy["role"] = "user"
    assert user["role"] == "admin"  # оригінал чистий


def test_dict_spread():
    """Spread оператор — ще один спосіб копіювання dict."""
    config = {"host": "localhost", "port": 8080}
    copy = {**config, "debug": True}
    assert "debug" not in config
    assert copy["debug"] is True


def test_set_copy():
    """Shallow copy множини."""
    tags = {"smoke", "api"}
    copy = tags.copy()
    copy.add("regression")
    assert "regression" not in tags