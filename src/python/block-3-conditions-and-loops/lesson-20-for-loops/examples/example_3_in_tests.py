"""
Приклад 3: for у тестових перевірках.
Запуск: pytest example_3_in_tests.py -v
"""


USERS = [
    {"id": 1, "name": "Alice", "email": "alice@t.com", "active": True},
    {"id": 2, "name": "Bob", "email": "bob@t.com", "active": True},
    {"id": 3, "name": "Charlie", "email": "charlie@t.com", "active": False},
]


def test_all_have_required_fields():
    required = ["id", "name", "email"]
    for user in USERS:
        for field in required:
            assert field in user, f"User {user['name']} missing '{field}'"


def test_all_ids_are_int():
    for user in USERS:
        assert isinstance(user["id"], int)


def test_all_emails_contain_at():
    for user in USERS:
        assert "@" in user["email"], f"Invalid email: {user['email']}"


def test_count_active():
    active_count = 0
    for user in USERS:
        if user["active"]:
            active_count += 1
    assert active_count == 2


def test_find_inactive_names():
    inactive = []
    for user in USERS:
        if not user["active"]:
            inactive.append(user["name"])
    assert inactive == ["Charlie"]