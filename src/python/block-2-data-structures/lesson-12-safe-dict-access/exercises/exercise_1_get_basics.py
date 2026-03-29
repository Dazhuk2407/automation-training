"""
Вправа 1: .get() основи.
Запуск: pytest exercise_1_get_basics.py -v
"""

import pytest


USER = {"name": "Alice", "role": "admin"}


def test_get_existing():
    """.get('name') повертає 'Alice'."""
    # TODO: замініть pass на: assert USER.get("name") == "Alice"
    pass


def test_get_missing_none():
    """.get('email') повертає None."""
    # TODO: замініть pass на: assert USER.get("email") is None
    pass


def test_get_with_default():
    """.get('age', 0) повертає 0."""
    # TODO: замініть pass на: assert USER.get("age", 0) == 0
    pass


def test_get_does_not_modify():
    """.get() не додає ключ до словника."""
    data = {"host": "localhost"}
    data.get("port", 8080)
    # TODO: замініть pass на: assert "port" not in data
    pass


def test_bracket_raises():
    """[] кидає KeyError при відсутньому ключі."""
    # TODO: замініть pass на:
    #   with pytest.raises(KeyError):
    #       _ = USER["email"]
    pass