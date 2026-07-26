"""Приклад 2: Числа, відсотки, вирівнювання. Запуск: pytest example_2_formatting.py -v"""


def format_price(value):
    return f"{value:.2f}"

def format_thousands(n):
    return f"{n:,}"

def pad_id(n):
    return f"{n:03d}"

def format_percent(ratio):
    return f"{ratio:.1%}"

def align_left(text, width):
    return f"{text:<{width}}"

def align_right(text, width):
    return f"{text:>{width}}"

def align_center(text, width):
    return f"{text:^{width}}"

def test_format_price():
    assert format_price(19.5) == "19.50"
    assert format_price(3) == "3.00"

def test_format_thousands():
    assert format_thousands(1234567) == "1,234,567"

def test_pad_id():
    assert pad_id(7) == "007"
    assert pad_id(42) == "042"

def test_format_percent():
    assert format_percent(0.8) == "80.0%"
    assert format_percent(0.1234) == "12.3%"

def test_alignment():
    assert align_left("ab", 6) == "ab    "
    assert align_right("ab", 6) == "    ab"
    assert align_center("ab", 6) == "  ab  "

def test_debug_equals():
    x = 5
    assert f"{x=}" == "x=5"
