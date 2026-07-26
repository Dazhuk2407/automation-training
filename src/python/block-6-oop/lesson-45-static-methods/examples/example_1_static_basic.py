"""Приклад 1: базовий @staticmethod. Запуск: pytest example_1_static_basic.py -v"""


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def square(x):
        return x * x


class TextUtils:
    @staticmethod
    def to_upper(text):
        return text.upper()


def test_add_via_class():
    assert MathUtils.add(2, 3) == 5

def test_square_via_class():
    assert MathUtils.square(4) == 16

def test_via_instance():
    utils = MathUtils()
    assert utils.add(10, 20) == 30

def test_class_and_instance_equal():
    assert TextUtils.to_upper("qa") == TextUtils().to_upper("qa") == "QA"
