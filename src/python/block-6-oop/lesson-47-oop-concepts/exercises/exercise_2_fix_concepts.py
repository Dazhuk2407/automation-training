"""Вправа 2: виправ баг. Запуск: pytest exercise_2_fix_concepts.py -v

Тести падають — знайди коментар `# BUG:` і виправ помилку.
Рівно один тест має падати до фіксу.
"""


class Circle:
    def __init__(self, r):
        self._r = r

    def area(self):
        return 3.14 * self._r ** 2


class Rectangle:
    def __init__(self, w, h):
        self._w = w
        self._h = h

    def area(self):
        # BUG: площа прямокутника — це w * h, а не w + h
        return self._w + self._h


class Vault:
    def __init__(self, secret):
        self.__secret = secret

    def reveal(self, key):
        return self.__secret if key == "open" else None


def test_circle_area():
    assert Circle(10).area() == 314.0

def test_rectangle_area():
    assert Rectangle(3, 4).area() == 12

def test_polymorphism():
    shapes = [Circle(10), Rectangle(2, 2)]
    total = sum(s.area() for s in shapes)
    assert total == 318.0

def test_vault_private():
    v = Vault("token")
    assert v.reveal("open") == "token"
    assert v._Vault__secret == "token"
