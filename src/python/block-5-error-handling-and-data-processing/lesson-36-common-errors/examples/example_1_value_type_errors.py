"""Приклад 1: ValueError та TypeError. Запуск: pytest example_1_value_type_errors.py -v"""

import pytest


def safe_int(text, default=0):
    """Парсинг числа з рядка без падіння на ValueError."""
    try:
        return int(text)
    except (ValueError, TypeError):
        return default


def parse_status_code(response):
    """Дістати числовий код статусу з поля API-відповіді."""
    return int(response["code"])


def test_value_error():
    # правильний тип (str), але значення не є числом
    with pytest.raises(ValueError):
        int("abc")


def test_type_error_concat():
    # несумісні типи: str + int
    with pytest.raises(TypeError):
        "a" + 1


def test_type_error_len():
    # int не має довжини
    with pytest.raises(TypeError):
        len(5)


def test_safe_int():
    assert safe_int("42") == 42
    assert safe_int("abc") == 0
    assert safe_int(None) == 0
    assert safe_int("bad", default=-1) == -1


def test_parse_status_code():
    assert parse_status_code({"code": "200"}) == 200
    with pytest.raises(ValueError):
        parse_status_code({"code": "OK"})
