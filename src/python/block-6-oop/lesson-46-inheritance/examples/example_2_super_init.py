"""Приклад 2: super().__init__(). Запуск: pytest example_2_super_init.py -v"""


class BasePage:
    def __init__(self, url):
        self.url = url

    def open(self):
        return f"GET {self.url}"


class LoginPage(BasePage):
    def __init__(self, url, username):
        super().__init__(url)
        self.username = username

    def login(self):
        return f"{self.username} -> {self.open()}"


def test_super_sets_parent_attribute():
    page = LoginPage("/login", "alice")
    assert page.url == "/login"

def test_child_adds_own_attribute():
    page = LoginPage("/login", "alice")
    assert page.username == "alice"

def test_child_uses_parent_method():
    page = LoginPage("/login", "alice")
    assert page.open() == "GET /login"
    assert page.login() == "alice -> GET /login"

def test_login_page_is_base_page():
    page = LoginPage("/login", "alice")
    assert isinstance(page, BasePage)
    assert isinstance(page, LoginPage)
