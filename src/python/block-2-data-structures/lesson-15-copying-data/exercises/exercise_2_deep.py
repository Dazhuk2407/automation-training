"""
Вправа 2: Deep copy для вкладених структур.
Запуск: pytest exercise_2_deep.py -v
"""

import copy


def test_shallow_fails_nested():
    """Shallow copy НЕ копіює вкладений list."""
    original = {"name": "Alice", "scores": [90, 85]}
    # TODO: замініть pass на:
    #   shallow = original.copy()
    #   shallow["scores"].append(95)
    #   assert original["scores"] == [90, 85, 95]  # зіпсований!
    pass


def test_deep_copy_safe():
    """Deep copy — вкладені об'єкти незалежні."""
    original = {"name": "Alice", "scores": [90, 85]}
    # TODO: замініть pass на:
    #   deep = copy.deepcopy(original)
    #   deep["scores"].append(95)
    #   assert original["scores"] == [90, 85]
    pass


def test_nested_dict_deep():
    """Deep copy для dict з вкладеними dict."""
    config = {"db": {"host": "localhost", "port": 5432}}
    # TODO: замініть pass на:
    #   safe = copy.deepcopy(config)
    #   safe["db"]["port"] = 3306
    #   assert config["db"]["port"] == 5432
    pass