"""
Приклад 2: Unpacking — розпакування tuples.

Запуск: pytest example_2_unpacking.py -v
"""


def get_user_info():
    """Повертає tuple (name, role, active)."""
    return "Alice", "admin", True


def get_api_response():
    """Повертає tuple (status_code, body)."""
    return 200, {"users": [{"name": "Alice"}]}


def test_basic_unpacking():
    """Розпакування у змінні."""
    point = (10, 20)
    x, y = point
    assert x == 10
    assert y == 20


def test_function_return_unpacking():
    """Розпакування результату функції."""
    name, role, active = get_user_info()
    assert name == "Alice"
    assert role == "admin"
    assert active is True


def test_ignore_with_underscore():
    """Ігнорування значень через _."""
    code, _ = get_api_response()
    assert code == 200


def test_star_unpacking():
    """Розпакування з * (зірочкою)."""
    first, *rest = (1, 2, 3, 4, 5)
    assert first == 1
    assert rest == [2, 3, 4, 5]

    head, *middle, tail = (10, 20, 30, 40, 50)
    assert head == 10
    assert middle == [20, 30, 40]
    assert tail == 50


def test_swap_values():
    """Обмін значень через unpacking."""
    a, b = 1, 2
    a, b = b, a
    assert a == 2
    assert b == 1