"""Приклад 2: кілька except, as e, tuple. Запуск: pytest example_2_multiple_except.py -v"""


def lookup(data, index):
    try:
        return data[index]
    except IndexError:
        return "index error"
    except KeyError:
        return "key error"
    except TypeError:
        return "type error"

def parse_int(value):
    try:
        return int(value), None
    except ValueError as e:
        return None, str(e)

def safe_ratio(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return 0.0

def test_lookup():
    assert lookup([1, 2, 3], 5) == "index error"
    assert lookup({"a": 1}, "b") == "key error"
    assert lookup(None, 0) == "type error"

def test_parse_int_ok():
    assert parse_int("100") == (100, None)

def test_parse_int_error():
    result, message = parse_int("nope")
    assert result is None
    assert "invalid literal" in message

def test_safe_ratio():
    assert safe_ratio(10, 2) == 5.0
    assert safe_ratio(10, 0) == 0.0
    assert safe_ratio(10, "x") == 0.0
