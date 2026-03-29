"""
Приклад 1: Default параметри.
Запуск: pytest example_1_defaults.py -v
"""


def make_request(method, url, timeout=30, verify=True):
    return {"method": method, "url": url, "timeout": timeout, "verify": verify}


def test_all_defaults():
    req = make_request("GET", "/api")
    assert req["timeout"] == 30
    assert req["verify"] is True


def test_override_one():
    req = make_request("GET", "/api", timeout=60)
    assert req["timeout"] == 60
    assert req["verify"] is True


def test_override_all():
    req = make_request("POST", "/api", timeout=5, verify=False)
    assert req["timeout"] == 5
    assert req["verify"] is False


def test_skip_middle_default():
    """Пропустити timeout, задати verify через keyword."""
    req = make_request("GET", "/api", verify=False)
    assert req["timeout"] == 30
    assert req["verify"] is False