"""
Приклад 2: Side effects — побічні ефекти у функціях.

Запуск: pytest example_2_side_effects.py -v
"""


def add_role_bad(user):
    """❌ Змінює оригінал (side effect)."""
    user["role"] = "admin"
    return user


def add_role_good(user):
    """✅ Створює новий dict, оригінал не чіпає."""
    return {**user, "role": "admin"}


def test_bad_side_effect():
    """Функція з side effect змінює оригінал."""
    original = {"name": "Alice"}
    result = add_role_bad(original)
    assert result["role"] == "admin"
    assert original["role"] == "admin"  # оригінал теж змінився!


def test_good_no_side_effect():
    """Функція без side effect — оригінал не змінюється."""
    original = {"name": "Alice"}
    result = add_role_good(original)
    assert result["role"] == "admin"
    assert "role" not in original  # оригінал чистий ✅


def test_mutable_default_arg():
    """Mutable default argument — класична пастка."""
    def add_item_bad(item, items=[]):
        items.append(item)
        return items

    result1 = add_item_bad("a")
    result2 = add_item_bad("b")
    # result2 == ["a", "b"] — не ["b"]!
    assert result2 == ["a", "b"]


def test_mutable_default_fixed():
    """Правильний варіант — None як default."""
    def add_item_good(item, items=None):
        if items is None:
            items = []
        items.append(item)
        return items

    result1 = add_item_good("a")
    result2 = add_item_good("b")
    assert result1 == ["a"]
    assert result2 == ["b"]  # кожен виклик — свій список ✅