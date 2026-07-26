"""Приклад 1: Найпростіший клас. Запуск: pytest example_1_first_class.py -v"""


class Dog:
    pass


class TestCase:
    pass


def test_instance_type():
    d = Dog()
    assert type(d) is Dog

def test_isinstance():
    d = Dog()
    assert isinstance(d, Dog)

def test_many_instances():
    login_test = TestCase()
    logout_test = TestCase()
    # різні об'єкти одного класу
    assert login_test is not logout_test
    assert isinstance(login_test, TestCase)
    assert isinstance(logout_test, TestCase)

def test_class_name():
    assert Dog.__name__ == "Dog"
