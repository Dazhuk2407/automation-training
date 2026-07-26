"""Вправа 1: інкапсуляція та поліморфізм. Запуск: pytest exercise_1_concepts.py -v"""


class Wallet:
    def __init__(self, amount):
        # TODO: self._balance = amount   (protected)
        # TODO: self.__code = "1234"     (private)
        pass

    def get_balance(self):
        # TODO: return self._balance
        pass

    def check_code(self, code):
        # TODO: return self.__code == code
        pass


class Dog:
    def speak(self):
        # TODO: return "Woof"
        pass

class Cat:
    def speak(self):
        # TODO: return "Meow"
        pass


def test_protected():
    # TODO: assert Wallet(100)._balance == 100
    pass

def test_get_balance():
    # TODO: assert Wallet(50).get_balance() == 50
    pass

def test_private_name_mangling():
    # TODO: assert Wallet(0)._Wallet__code == "1234"
    pass

def test_check_code():
    # TODO: assert Wallet(0).check_code("1234") is True
    pass

def test_polymorphism():
    # TODO:
    #   animals = [Dog(), Cat()]
    #   assert [a.speak() for a in animals] == ["Woof", "Meow"]
    pass
