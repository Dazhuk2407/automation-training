"""
Вправа 1: List comprehensions.
Запуск: pytest exercise_1_list_comp.py -v
"""


def test_squares():
    # TODO: замініть pass на: assert [n ** 2 for n in range(1, 6)] == [1, 4, 9, 16, 25]
    pass

def test_filter_errors():
    codes = [200, 301, 404, 500, 201]
    # TODO: замініть pass на: assert [c for c in codes if c >= 400] == [404, 500]
    pass

def test_upper_names():
    names = ["alice", "bob"]
    # TODO: замініть pass на: assert [n.upper() for n in names] == ["ALICE", "BOB"]
    pass

def test_ternary_labels():
    codes = [200, 404, 500]
    # TODO: замініть pass на: assert ["OK" if c < 400 else "ERROR" for c in codes] == ["OK", "ERROR", "ERROR"]
    pass