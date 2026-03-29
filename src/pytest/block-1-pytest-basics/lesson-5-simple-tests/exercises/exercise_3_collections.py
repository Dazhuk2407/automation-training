"""
Вправа 3: Тести для колекцій (списки та словники).

Замініть pass на assert у кожному тесті.
Запуск: pytest exercise_3_collections.py -v
"""


# --- Списки ---

def test_list_length():
    """Довжина списку [1, 2, 3, 4, 5] має бути 5."""
    numbers = [1, 2, 3, 4, 5]
    # TODO: замініть pass на: assert len(numbers) == 5
    pass


def test_list_first_last():
    """Перший елемент == 1, останній == 5."""
    numbers = [1, 2, 3, 4, 5]
    # TODO: замініть pass на:
    #   assert numbers[0] == 1
    #   assert numbers[-1] == 5
    pass


def test_list_membership():
    """'apple' є в списку фруктів."""
    fruits = ["apple", "banana", "cherry"]
    # TODO: замініть pass на: assert "apple" in fruits
    pass


def test_list_sorted():
    """sorted([3, 1, 2]) має повернути [1, 2, 3]."""
    # TODO: замініть pass на: assert sorted([3, 1, 2]) == [1, 2, 3]
    pass


# --- Словники ---

def test_dict_access():
    """user['name'] має бути 'Alice'."""
    user = {"name": "Alice", "age": 25}
    # TODO: замініть pass на: assert user["name"] == "Alice"
    pass


def test_dict_key_exists():
    """'name' є ключем словника."""
    user = {"name": "Alice", "age": 25}
    # TODO: замініть pass на: assert "name" in user
    pass


def test_dict_key_missing():
    """'phone' НЕ є ключем словника."""
    user = {"name": "Alice", "age": 25}
    # TODO: замініть pass на: assert "phone" not in user
    pass


def test_dict_get_default():
    """user.get('phone') має повернути None."""
    user = {"name": "Alice", "age": 25}
    # TODO: замініть pass на: assert user.get("phone") is None
    pass