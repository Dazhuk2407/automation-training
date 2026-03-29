"""
Вправа 1: Основи словників.
Запуск: pytest exercise_1_basics.py -v
"""


USER = {"name": "Alice", "role": "admin", "age": 25}
CONFIG = {"host": "localhost", "port": 8080, "debug": True}


def test_access():
    """user['name'] == 'Alice'."""
    # TODO: замініть pass на: assert USER["name"] == "Alice"
    pass


def test_length():
    """config має 3 ключі."""
    # TODO: замініть pass на: assert len(CONFIG) == 3
    pass


def test_key_exists():
    """'host' є ключем config."""
    # TODO: замініть pass на: assert "host" in CONFIG
    pass


def test_key_missing():
    """'password' немає в config."""
    # TODO: замініть pass на: assert "password" not in CONFIG
    pass


def test_value_in_values():
    """'Alice' є серед значень user."""
    # TODO: замініть pass на: assert "Alice" in USER.values()
    pass