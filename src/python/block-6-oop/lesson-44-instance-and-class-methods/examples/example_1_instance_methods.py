"""Приклад 1: методи екземпляра та self. Запуск: pytest example_1_instance_methods.py -v"""


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def is_admin(self):
        return self.role == "admin"

    def greet(self):
        return f"Hi, {self.name}"

    def promote(self):
        self.role = "admin"


class TestCase:
    def __init__(self, title, status="new"):
        self.title = title
        self.status = status

    def run(self):
        self.status = "passed"
        return self.status


def test_is_admin():
    alice = User("Alice", "admin")
    bob = User("Bob", "user")
    assert alice.is_admin() is True
    assert bob.is_admin() is False

def test_greet_uses_self():
    assert User("Alice", "user").greet() == "Hi, Alice"

def test_promote_mutates_instance():
    bob = User("Bob", "user")
    bob.promote()
    assert bob.is_admin() is True

def test_instances_are_independent():
    alice = User("Alice", "admin")
    bob = User("Bob", "user")
    bob.promote()
    assert alice.role == "admin"
    assert bob.role == "admin"

def test_run_changes_status():
    tc = TestCase("Login")
    assert tc.status == "new"
    assert tc.run() == "passed"
    assert tc.status == "passed"
