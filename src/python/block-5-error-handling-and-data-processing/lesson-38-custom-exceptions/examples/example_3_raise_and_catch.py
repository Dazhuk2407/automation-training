"""Приклад 3: ловля, повідомлення та кастомні атрибути у QA. Запуск: pytest example_3_raise_and_catch.py -v"""

import pytest


class TestDataError(Exception):
    """Некоректні вхідні тестові дані."""
    pass


class ApiResponseError(Exception):
    """Неочікувана відповідь від API з кодом статусу."""

    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code


def load_user(data):
    if "id" not in data:
        raise TestDataError("user fixture missing 'id'")
    return data


def check_status(response):
    if response["status"] != 200:
        raise ApiResponseError(f"unexpected status {response['status']}", response["status"])
    return response


def test_load_user_ok():
    assert load_user({"id": 1}) == {"id": 1}


def test_load_user_raises():
    with pytest.raises(TestDataError, match="missing 'id'"):
        load_user({"name": "Alice"})


def test_check_status_ok():
    response = {"status": 200}
    assert check_status(response) == response


def test_api_error_message():
    with pytest.raises(ApiResponseError, match="unexpected status 404"):
        check_status({"status": 404})


def test_api_error_attribute():
    try:
        check_status({"status": 500})
    except ApiResponseError as e:
        assert e.status_code == 500
        assert str(e) == "unexpected status 500"
