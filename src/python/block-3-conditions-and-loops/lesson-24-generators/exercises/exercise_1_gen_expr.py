"""
Вправа 1: Generator expressions.
Запуск: pytest exercise_1_gen_expr.py -v
"""


def test_all_positive():
    numbers = [5, 10, 15, 20]
    # TODO: замініть pass на: assert all(n > 0 for n in numbers)
    pass

def test_any_error():
    codes = [200, 200, 500, 200]
    # TODO: замініть pass на: assert any(c >= 400 for c in codes)
    pass

def test_sum_gen():
    prices = [10, 20, 30]
    # TODO: замініть pass на: assert sum(p for p in prices) == 60
    pass