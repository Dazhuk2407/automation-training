"""Приклад 2: __eq__ та порівняння об'єктів. Запуск: pytest example_2_eq_comparison.py -v"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class NoEq:
    def __init__(self, value):
        self.value = value


def parse_user(raw):
    name, role = raw.split(";")
    return User(name, role)


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __eq__(self, other):
        return self.name == other.name and self.role == other.role

    def __repr__(self):
        return f"User(name={self.name!r}, role={self.role!r})"


def test_eq_by_value():
    assert Point(1, 2) == Point(1, 2)

def test_not_eq_different_value():
    assert Point(1, 2) != Point(3, 4)

def test_without_eq_compares_by_id():
    assert NoEq(5) != NoEq(5)

def test_parse_user_returns_equal_object():
    result = parse_user("Alice;admin")
    assert result == User("Alice", "admin")

def test_eq_in_list():
    points = [Point(0, 0), Point(1, 1)]
    assert Point(1, 1) in points
