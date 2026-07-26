"""Приклад 3: override, isinstance/issubclass. Запуск: pytest example_3_override.py -v"""


class BaseTest:
    def name(self):
        return "base"

    def describe(self):
        return f"test={self.name()}"


class LoginTest(BaseTest):
    def name(self):
        return "login"


class SmokeTest(BaseTest):
    def describe(self):
        base = super().describe()
        return f"[SMOKE] {base}"


def test_override_replaces_method():
    assert BaseTest().name() == "base"
    assert LoginTest().name() == "login"

def test_override_affects_inherited_method():
    # describe() не перевизначений, але викликає перевизначений name()
    assert LoginTest().describe() == "test=login"

def test_super_extends_method():
    assert SmokeTest().describe() == "[SMOKE] test=base"

def test_isinstance_and_issubclass():
    login = LoginTest()
    assert isinstance(login, BaseTest)
    assert issubclass(LoginTest, BaseTest)
    assert not issubclass(BaseTest, LoginTest)
