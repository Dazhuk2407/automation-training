"""Вправа 2: виправ баг. Запуск: pytest exercise_2_fix_methods.py -v

Тести падають — знайди коментар `# BUG:` і виправ його.
"""


class TestCase:
    count = 0

    def __init__(self, title, priority="normal"):
        self.title = title
        self.priority = priority
        TestCase.count += 1

    def is_high_priority(self):
        return self.priority == "high"

    @classmethod
    def from_dict(cls, data):
        # BUG: фабрика ігнорує data["priority"] і завжди бере значення за
        #      замовчуванням "normal". Треба передати priority у конструктор.
        return cls(data["title"])


def test_instance_method():
    tc = TestCase("Login", "high")
    assert tc.is_high_priority() is True

def test_from_dict_title():
    tc = TestCase.from_dict({"title": "Logout", "priority": "low"})
    assert tc.title == "Logout"

def test_from_dict_priority():
    tc = TestCase.from_dict({"title": "Logout", "priority": "high"})
    assert tc.priority == "high"

def test_from_dict_returns_testcase():
    tc = TestCase.from_dict({"title": "Search", "priority": "normal"})
    assert isinstance(tc, TestCase)
