"""
Приклад 3: Списки в реальних тестах.

Запуск: pytest example_3_lists_in_tests.py -v
"""


# --- Імітація API ---

def get_users():
    """Повертає список користувачів (імітація API response)."""
    return [
        {"id": 1, "name": "Alice", "role": "admin", "active": True},
        {"id": 2, "name": "Bob", "role": "user", "active": True},
        {"id": 3, "name": "Charlie", "role": "user", "active": False},
    ]


def get_response_times():
    """Повертає список часу відповіді API (ms)."""
    return [120, 45, 200, 89, 150, 310, 75]


# --- Тести ---

def test_users_count():
    """Перевірити кількість користувачів."""
    users = get_users()
    assert len(users) == 3


def test_admin_is_first():
    """Перший користувач — admin."""
    users = get_users()
    assert users[0]["role"] == "admin"


def test_all_users_have_required_fields():
    """Кожен користувач має обов'язкові поля."""
    required = ["id", "name", "role", "active"]
    users = get_users()
    for user in users:
        for field in required:
            assert field in user, f"User {user.get('name')} missing '{field}'"


def test_active_users_count():
    """Кількість активних користувачів."""
    users = get_users()
    active = [u for u in users if u["active"]]
    assert len(active) == 2


def test_response_times_within_limit():
    """Всі відповіді швидше за 500ms."""
    times = get_response_times()
    for t in times:
        assert t < 500, f"Response time {t}ms exceeds 500ms limit"


def test_average_response_time():
    """Середній час відповіді менше 200ms."""
    times = get_response_times()
    average = sum(times) / len(times)
    assert average < 200, f"Average {average:.1f}ms exceeds 200ms"