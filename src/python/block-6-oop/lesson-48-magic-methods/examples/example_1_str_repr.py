"""Приклад 1: __str__ vs __repr__. Запуск: pytest example_1_str_repr.py -v"""


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"User(name={self.name!r}, user_id={self.user_id})"


class TestCase:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"TestCase({self.name!r})"


def test_str_for_user():
    u = User("Alice", 1)
    assert str(u) == "User: Alice"

def test_repr_for_developer():
    u = User("Alice", 1)
    assert repr(u) == "User(name='Alice', user_id=1)"

def test_print_uses_str():
    u = User("Bob", 2)
    assert format(u) == "User: Bob"

def test_container_uses_repr():
    u = User("Alice", 1)
    assert str([u]) == "[User(name='Alice', user_id=1)]"

def test_repr_is_fallback_for_str():
    tc = TestCase("test_login")
    assert str(tc) == "TestCase('test_login')"
    assert repr(tc) == "TestCase('test_login')"
