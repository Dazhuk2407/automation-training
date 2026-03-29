"""
Вправа 3: Безпечні тестові дані через фабрику.
Запуск: pytest exercise_3_test_data.py -v
"""

import copy


BASE = {"name": "Alice", "roles": ["user"], "settings": {"theme": "light"}}


def make_user():
    """Фабрика — deepcopy кожен раз."""
    return copy.deepcopy(BASE)


def test_factory_returns_fresh():
    """Фабрика повертає свіжу копію."""
    # TODO: замініть pass на:
    #   user = make_user()
    #   assert user == BASE
    #   assert user is not BASE
    pass


def test_modify_copy_not_original():
    """Зміна копії не впливає на оригінал."""
    # TODO: замініть pass на:
    #   user = make_user()
    #   user["roles"].append("admin")
    #   assert "admin" not in BASE["roles"]
    pass


def test_two_copies_independent():
    """Дві копії незалежні одна від одної."""
    # TODO: замініть pass на:
    #   u1 = make_user()
    #   u2 = make_user()
    #   u1["name"] = "Bob"
    #   assert u2["name"] == "Alice"
    pass