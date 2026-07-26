"""Вправа 1: f-strings форматування. Запуск: pytest exercise_1_format.py -v"""


def format_price(value):
    # TODO: return f"{value:.2f}"
    pass

def format_percent(ratio):
    # TODO: return f"{ratio:.1%}"
    pass

def align_name(name, width):
    # TODO: return f"{name:<{width}}"
    pass

def test_price():
    # TODO: assert format_price(19.5) == "19.50"
    pass

def test_price_int():
    # TODO: assert format_price(3) == "3.00"
    pass

def test_percent():
    # TODO: assert format_percent(0.8) == "80.0%"
    pass

def test_percent_full():
    # TODO: assert format_percent(1) == "100.0%"
    pass

def test_align():
    # TODO: assert align_name("qa", 5) == "qa   "
    pass
