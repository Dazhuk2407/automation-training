"""Вправа 1: Функції з default значеннями. Запуск: pytest exercise_1_defaults.py -v"""


def greet(name, greeting="Hello"):
    # TODO: замініть pass на: return f"{greeting}, {name}!"
    pass

def make_config(host, port=8080, debug=False):
    # TODO: замініть pass на: return {"host": host, "port": port, "debug": debug}
    pass

def test_greet_default():
    # TODO: замініть pass на: assert greet("Alice") == "Hello, Alice!"
    pass

def test_greet_custom():
    # TODO: замініть pass на: assert greet("Bob", greeting="Hi") == "Hi, Bob!"
    pass

def test_config_default():
    # TODO: замініть pass на:
    #   c = make_config("localhost")
    #   assert c == {"host": "localhost", "port": 8080, "debug": False}
    pass

def test_config_custom():
    # TODO: замініть pass на:
    #   c = make_config("prod", port=443, debug=True)
    #   assert c["port"] == 443
    pass