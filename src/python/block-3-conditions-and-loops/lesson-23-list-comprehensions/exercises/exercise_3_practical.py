"""
Вправа 3: Практичні comprehensions.
Запуск: pytest exercise_3_practical.py -v
"""

USERS = [
    {"id": 1, "name": "Alice", "active": True},
    {"id": 2, "name": "Bob", "active": False},
    {"id": 3, "name": "Charlie", "active": True},
]

def test_extract_ids():
    # TODO: замініть pass на: assert [u["id"] for u in USERS] == [1, 2, 3]
    pass

def test_active_names():
    # TODO: замініть pass на: assert [u["name"] for u in USERS if u["active"]] == ["Alice", "Charlie"]
    pass

def test_name_map():
    # TODO: замініть pass на: assert {u["name"]: u["id"] for u in USERS} == {"Alice": 1, "Bob": 2, "Charlie": 3}
    pass