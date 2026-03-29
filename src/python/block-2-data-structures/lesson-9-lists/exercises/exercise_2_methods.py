"""
Вправа 2: Методи списків.
Запуск: pytest exercise_2_methods.py -v
"""


def test_append():
    """Додати 500 до списку."""
    codes = [200, 404]
    # TODO: замініть pass на:
    #   codes.append(500)
    #   assert codes == [200, 404, 500]
    pass


def test_extend():
    """Додати кілька елементів."""
    codes = [200]
    # TODO: замініть pass на:
    #   codes.extend([502, 503])
    #   assert codes == [200, 502, 503]
    pass


def test_remove():
    """Видалити елемент за значенням."""
    users = ["Alice", "Bob", "Charlie"]
    # TODO: замініть pass на:
    #   users.remove("Bob")
    #   assert users == ["Alice", "Charlie"]
    pass


def test_pop_last():
    """pop() повертає та видаляє останній елемент."""
    items = [1, 2, 3]
    # TODO: замініть pass на:
    #   last = items.pop()
    #   assert last == 3
    #   assert items == [1, 2]
    pass


def test_sort_ascending():
    """sorted() повертає відсортований список."""
    # TODO: замініть pass на: assert sorted([3, 1, 2]) == [1, 2, 3]
    pass


def test_sort_descending():
    """sorted() з reverse=True."""
    # TODO: замініть pass на: assert sorted([3, 1, 2], reverse=True) == [3, 2, 1]
    pass