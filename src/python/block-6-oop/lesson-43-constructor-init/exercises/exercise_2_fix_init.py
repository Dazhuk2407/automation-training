"""Вправа 2: Виправ баг у __init__. Запуск: pytest exercise_2_fix_init.py -v

Тести нижче падають. Знайди рядок з поміткою `# BUG:` у __init__
та виправ його так, щоб усі тести проходили.
"""


class TestUser:
    def __init__(self, name, role, active=True):
        self.name = name
        self.role = name        # BUG: тут має бути role, а не name
        self.active = active


def test_name():
    u = TestUser("Alice", "admin")
    assert u.name == "Alice"


def test_role():
    u = TestUser("Alice", "admin")
    assert u.role == "admin"


def test_active_default():
    u = TestUser("Alice", "admin")
    assert u.active is True


def test_active_override():
    u = TestUser("Bob", "guest", active=False)
    assert u.active is False
