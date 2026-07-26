"""Приклад 2: поліморфізм. Запуск: pytest example_2_polymorphism.py -v"""


class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h


def total_area(shapes):
    return sum(shape.area() for shape in shapes)


class LoginPage:
    def is_loaded(self):
        return True

class DashboardPage:
    def is_loaded(self):
        return True


def test_polymorphic_call():
    shapes = [Circle(10), Square(5), Rectangle(2, 3)]
    areas = [shape.area() for shape in shapes]
    assert areas == [314.0, 25, 6]

def test_total_area():
    shapes = [Square(2), Rectangle(3, 4)]
    assert total_area(shapes) == 16

def test_duck_typing():
    # будь-який об'єкт з .area() підходить
    class Triangle:
        def area(self):
            return 42
    assert total_area([Triangle()]) == 42

def test_pages_same_interface():
    pages = [LoginPage(), DashboardPage()]
    assert all(p.is_loaded() for p in pages)
