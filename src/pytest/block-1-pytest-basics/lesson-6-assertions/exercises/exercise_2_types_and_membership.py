"""
Вправа 2: Типи та належність.

Використовуйте isinstance() для перевірки типів.
Використовуйте in / not in для належності.

Запуск: pytest exercise_2_types_and_membership.py -v
"""


def test_isinstance_int():
    """42 — це int."""
    # TODO: замініть pass на: assert isinstance(42, int)
    pass


def test_isinstance_str():
    """'hello' — це str."""
    # TODO: замініть pass на: assert isinstance("hello", str)
    pass


def test_isinstance_multiple():
    """3.14 — це int або float."""
    # TODO: замініть pass на: assert isinstance(3.14, (int, float))
    pass


def test_in_list():
    """3 є в списку [1, 2, 3]."""
    # TODO: замініть pass на: assert 3 in [1, 2, 3]
    pass


def test_in_string():
    """'test' є підрядком 'pytest'."""
    # TODO: замініть pass на: assert "test" in "pytest"
    pass


def test_not_in_dict():
    """'phone' немає серед ключів словника."""
    user = {"name": "Alice"}
    # TODO: замініть pass на: assert "phone" not in user
    pass