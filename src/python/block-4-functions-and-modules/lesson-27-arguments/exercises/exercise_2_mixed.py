"""
Вправа 2: Змішування аргументів.
Запуск: pytest exercise_2_mixed.py -v
"""


def make_request(method, url, timeout=30):
    return {"method": method, "url": url, "timeout": timeout}


def test_mixed_call():
    # TODO: замініть pass на:
    #   req = make_request("GET", "/api", timeout=60)
    #   assert req["method"] == "GET"
    #   assert req["timeout"] == 60
    pass

def test_default_used():
    # TODO: замініть pass на:
    #   req = make_request("GET", "/api")
    #   assert req["timeout"] == 30
    pass

def test_override_default():
    # TODO: замініть pass на:
    #   req = make_request("POST", "/api", timeout=120)
    #   assert req["timeout"] == 120
    pass