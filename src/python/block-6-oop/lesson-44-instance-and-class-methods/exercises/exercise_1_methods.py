"""Вправа 1: instance та class methods. Запуск: pytest exercise_1_methods.py -v"""


class User:
    count = 0

    def __init__(self, name, role):
        # TODO: self.name = name; self.role = role; User.count += 1
        pass

    def is_admin(self):
        # TODO: return self.role == "admin"
        pass

    @classmethod
    def from_dict(cls, data):
        # TODO: return cls(data["name"], data["role"])
        pass


def test_is_admin_true():
    # TODO: assert User("Alice", "admin").is_admin() is True
    pass

def test_is_admin_false():
    # TODO: assert User("Bob", "user").is_admin() is False
    pass

def test_from_dict_name():
    # TODO: assert User.from_dict({"name": "Al", "role": "admin"}).name == "Al"
    pass

def test_from_dict_role():
    # TODO: assert User.from_dict({"name": "Al", "role": "user"}).role == "user"
    pass

def test_counter():
    # TODO: User.count = 0; User("A", "user"); User("B", "user"); assert User.count == 2
    pass
