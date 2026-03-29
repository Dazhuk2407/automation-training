"""
Приклад 2: Deep copy — копіювання вкладених структур.

Запуск: pytest example_2_deep_copy.py -v
"""

import copy


def test_shallow_copy_problem():
    """Shallow copy не копіює вкладені об'єкти."""
    original = {"name": "Alice", "scores": [90, 85]}
    shallow = original.copy()

    shallow["scores"].append(95)
    # Вкладений list спільний!
    assert original["scores"] == [90, 85, 95]  # зіпсований


def test_deep_copy_safe():
    """Deep copy копіює все рекурсивно."""
    original = {"name": "Alice", "scores": [90, 85]}
    deep = copy.deepcopy(original)

    deep["scores"].append(95)
    assert original["scores"] == [90, 85]  # чистий ✅
    assert deep["scores"] == [90, 85, 95]


def test_nested_list_of_dicts():
    """Deep copy для списку словників."""
    users = [
        {"name": "Alice", "tags": ["admin"]},
        {"name": "Bob", "tags": ["user"]},
    ]
    users_copy = copy.deepcopy(users)

    users_copy[0]["tags"].append("superuser")
    assert users[0]["tags"] == ["admin"]  # оригінал чистий ✅


def test_shallow_vs_deep_flat():
    """Для плоских структур shallow і deep дають однаковий результат."""
    flat = {"a": 1, "b": 2, "c": 3}
    shallow = flat.copy()
    deep = copy.deepcopy(flat)

    shallow["d"] = 4
    deep["e"] = 5
    assert "d" not in flat
    assert "e" not in flat