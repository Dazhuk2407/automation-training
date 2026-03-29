"""
Приклад 2: or для default та fallback значень.

Запуск: pytest example_2_or_defaults.py -v
"""


def test_or_with_string():
    """or повертає перше truthy значення."""
    name = "Alice" or "Default"
    assert name == "Alice"

    name = "" or "Default"
    assert name == "Default"


def test_or_with_none():
    """None — falsy, or поверне fallback."""
    value = None or "fallback"
    assert value == "fallback"


def test_or_chain():
    """Ланцюжок or — перше truthy."""
    result = None or "" or 0 or "found"
    assert result == "found"


def test_or_zero_pitfall():
    """Обережно: 0 — falsy!"""
    port = 0 or 8080
    assert port == 8080  # 0 загублено!

    # Правильно для 0 як валідного значення:
    port = 0
    actual = port if port is not None else 8080
    assert actual == 0


def test_dict_get_vs_or():
    """Порівняння .get(default) та or."""
    config = {"host": "localhost", "port": 0}

    # .get() зберігає 0
    port_get = config.get("port", 8080)
    assert port_get == 0

    # or втрачає 0
    port_or = config.get("port") or 8080
    assert port_or == 8080  # 0 → falsy → fallback