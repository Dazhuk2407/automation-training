"""Вправа 1: Constructor (__init__). Запуск: pytest exercise_1_init.py -v"""


class User:
    def __init__(self, name, role):
        # TODO: self.name = name
        # TODO: self.role = role
        pass


class ApiClient:
    def __init__(self, base_url, timeout=30):
        # TODO: self.base_url = base_url
        # TODO: self.timeout = timeout
        pass


class TestReport:
    def __init__(self, passed, failed):
        # TODO: self.passed = passed
        # TODO: self.failed = failed
        # TODO: self.total = passed + failed
        pass


def test_user_attributes():
    # TODO:
    #   u = User("Alice", "admin")
    #   assert u.name == "Alice"
    #   assert u.role == "admin"
    pass


def test_client_default_timeout():
    # TODO:
    #   client = ApiClient("https://api.example.com")
    #   assert client.timeout == 30
    pass


def test_client_custom_timeout():
    # TODO:
    #   client = ApiClient("https://api.example.com", timeout=60)
    #   assert client.timeout == 60
    pass


def test_report_total():
    # TODO:
    #   r = TestReport(8, 2)
    #   assert r.total == 10
    pass


def test_report_stores_values():
    # TODO:
    #   r = TestReport(8, 2)
    #   assert r.passed == 8
    #   assert r.failed == 2
    pass
