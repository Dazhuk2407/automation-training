"""Приклад 2: Значення за замовчуванням та похідні атрибути. Запуск: pytest example_2_defaults.py -v"""


class User:
    def __init__(self, name, active=True):
        self.name = name
        self.active = active


class TestReport:
    def __init__(self, passed, failed):
        self.passed = passed
        self.failed = failed
        self.total = passed + failed
        self.success_rate = passed / self.total if self.total else 0.0


class TestSuite:
    def __init__(self, name, tests=None):
        self.name = name
        self.tests = tests if tests is not None else []


def test_default_active():
    u = User("Alice")
    assert u.active is True


def test_override_default():
    u = User("Bob", active=False)
    assert u.active is False


def test_derived_attributes():
    r = TestReport(passed=8, failed=2)
    assert r.total == 10
    assert r.success_rate == 0.8


def test_mutable_default_is_safe():
    a = TestSuite("smoke")
    b = TestSuite("regression")
    a.tests.append("test_login")
    assert a.tests == ["test_login"]
    assert b.tests == []


def test_init_returns_none():
    u = User("Alice")
    assert User.__init__(u, "Alice") is None
