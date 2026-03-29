"""
Вправа 2: Виправити side effects.
Запуск: pytest exercise_2_side_effects.py -v
"""


def test_no_side_effect_dict():
    """Створити новий dict замість мутації оригіналу."""
    user = {"name": "Alice", "role": "user"}
    # TODO: замініть pass на:
    #   admin = {**user, "role": "admin"}
    #   assert admin["role"] == "admin"
    #   assert user["role"] == "user"
    pass


def test_no_side_effect_list():
    """Створити новий list замість мутації оригіналу."""
    items = [1, 2, 3]
    # TODO: замініть pass на:
    #   extended = [*items, 4, 5]
    #   assert extended == [1, 2, 3, 4, 5]
    #   assert items == [1, 2, 3]
    pass


def test_fix_default_arg():
    """Функція з правильним default argument."""
    def collect(item, items=None):
        if items is None:
            items = []
        items.append(item)
        return items

    # TODO: замініть pass на:
    #   result1 = collect("a")
    #   result2 = collect("b")
    #   assert result1 == ["a"]
    #   assert result2 == ["b"]
    pass