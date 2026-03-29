"""
Вправа 4: Списки як тестові дані.
Запуск: pytest exercise_4_test_data.py -v
"""


USERS = [
    {"name": "Alice", "role": "admin", "active": True},
    {"name": "Bob", "role": "user", "active": True},
    {"name": "Charlie", "role": "user", "active": False},
]

RESPONSE_TIMES = [120, 45, 200, 89, 150, 310, 75]


def test_users_not_empty():
    """Список користувачів не порожній."""
    # TODO: замініть pass на: assert len(USERS) > 0
    pass


def test_all_have_name():
    """Кожен користувач має ключ 'name'."""
    # TODO: замініть pass на:
    #   for user in USERS:
    #       assert "name" in user
    pass


def test_active_count():
    """Двоє користувачів активні."""
    # TODO: замініть pass на:
    #   active = [u for u in USERS if u["active"]]
    #   assert len(active) == 2
    pass


def test_response_times_under_limit():
    """Всі часи відповіді < 1000ms."""
    # TODO: замініть pass на:
    #   for t in RESPONSE_TIMES:
    #       assert t < 1000
    pass