"""Приклад 1: базовий підклас. Запуск: pytest example_1_basic_inheritance.py -v"""


class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, {self.name}"


class Admin(User):
    pass


class Guest(User):
    pass


def test_admin_inherits_attribute():
    admin = Admin("Alice")
    assert admin.name == "Alice"

def test_admin_inherits_method():
    admin = Admin("Alice")
    assert admin.greet() == "Hi, Alice"

def test_admin_is_user():
    admin = Admin("Alice")
    assert isinstance(admin, User)
    assert isinstance(admin, Admin)

def test_guest_also_inherits():
    guest = Guest("Bob")
    assert guest.greet() == "Hi, Bob"
    assert isinstance(guest, User)
