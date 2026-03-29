"""
Вправа 2: or для fallback значень.
Запуск: pytest exercise_2_or_defaults.py -v
"""


def test_name_or_default():
    """Ім'я або 'Anonymous'."""
    name = "Alice"
    # TODO: замініть pass на:
    #   result = name or "Anonymous"
    #   assert result == "Alice"
    pass


def test_none_fallback():
    """None → fallback."""
    value = None
    # TODO: замініть pass на:
    #   result = value or "fallback"
    #   assert result == "fallback"
    pass


def test_empty_string_fallback():
    """Порожній рядок → default."""
    text = ""
    # TODO: замініть pass на:
    #   result = text or "default"
    #   assert result == "default"
    pass