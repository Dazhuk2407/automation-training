"""Вправа 2: filter та map з lambda. Запуск: pytest exercise_2_filter_map.py -v"""


def test_filter_positive():
    numbers = [-3, 5, -1, 8, 0]
    # TODO: замініть pass на:
    #   positive = list(filter(lambda n: n > 0, numbers))
    #   assert positive == [5, 8]
    pass

def test_map_double():
    numbers = [1, 2, 3, 4]
    # TODO: замініть pass на:
    #   doubled = list(map(lambda n: n * 2, numbers))
    #   assert doubled == [2, 4, 6, 8]
    pass

def test_map_extract_names():
    users = [{"name": "Alice"}, {"name": "Bob"}]
    # TODO: замініть pass на:
    #   names = list(map(lambda u: u["name"], users))
    #   assert names == ["Alice", "Bob"]
    pass

def test_filter_active():
    users = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False},
        {"name": "Charlie", "active": True},
    ]
    # TODO: замініть pass на:
    #   active = list(filter(lambda u: u["active"], users))
    #   assert len(active) == 2
    pass