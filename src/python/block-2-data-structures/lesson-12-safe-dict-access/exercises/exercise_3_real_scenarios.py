"""
Вправа 3: Реальні сценарії — config та API.
Запуск: pytest exercise_3_real_scenarios.py -v
"""


CONFIG = {"host": "api.example.com", "debug": True}

API_USER = {"id": 1, "name": "Alice", "role": "admin"}


def test_config_defaults():
    """host є, port та timeout мають default."""
    # TODO: замініть pass на:
    #   host = CONFIG.get("host", "localhost")
    #   port = CONFIG.get("port", 8080)
    #   timeout = CONFIG.get("timeout", 30)
    #   assert host == "api.example.com"
    #   assert port == 8080
    #   assert timeout == 30
    pass


def test_optional_field():
    """email відсутній → None."""
    # TODO: замініть pass на: assert API_USER.get("email") is None
    pass


def test_required_vs_optional():
    """id обов'язковий (через []), email опціональний (через .get())."""
    # TODO: замініть pass на:
    #   assert API_USER["id"] == 1
    #   assert API_USER.get("email", "N/A") == "N/A"
    pass


def test_fallback_value():
    """nickname fallback на name."""
    # TODO: замініть pass на:
    #   nickname = API_USER.get("nickname", API_USER["name"])
    #   assert nickname == "Alice"
    pass