"""Приклад 3: __len__ для власного контейнера. Запуск: pytest example_3_len_container.py -v"""


class TestSuite:
    def __init__(self, tests):
        self.tests = tests

    def __len__(self):
        return len(self.tests)

    def __contains__(self, name):
        return name in self.tests

    def __repr__(self):
        return f"TestSuite({self.tests!r})"


class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)


def test_len_of_suite():
    suite = TestSuite(["test_login", "test_logout", "test_signup"])
    assert len(suite) == 3

def test_len_empty():
    suite = TestSuite([])
    assert len(suite) == 0

def test_contains():
    suite = TestSuite(["test_login", "test_logout"])
    assert "test_login" in suite

def test_len_grows():
    cart = Cart()
    assert len(cart) == 0
    cart.add("book")
    cart.add("pen")
    assert len(cart) == 2

def test_len_used_in_assert():
    suite = TestSuite(["test_a", "test_b"])
    assert len(suite) == 2
