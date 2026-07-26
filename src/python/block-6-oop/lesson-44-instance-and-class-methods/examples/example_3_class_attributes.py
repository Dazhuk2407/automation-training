"""Приклад 3: атрибути класу vs екземпляра, лічильник. Запуск: pytest example_3_class_attributes.py -v"""


class TestCase:
    count = 0  # атрибут класу — спільний для всіх

    def __init__(self, title):
        self.title = title  # атрибут екземпляра — свій у кожного
        TestCase.count += 1


class Config:
    def __init__(self):
        self.tags = []  # атрибут екземпляра — свій у кожного

    def add_tag(self, tag):
        self.tags.append(tag)


def test_counter_is_shared():
    TestCase.count = 0
    tc1 = TestCase("Login")
    tc2 = TestCase("Logout")
    assert TestCase.count == 2
    assert tc1.count == 2
    assert tc2.count == 2

def test_instance_attributes_are_own():
    TestCase.count = 0
    tc1 = TestCase("Login")
    tc2 = TestCase("Logout")
    assert tc1.title == "Login"
    assert tc2.title == "Logout"

def test_instance_tags_are_independent():
    a = Config()
    b = Config()
    a.add_tag("smoke")
    assert a.tags == ["smoke"]
    assert b.tags == []

def test_access_class_attribute_via_name():
    TestCase.count = 0
    TestCase("A")
    assert TestCase.count == 1

def test_shadowing_does_not_touch_class():
    TestCase.count = 0
    tc = TestCase("A")
    tc.count = 999  # створює атрибут екземпляра, не чіпає клас
    assert tc.count == 999
    assert TestCase.count == 1
