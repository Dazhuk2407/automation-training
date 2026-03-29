"""
Вправа 2: Валідація структури даних.
Запуск: pytest exercise_2_validation.py -v
"""

USERS = [
    {"id": 1, "name": "Alice", "email": "alice@test.com", "roles": ["admin"]},
    {"id": 2, "name": "Bob", "email": "bob@test.com", "roles": ["user"]},
    {"id": 3, "name": "Charlie", "email": "charlie@test.com", "roles": ["user", "editor"]},
]


def test_required_fields():
    """Кожен user має id, name, email."""
    required = {"id", "name", "email"}
    # TODO: замініть pass на:
    #   for user in USERS:
    #       assert required.issubset(user.keys())
    pass


def test_all_emails_valid():
    """Кожен email містить '@'."""
    # TODO: замініть pass на:
    #   for user in USERS:
    #       assert "@" in user["email"]
    pass


def test_unique_ids():
    """ID унікальні."""
    ids = [u["id"] for u in USERS]
    # TODO: замініть pass на: assert len(ids) == len(set(ids))
    pass


def test_roles_not_empty():
    """Кожен user має хоча б одну роль."""
    # TODO: замініть pass на:
    #   for user in USERS:
    #       assert len(user["roles"]) > 0
    pass