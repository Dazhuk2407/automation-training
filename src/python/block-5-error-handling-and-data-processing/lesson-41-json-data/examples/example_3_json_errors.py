"""Приклад 3: обробка JSONDecodeError. Запуск: pytest example_3_json_errors.py -v"""
import json


def safe_parse(raw):
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None

def parse_or_default(raw, default):
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return default

def is_valid_json(raw):
    try:
        json.loads(raw)
        return True
    except json.JSONDecodeError:
        return False

def test_safe_parse_valid():
    assert safe_parse('{"ok": true}') == {"ok": True}

def test_safe_parse_invalid():
    assert safe_parse('{broken}') is None

def test_single_quotes_invalid():
    # JSON вимагає подвійні лапки
    assert safe_parse("{'name': 'Alice'}") is None

def test_python_true_invalid():
    # True з великої — це Python, не JSON
    assert safe_parse('{"active": True}') is None

def test_parse_or_default():
    assert parse_or_default('not json', {}) == {}
    assert parse_or_default('[1, 2]', {}) == [1, 2]

def test_is_valid_json():
    assert is_valid_json('{"a": 1}') is True
    assert is_valid_json('{"a": }') is False

def test_decode_error_is_valueerror():
    # JSONDecodeError — підклас ValueError
    try:
        json.loads('{oops}')
    except ValueError:
        caught = True
    assert caught is True
