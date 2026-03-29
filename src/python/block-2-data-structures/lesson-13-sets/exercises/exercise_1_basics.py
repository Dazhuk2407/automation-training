"""
Вправа 1: Основи множин.
Запуск: pytest exercise_1_basics.py -v
"""


def test_unique_elements():
    """{1, 2, 2, 3, 3} має тільки 3 унікальні елементи."""
    numbers = {1, 2, 2, 3, 3}
    # TODO: замініть pass на: assert len(numbers) == 3
    pass


def test_add_element():
    """Додати 'critical' до множини тегів."""
    tags = {"smoke", "api"}
    # TODO: замініть pass на:
    #   tags.add("critical")
    #   assert "critical" in tags
    pass


def test_discard_safe():
    """discard неіснуючого елемента — без помилки."""
    tags = {"smoke", "api"}
    # TODO: замініть pass на:
    #   tags.discard("nonexistent")
    #   assert len(tags) == 2
    pass


def test_membership():
    """200 є в множині кодів."""
    codes = {200, 301, 404}
    # TODO: замініть pass на: assert 200 in codes
    pass


def test_empty_set_type():
    """set() — це set, а {} — це dict."""
    # TODO: замініть pass на:
    #   assert isinstance(set(), set)
    #   assert isinstance({}, dict)
    pass