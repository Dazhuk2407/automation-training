"""Вправа 1: перехоплення винятків. Запуск: pytest exercise_1_catching.py -v"""


def to_float(value):
    # TODO: try: return float(value) except ValueError: return None
    pass

def safe_get(data, key, default=None):
    # TODO: try: return data[key] except (KeyError, TypeError): return default
    pass

def parse_error(value):
    # TODO: try: int(value); return None except ValueError as e: return str(e)
    pass

def test_to_float_ok():
    # TODO: assert to_float("3.14") == 3.14
    pass

def test_to_float_bad():
    # TODO: assert to_float("abc") is None
    pass

def test_safe_get():
    # TODO: assert safe_get({"a": 1}, "a") == 1
    pass

def test_safe_get_missing():
    # TODO: assert safe_get({"a": 1}, "b", 0) == 0
    pass

def test_parse_error():
    # TODO: assert "invalid literal" in parse_error("xx")
    pass
