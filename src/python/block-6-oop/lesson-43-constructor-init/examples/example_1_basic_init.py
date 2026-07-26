"""Приклад 1: Базовий __init__. Запуск: pytest example_1_basic_init.py -v"""


class User:
    def __init__(self, name):
        self.name = name


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class User3:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role


def test_single_attribute():
    u = User("Alice")
    assert u.name == "Alice"


def test_init_called_automatically():
    a = User("Alice")
    b = User("Bob")
    assert a.name == "Alice"
    assert b.name == "Bob"


def test_two_attributes():
    p = Point(3, 5)
    assert p.x == 3
    assert p.y == 5


def test_many_attributes():
    u = User3("Alice", "alice@example.com", "admin")
    assert u.name == "Alice"
    assert u.email == "alice@example.com"
    assert u.role == "admin"
