"""Приклад 3: __init__ у QA (TestUser, ApiClient). Запуск: pytest example_3_qa_objects.py -v"""


class TestUser:
    def __init__(self, name, role, active=True):
        self.name = name
        self.role = role
        self.active = active


class ApiClient:
    def __init__(self, base_url, timeout=30):
        self.base_url = base_url
        self.timeout = timeout
        self.session_headers = {"Accept": "application/json"}


class TestCase:
    def __init__(self, test_id, title, priority="medium"):
        self.test_id = test_id
        self.title = title
        self.priority = priority
        self.status = "not_run"


def test_test_user_defaults():
    user = TestUser("Alice", "admin")
    assert user.name == "Alice"
    assert user.role == "admin"
    assert user.active is True


def test_test_user_inactive():
    user = TestUser("Bob", "guest", active=False)
    assert user.active is False


def test_api_client_default_timeout():
    client = ApiClient("https://api.example.com")
    assert client.base_url == "https://api.example.com"
    assert client.timeout == 30
    assert client.session_headers == {"Accept": "application/json"}


def test_api_client_custom_timeout():
    client = ApiClient("https://api.example.com", timeout=60)
    assert client.timeout == 60


def test_test_case_initial_status():
    case = TestCase("TC-001", "Login works")
    assert case.test_id == "TC-001"
    assert case.priority == "medium"
    assert case.status == "not_run"
