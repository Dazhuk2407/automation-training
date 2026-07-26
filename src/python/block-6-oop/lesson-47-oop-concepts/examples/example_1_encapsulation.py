"""Приклад 1: інкапсуляція. Запуск: pytest example_1_encapsulation.py -v"""


class Account:
    def __init__(self, balance):
        self.owner = "public"        # публічний
        self._balance = balance      # protected за конвенцією
        self.__pin = "0000"          # private: name mangling

    def get_balance(self):
        return self._balance

    def check_pin(self, pin):
        return self.__pin == pin


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Нижче абсолютного нуля")
        self._celsius = value


def test_protected_accessible():
    acc = Account(100)
    assert acc._balance == 100
    assert acc.get_balance() == 100

def test_private_name_mangling():
    acc = Account(100)
    assert acc.check_pin("0000") is True
    # __pin перейменований у _Account__pin
    assert acc._Account__pin == "0000"

def test_private_not_directly_accessible():
    acc = Account(100)
    import pytest
    with pytest.raises(AttributeError):
        _ = acc.__pin

def test_property_get():
    t = Temperature(20)
    assert t.celsius == 20

def test_property_setter_validation():
    t = Temperature(20)
    t.celsius = 25
    assert t.celsius == 25
    import pytest
    with pytest.raises(ValueError):
        t.celsius = -300
