"""
Вправа 1: Визначити mutable/immutable поведінку.
Запуск: pytest exercise_1_identify.py -v
"""

import pytest


def test_list_is_mutable():
    """append змінює оригінальний список."""
    items = [1, 2, 3]
    # TODO: замініть pass на:
    #   items.append(4)
    #   assert items == [1, 2, 3, 4]
    pass


def test_string_is_immutable():
    """upper() не змінює оригінал, а повертає новий рядок."""
    name = "alice"
    # TODO: замініть pass на:
    #   upper = name.upper()
    #   assert name == "alice"
    #   assert upper == "ALICE"
    pass


def test_reference_vs_copy():
    """other = items — це посилання, не копія."""
    items = [1, 2, 3]
    other = items
    # TODO: замініть pass на:
    #   items.append(4)
    #   assert other == [1, 2, 3, 4]
    pass


def test_copy_is_independent():
    """.copy() створює незалежний список."""
    original = [1, 2, 3]
    # TODO: замініть pass на:
    #   copy = original.copy()
    #   copy.append(4)
    #   assert original == [1, 2, 3]
    #   assert copy == [1, 2, 3, 4]
    pass


def test_tuple_is_immutable():
    """Спроба змінити tuple кидає TypeError."""
    point = (10, 20)
    # TODO: замініть pass на:
    #   with pytest.raises(TypeError):
    #       point[0] = 30
    pass