"""
Приклад 2: Змішування та порядок аргументів.
Запуск: pytest example_2_mixed.py -v
"""

import pytest


def make_request(method, url, body=None, timeout=30):
    return {"method": method, "url": url, "body": body, "timeout": timeout}


def test_minimal_call():
    req = make_request("GET", "/api/users")
    assert req["method"] == "GET"
    assert req["body"] is None
    assert req["timeout"] == 30


def test_with_keyword():
    req = make_request("POST", "/api/users", body={"name": "Alice"})
    assert req["body"] == {"name": "Alice"}


def test_all_keyword():
    req = make_request(method="DELETE", url="/api/users/1", timeout=5)
    assert req["method"] == "DELETE"
    assert req["timeout"] == 5


def test_duplicate_argument_raises():
    """Не можна передати аргумент і positional, і keyword."""
    with pytest.raises(TypeError):
        make_request("GET", method="POST", url="/api")