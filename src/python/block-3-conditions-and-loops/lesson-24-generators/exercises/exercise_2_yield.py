"""
Вправа 2: Generator functions з yield.
Запуск: pytest exercise_2_yield.py -v
"""


def count_up(n):
    """Генерувати числа від 1 до n."""
    # TODO: замініть pass на:
    #   i = 1
    #   while i <= n:
    #       yield i
    #       i += 1
    pass


def generate_ids(start, end):
    """Генерувати ID від start до end включно."""
    # TODO: замініть pass на:
    #   for i in range(start, end + 1):
    #       yield i
    pass


def page_numbers(total, page_size):
    """Генерувати номери сторінок."""
    # TODO: замініть pass на:
    #   page = 1
    #   while (page - 1) * page_size < total:
    #       yield page
    #       page += 1
    pass


def test_count_up():
    # TODO: замініть pass на: assert list(count_up(5)) == [1, 2, 3, 4, 5]
    pass

def test_generate_ids():
    # TODO: замініть pass на: assert list(generate_ids(10, 13)) == [10, 11, 12, 13]
    pass

def test_page_numbers():
    # TODO: замініть pass на: assert list(page_numbers(25, 10)) == [1, 2, 3]
    pass