"""Приклад 2: @classmethod, cls та factory from_dict. Запуск: pytest example_2_class_methods.py -v"""


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["role"])

    @classmethod
    def guest(cls):
        return cls("guest", "guest")


class TestCase:
    count = 0

    def __init__(self, title):
        self.title = title
        TestCase.count += 1

    @classmethod
    def total_created(cls):
        return cls.count


def test_from_dict_builds_user():
    data = {"name": "Alice", "role": "admin"}
    user = User.from_dict(data)
    assert user.name == "Alice"
    assert user.role == "admin"

def test_from_dict_on_api_response():
    api_response = {"name": "Bob", "role": "user"}
    user = User.from_dict(api_response)
    assert user.role == "user"

def test_guest_factory():
    g = User.guest()
    assert g.name == "guest"
    assert g.role == "guest"

def test_classmethod_no_instance_needed():
    TestCase.count = 0
    TestCase("Smoke: login")
    TestCase("Smoke: logout")
    assert TestCase.total_created() == 2

def test_from_dict_returns_correct_type():
    user = User.from_dict({"name": "X", "role": "y"})
    assert isinstance(user, User)
