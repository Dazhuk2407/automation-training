"""
Приклад 1: Основи списків — створення, індексація, slicing.

Запуск: pytest example_1_basics.py -v
"""


def test_create_list():
    """Різні способи створення списку."""
    status_codes = [200, 301, 404, 500]
    assert len(status_codes) == 4
    assert status_codes[0] == 200


def test_indexing():
    """Позитивні та від'ємні індекси."""
    endpoints = ["/users", "/auth", "/products", "/orders"]
    assert endpoints[0] == "/users"
    assert endpoints[-1] == "/orders"
    assert endpoints[-2] == "/products"


def test_slicing():
    """Зрізи — вибір частини списку."""
    codes = [200, 301, 302, 404, 500]
    assert codes[:2] == [200, 301]
    assert codes[2:] == [302, 404, 500]
    assert codes[1:3] == [301, 302]
    assert codes[-2:] == [404, 500]


def test_slice_step():
    """Slicing з кроком."""
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert numbers[::2] == [0, 2, 4, 6, 8]
    assert numbers[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def test_membership():
    """Перевірка належності."""
    allowed_methods = ["GET", "POST", "PUT", "DELETE"]
    assert "GET" in allowed_methods
    assert "PATCH" not in allowed_methods