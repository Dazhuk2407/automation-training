"""Вправа 1: *args. Запуск: pytest exercise_1_args.py -v"""


def sum_all(*args):
    # TODO: return sum(args)
    pass

def count_args(*args):
    # TODO: return len(args)
    pass

def first_or_none(*args):
    # TODO: return args[0] if args else None
    pass

def test_sum():
    # TODO: assert sum_all(1, 2, 3) == 6
    pass

def test_sum_empty():
    # TODO: assert sum_all() == 0
    pass

def test_count():
    # TODO: assert count_args("a", "b", "c") == 3
    pass

def test_first():
    # TODO: assert first_or_none(10, 20) == 10
    pass

def test_first_empty():
    # TODO: assert first_or_none() is None
    pass