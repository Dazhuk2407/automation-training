"""Приклад 3: else та finally. Запуск: pytest example_3_else_finally.py -v"""


def read_config(raw):
    try:
        value = int(raw)
    except ValueError:
        return "parse error"
    else:
        return f"ok: {value}"

def process_resource(data):
    log = []
    try:
        log.append("open")
        if not data:
            raise ValueError("empty")
        log.append("process")
    except ValueError:
        log.append("error")
    finally:
        log.append("close")
    return log

def get_status_code(response, default=500):
    try:
        return int(response["status"])
    except (KeyError, ValueError, TypeError):
        return default

def test_read_config():
    assert read_config("8080") == "ok: 8080"
    assert read_config("bad") == "parse error"

def test_process_resource_ok():
    assert process_resource([1]) == ["open", "process", "close"]

def test_process_resource_error():
    assert process_resource([]) == ["open", "error", "close"]

def test_get_status_code():
    assert get_status_code({"status": "200"}) == 200
    assert get_status_code({}) == 500
    assert get_status_code({"status": "oops"}) == 500
    assert get_status_code(None) == 500
