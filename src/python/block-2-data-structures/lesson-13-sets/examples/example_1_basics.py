"""
Приклад 1: Основи множин — створення, унікальність, базові операції.

Запуск: pytest example_1_basics.py -v
"""


def test_create_set():
    """Дублікати автоматично видаляються."""
    codes = {200, 301, 404, 404, 500, 500}
    assert len(codes) == 4


def test_empty_set():
    """Порожній set створюється через set(), не {}."""
    empty = set()
    assert len(empty) == 0
    assert isinstance(empty, set)


def test_add_element():
    """add() додає один елемент."""
    tags = {"smoke", "api"}
    tags.add("regression")
    assert "regression" in tags
    assert len(tags) == 3


def test_add_duplicate():
    """Додавання дублікату нічого не змінює."""
    tags = {"smoke", "api"}
    tags.add("smoke")
    assert len(tags) == 2


def test_remove_vs_discard():
    """remove кидає KeyError, discard — ні."""
    tags = {"smoke", "api"}
    tags.discard("nonexistent")  # без помилки
    assert len(tags) == 2

    tags.remove("smoke")
    assert "smoke" not in tags


def test_membership():
    """Перевірка належності — дуже швидка для set."""
    valid_codes = {200, 201, 204, 301, 302}
    assert 200 in valid_codes
    assert 404 not in valid_codes