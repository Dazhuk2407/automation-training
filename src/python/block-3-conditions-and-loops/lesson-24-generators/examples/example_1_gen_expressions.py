"""
Приклад 1: Generator expressions.
Запуск: pytest example_1_gen_expressions.py -v
"""


def test_gen_is_not_list():
    gen = (n for n in range(5))
    assert not isinstance(gen, list)
    assert list(gen) == [0, 1, 2, 3, 4]


def test_gen_exhausted():
    """Генератор вичерпується після першої ітерації."""
    gen = (n for n in range(3))
    first = list(gen)
    second = list(gen)
    assert first == [0, 1, 2]
    assert second == []


def test_all_with_gen():
    users = [{"active": True}, {"active": True}, {"active": True}]
    assert all(u["active"] for u in users)


def test_any_with_gen():
    codes = [200, 200, 500, 200]
    assert any(c >= 400 for c in codes)


def test_sum_with_gen():
    prices = [10.5, 20.0, 5.5]
    assert sum(p for p in prices) == 36.0