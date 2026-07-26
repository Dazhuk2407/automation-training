"""Вправа 1: основи HTTP. Запуск: pytest exercise_1_api.py -v"""
import os


def status_class(code):
    # TODO: return f"{code // 100}xx"
    pass

def is_success(code):
    # TODO: return 200 <= code < 300
    pass

def build_auth_header():
    # TODO: token = os.getenv("API_TOKEN", ""); return {"Authorization": f"Bearer {token}"}
    pass

def test_status_class_2xx():
    # TODO: assert status_class(200) == "2xx"
    pass

def test_status_class_4xx():
    # TODO: assert status_class(404) == "4xx"
    pass

def test_is_success_true():
    # TODO: assert is_success(201) is True
    pass

def test_is_success_false():
    # TODO: assert is_success(500) is False
    pass

def test_build_auth_header(monkeypatch):
    # TODO: monkeypatch.setenv("API_TOKEN", "abc"); assert build_auth_header() == {"Authorization": "Bearer abc"}
    pass
