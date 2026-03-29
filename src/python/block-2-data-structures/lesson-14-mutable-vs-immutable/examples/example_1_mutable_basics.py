"""
Приклад 1: Mutable vs Immutable — базова різниця.

Запуск: pytest example_1_mutable_basics.py -v
"""


def test_immutable_int():
    """int — immutable: 'зміна' створює новий об'єкт."""
    x = 10
    y = x
    x = 20
    assert y == 10  # y не змінився


def test_immutable_string():
    """str — immutable: методи повертають новий рядок."""
    name = "alice"
    upper = name.upper()
    assert name == "alice"    # оригінал не змінився
    assert upper == "ALICE"   # новий рядок


def test_mutable_list():
    """list — mutable: зміна через посилання."""
    items = [1, 2, 3]
    other = items         # other і items — ТОЙ САМИЙ об'єкт
    items.append(4)
    assert other == [1, 2, 3, 4]  # other теж змінився!


def test_mutable_dict():
    """dict — mutable: зміна через посилання."""
    user = {"name": "Alice"}
    ref = user
    user["role"] = "admin"
    assert ref["role"] == "admin"  # ref теж змінився


def test_immutable_tuple():
    """tuple — immutable: не можна змінити."""
    point = (10, 20)
    # point[0] = 30  # TypeError
    assert point == (10, 20)


def test_list_copy_independent():
    """Копія списку — незалежна."""
    original = [1, 2, 3]
    copy = original.copy()
    copy.append(4)
    assert original == [1, 2, 3]  # оригінал не змінився
    assert copy == [1, 2, 3, 4]