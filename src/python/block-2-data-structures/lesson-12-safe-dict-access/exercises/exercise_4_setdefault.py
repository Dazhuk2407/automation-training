"""
Вправа 4: setdefault() для ініціалізації.
Запуск: pytest exercise_4_setdefault.py -v
"""


def test_setdefault_adds():
    """setdefault додає ключ якщо його немає."""
    config = {"host": "localhost"}
    # TODO: замініть pass на:
    #   config.setdefault("port", 8080)
    #   assert config["port"] == 8080
    pass


def test_setdefault_keeps():
    """setdefault не змінює існуючий ключ."""
    config = {"host": "localhost", "port": 3000}
    # TODO: замініть pass на:
    #   config.setdefault("port", 8080)
    #   assert config["port"] == 3000
    pass


def test_group_errors():
    """Використати setdefault для групування помилок."""
    log_entries = ["timeout", "404", "timeout", "500", "timeout"]
    # TODO: замініть pass на:
    #   grouped = {}
    #   for entry in log_entries:
    #       grouped.setdefault(entry, []).append(1)
    #   assert len(grouped["timeout"]) == 3
    #   assert len(grouped["404"]) == 1
    pass