"""Приклад 3: групи () та валідація/витяг у QA.
Запуск: pytest example_3_groups_qa.py -v"""
import re


def is_valid_email(s):
    return re.fullmatch(r"[\w.]+@[\w.]+\.\w+", s) is not None

def is_valid_phone(s):
    return re.fullmatch(r"\d{3}-\d{3}-\d{4}", s) is not None

def is_valid_date(s):
    return re.fullmatch(r"\d{4}-\d{2}-\d{2}", s) is not None

def extract_test_id(log):
    m = re.search(r"TEST-(\d+)", log)
    return m.group(1) if m else None

def extract_error_code(log):
    m = re.search(r"error code (\d+)", log)
    return int(m.group(1)) if m else None

def parse_pairs(text):
    return re.findall(r"(\w+)=(\d+)", text)


def test_is_valid_email():
    assert is_valid_email("a@b.com") is True
    assert is_valid_email("qa.user@example.com") is True
    assert is_valid_email("bad") is False

def test_is_valid_phone():
    assert is_valid_phone("123-456-7890") is True
    assert is_valid_phone("1234567890") is False

def test_is_valid_date():
    assert is_valid_date("2026-07-26") is True
    assert is_valid_date("26-07-2026") is False

def test_extract_test_id():
    assert extract_test_id("Run TEST-42 failed") == "42"
    assert extract_test_id("no id here") is None

def test_extract_error_code():
    assert extract_error_code("failed with error code 500") == 500
    assert extract_error_code("ok") is None

def test_parse_pairs():
    assert parse_pairs("a=1 b=2") == [("a", "1"), ("b", "2")]
