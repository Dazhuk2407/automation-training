"""
Приклад 1: if / elif / else та truthy / falsy.

Запуск: pytest example_1_basics.py -v
"""


def classify_status(code):
    """Класифікувати HTTP статус код."""
    if code < 200:
        return "informational"
    elif code < 300:
        return "success"
    elif code < 400:
        return "redirect"
    elif code < 500:
        return "client_error"
    else:
        return "server_error"


def test_success():
    assert classify_status(200) == "success"
    assert classify_status(201) == "success"


def test_client_error():
    assert classify_status(404) == "client_error"
    assert classify_status(400) == "client_error"


def test_server_error():
    assert classify_status(500) == "server_error"
    assert classify_status(503) == "server_error"


def test_truthy_falsy():
    """Truthy та falsy значення."""
    assert bool([1, 2, 3]) is True   # непорожній список
    assert bool([]) is False          # порожній список
    assert bool("text") is True       # непорожній рядок
    assert bool("") is False          # порожній рядок
    assert bool(0) is False
    assert bool(42) is True
    assert bool(None) is False


def test_truthy_in_conditions():
    """Pythonic перевірки через truthy."""
    users = ["Alice", "Bob"]
    assert users  # не порожній → truthy

    empty = []
    assert not empty  # порожній → falsy