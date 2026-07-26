"""Вправа 1: наслідування. Запуск: pytest exercise_1_inherit.py -v"""


class Animal:
    def __init__(self, name):
        # TODO: self.name = name
        pass

    def speak(self):
        # TODO: return "..."
        pass


class Dog(Animal):
    def __init__(self, name, breed):
        # TODO: super().__init__(name); self.breed = breed
        pass

    def speak(self):
        # TODO: return "Woof"
        pass


def test_dog_inherits_name():
    # TODO: assert Dog("Rex", "husky").name == "Rex"
    pass

def test_dog_has_breed():
    # TODO: assert Dog("Rex", "husky").breed == "husky"
    pass

def test_dog_overrides_speak():
    # TODO: assert Dog("Rex", "husky").speak() == "Woof"
    pass

def test_dog_is_animal():
    # TODO: assert isinstance(Dog("Rex", "husky"), Animal)
    pass

def test_dog_is_subclass():
    # TODO: assert issubclass(Dog, Animal)
    pass
