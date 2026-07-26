"""Приклад 3: instance / class / static разом. Запуск: pytest example_3_compare_methods.py -v"""


class Order:
    tax_rate = 0.2  # стан класу

    def __init__(self, amount):
        self.amount = amount  # стан екземпляра

    def total(self):
        """instance: читає self.amount та стан класу."""
        return self.amount * (1 + Order.tax_rate)

    @classmethod
    def free(cls):
        """class: factory через cls."""
        return cls(0)

    @staticmethod
    def is_valid_amount(amount):
        """static: чиста утиліта без self/cls."""
        return amount >= 0


def test_instance_method():
    order = Order(100)
    assert order.total() == 120.0

def test_class_method_factory():
    order = Order.free()
    assert order.amount == 0
    assert isinstance(order, Order)

def test_static_method():
    assert Order.is_valid_amount(50) is True
    assert Order.is_valid_amount(-10) is False

def test_static_callable_without_instance():
    # static можна викликати без створення об'єкта
    assert Order.is_valid_amount(0) is True
