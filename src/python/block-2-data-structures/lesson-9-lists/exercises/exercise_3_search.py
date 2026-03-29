"""
Вправа 3: Пошук та фільтрація.
Запуск: pytest exercise_3_search.py -v
"""


def test_count_occurrences():
    """Порахувати скільки разів 200 зустрічається."""
    codes = [200, 301, 200, 404, 200, 500]
    # TODO: замініть pass на: assert codes.count(200) == 3
    pass


def test_find_index():
    """Знайти індекс елемента 404."""
    codes = [200, 301, 404, 500]
    # TODO: замініть pass на: assert codes.index(404) == 2
    pass


def test_filter_errors():
    """Відфільтрувати коди >= 400 (клієнтські та серверні помилки)."""
    codes = [200, 301, 404, 500, 201, 503]
    # TODO: замініть pass на:
    #   errors = [c for c in codes if c >= 400]
    #   assert errors == [404, 500, 503]
    pass


def test_all_positive():
    """Перевірити що всі числа > 0."""
    times = [120, 45, 200, 89]
    # TODO: замініть pass на: assert all(t > 0 for t in times)
    pass