"""
Вправа 2: Dict та set comprehensions.
Запуск: pytest exercise_2_dict_set_comp.py -v
"""


def test_dict_from_lists():
    keys = ["name", "age"]
    values = ["Alice", 25]
    # TODO: замініть pass на: assert {k: v for k, v in zip(keys, values)} == {"name": "Alice", "age": 25}
    pass

def test_unique_domains():
    emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com"]
    # TODO: замініть pass на: assert {e.split("@")[1] for e in emails} == {"gmail.com", "yahoo.com"}
    pass

def test_filter_config():
    config = {"host": "localhost", "port": 8080, "debug": False}
    # TODO: замініть pass на:
    #   truthy = {k: v for k, v in config.items() if v}
    #   assert "debug" not in truthy
    #   assert "host" in truthy
    pass