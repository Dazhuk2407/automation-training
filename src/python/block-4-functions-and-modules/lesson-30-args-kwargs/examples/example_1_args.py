"""Приклад 1: *args. Запуск: pytest example_1_args.py -v"""


def sum_all(*args):
    return sum(args)

def max_of(*args):
    return max(args) if args else None

def collect(*args):
    return list(args)

def test_sum_all():
    assert sum_all(1, 2, 3) == 6
    assert sum_all(10, 20) == 30
    assert sum_all() == 0

def test_max_of():
    assert max_of(3, 7, 1) == 7
    assert max_of(42) == 42
    assert max_of() is None

def test_collect():
    assert collect(1, 2, 3) == [1, 2, 3]
    assert collect() == []

def test_args_is_tuple():
    def check(*args):
        return type(args)
    assert check(1, 2) == tuple