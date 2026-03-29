"""
Вправа 3: Ітерація по словниках.
Запуск: pytest exercise_3_iteration.py -v
"""


CONFIG = {"host": "localhost", "port": 8080, "debug": True}
SCORES = {"Alice": 95, "Bob": 87, "Charlie": 92}
USER = {"name": "Alice", "age": 25, "role": "admin"}


def test_get_all_keys():
    """'host' є серед ключів config."""
    # TODO: замініть pass на: assert "host" in list(CONFIG.keys())
    pass


def test_get_all_values():
    """Максимальна оцінка == 95."""
    # TODO: замініть pass на: assert max(SCORES.values()) == 95
    pass


def test_items_contain():
    """('name', 'Alice') є серед items."""
    # TODO: замініть pass на: assert ("name", "Alice") in USER.items()
    pass


def test_no_none_values():
    """Жодне значення config не None."""
    # TODO: замініть pass на:
    #   for key, value in CONFIG.items():
    #       assert value is not None
    pass