"""Приклад 1: Базові f-strings та вирази. Запуск: pytest example_1_basics.py -v"""


def greet(name):
    return f"Hello {name}"

def shout(name):
    return f"{name.upper()}!"

def get_field(user, key):
    return f"{user[key]}"

def add_label(a, b):
    return f"sum = {a + b}"

def test_greet():
    assert greet("Alice") == "Hello Alice"

def test_shout():
    assert shout("alice") == "ALICE!"

def test_get_field():
    user = {"name": "Bob", "role": "admin"}
    assert get_field(user, "name") == "Bob"
    assert get_field(user, "role") == "admin"

def test_add_label():
    assert add_label(2, 2) == "sum = 4"

def test_method_call_inside():
    name = "qa"
    assert f"{name.upper()} ({len(name)})" == "QA (2)"
