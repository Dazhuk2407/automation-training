"""Приклад 1: основи HTTP як чисті функції. Запуск: pytest example_1_http_basics.py -v"""


def status_class(code):
    return f"{code // 100}xx"

def is_success(code):
    return 200 <= code < 300

def is_client_error(code):
    return 400 <= code < 500

def method_is_safe(method):
    return method.upper() in {"GET", "HEAD", "OPTIONS"}

def test_status_class():
    assert status_class(200) == "2xx"
    assert status_class(404) == "4xx"
    assert status_class(503) == "5xx"

def test_is_success():
    assert is_success(200) is True
    assert is_success(201) is True
    assert is_success(404) is False

def test_is_client_error():
    assert is_client_error(400) is True
    assert is_client_error(404) is True
    assert is_client_error(500) is False

def test_method_is_safe():
    assert method_is_safe("GET") is True
    assert method_is_safe("get") is True
    assert method_is_safe("POST") is False
