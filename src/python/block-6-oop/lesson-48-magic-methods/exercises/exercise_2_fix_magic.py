"""Вправа 2: Виправити баг у magic-методі. Запуск: pytest exercise_2_fix_magic.py -v

Тести нижче падають — рівно один. Знайдіть рядок з коментарем `# BUG:`
і виправте його, щоб усі 4 тести проходили.
"""


class TestResult:
    def __init__(self, name, passed):
        self.name = name
        self.passed = passed

    def __str__(self):
        status = "PASS" if self.passed else "FAIL"
        return f"{self.name}: {status}"

    def __eq__(self, other):
        # BUG: порівнює тільки name та ігнорує passed —
        #      два результати з різним статусом вважаються рівними.
        #      Треба порівнювати обидва поля:
        #      return self.name == other.name and self.passed == other.passed
        return self.name == other.name

    def __repr__(self):
        return f"TestResult({self.name!r}, {self.passed})"


def test_str_pass():
    assert str(TestResult("test_login", True)) == "test_login: PASS"

def test_str_fail():
    assert str(TestResult("test_logout", False)) == "test_logout: FAIL"

def test_eq_same():
    assert TestResult("test_login", True) == TestResult("test_login", True)

def test_eq_status_matters():
    assert TestResult("test_login", True) != TestResult("test_login", False)
