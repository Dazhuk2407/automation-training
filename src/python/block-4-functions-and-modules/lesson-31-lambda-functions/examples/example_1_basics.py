"""Приклад 1: Lambda basics. Запуск: pytest example_1_basics.py -v"""


def test_lambda_basic():
    double = lambda n: n * 2
    assert double(5) == 10

def test_lambda_with_two_args():
    add = lambda a, b: a + b
    assert add(3, 7) == 10

def test_lambda_string():
    to_upper = lambda s: s.upper()
    assert to_upper("hello") == "HELLO"

def test_lambda_conditional():
    sign = lambda n: "positive" if n > 0 else "non-positive"
    assert sign(5) == "positive"
    assert sign(-3) == "non-positive"