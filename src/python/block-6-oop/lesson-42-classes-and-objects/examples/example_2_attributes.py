"""Приклад 2: Атрибути екземпляра. Запуск: pytest example_2_attributes.py -v"""


class Dog:
    def set_name(self, name):
        self.name = name


class User:
    def set_role(self, role):
        self.role = role

    def is_admin(self):
        return self.role == "admin"


def test_attribute_via_method():
    d = Dog()
    d.set_name("Rex")
    assert d.name == "Rex"

def test_attribute_from_outside():
    d = Dog()
    d.age = 3  # атрибут задано ззовні
    assert d.age == 3

def test_role_attribute():
    u = User()
    u.set_role("admin")
    assert u.role == "admin"

def test_method_uses_attribute():
    u = User()
    u.set_role("admin")
    assert u.is_admin() is True

def test_non_admin():
    u = User()
    u.set_role("guest")
    assert u.is_admin() is False
