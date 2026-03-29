"""
Приклад 3: Comprehensions у тестових сценаріях.
Запуск: pytest example_3_in_tests.py -v
"""


USERS = [
    {"id": 1, "name": "Alice", "email": "alice@t.com", "active": True},
    {"id": 2, "name": "Bob", "email": "bob@t.com", "active": False},
    {"id": 3, "name": "Charlie", "email": "charlie@t.com", "active": True},
]


def test_extract_ids():
    ids = [u["id"] for u in USERS]
    assert ids == [1, 2, 3]


def test_active_emails():
    emails = [u["email"] for u in USERS if u["active"]]
    assert emails == ["alice@t.com", "charlie@t.com"]


def test_name_to_id_map():
    name_map = {u["name"]: u["id"] for u in USERS}
    assert name_map["Alice"] == 1
    assert name_map["Bob"] == 2


def test_all_ids_positive():
    assert all(u["id"] > 0 for u in USERS)


def test_any_inactive():
    assert any(not u["active"] for u in USERS)