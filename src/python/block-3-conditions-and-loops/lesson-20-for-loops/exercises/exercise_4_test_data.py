"""
Вправа 4: Цикли в тестових перевірках.
Запуск: pytest exercise_4_test_data.py -v
"""


USERS = [
    {"name": "Alice", "email": "alice@t.com", "role": "admin", "active": True},
    {"name": "Bob", "email": "bob@t.com", "role": "user", "active": True},
    {"name": "Charlie", "email": "charlie@t.com", "role": "user", "active": False},
]


def test_all_emails_valid():
    """Кожен email містить '@'."""
    # TODO: замініть pass на:
    #   for user in USERS:
    #       assert "@" in user["email"]
    pass


def test_count_active():
    """Порахувати кількість активних користувачів."""
    # TODO: замініть pass на:
    #   count = 0
    #   for user in USERS:
    #       if user["active"]:
    #           count += 1
    #   assert count == 2
    pass


def test_find_admin():
    """Знайти першого admin."""
    # TODO: замініть pass на:
    #   admin = None
    #   for user in USERS:
    #       if user["role"] == "admin":
    #           admin = user
    #           break
    #   assert admin is not None
    #   assert admin["name"] == "Alice"
    pass