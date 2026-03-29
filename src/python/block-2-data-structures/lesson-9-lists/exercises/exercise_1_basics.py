"""
Вправа 1: Основи списків.
Запуск: pytest exercise_1_basics.py -v
"""


def test_first_element():
    """Перший елемент [10, 20, 30] == 10."""
    numbers = [10, 20, 30]
    # TODO: замініть pass на: assert numbers[0] == 10
    pass


def test_last_element():
    """Останній елемент через [-1] == 30."""
    numbers = [10, 20, 30]
    # TODO: замініть pass на: assert numbers[-1] == 30
    pass


def test_length():
    """Довжина списку == 4."""
    codes = [200, 301, 404, 500]
    # TODO: замініть pass на: assert len(codes) == 4
    pass


def test_slice_first_two():
    """Перші 2 елементи."""
    codes = [200, 301, 404, 500]
    # TODO: замініть pass на: assert codes[:2] == [200, 301]
    pass


def test_slice_last_two():
    """Останні 2 елементи."""
    codes = [200, 301, 404, 500]
    # TODO: замініть pass на: assert codes[-2:] == [404, 500]
    pass


def test_membership():
    """GET є в списку HTTP-методів."""
    methods = ["GET", "POST", "PUT"]
    # TODO: замініть pass на: assert "GET" in methods
    pass