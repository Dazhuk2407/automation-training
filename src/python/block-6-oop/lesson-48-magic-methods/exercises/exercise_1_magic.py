"""Вправа 1: magic-методи. Запуск: pytest exercise_1_magic.py -v"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        # TODO: return f"Product: {self.name} (${self.price})"
        pass

    def __eq__(self, other):
        # TODO: return self.name == other.name and self.price == other.price
        pass


class Basket:
    def __init__(self, products):
        self.products = products

    def __len__(self):
        # TODO: return len(self.products)
        pass


def test_str():
    # TODO: assert str(Product("Book", 10)) == "Product: Book ($10)"
    pass

def test_eq_equal():
    # TODO: assert Product("Book", 10) == Product("Book", 10)
    pass

def test_eq_not_equal():
    # TODO: assert Product("Book", 10) != Product("Pen", 10)
    pass

def test_len():
    # TODO: assert len(Basket(["Book", "Pen", "Cup"])) == 3
    pass

def test_len_empty():
    # TODO: assert len(Basket([])) == 0
    pass
