"""Приклад 1: search / match / fullmatch. Запуск: pytest example_1_search_match.py -v"""
import re


def find_number(text):
    m = re.search(r"\d+", text)
    return m.group() if m else None

def starts_with_digits(text):
    return re.match(r"\d+", text) is not None

def is_all_digits(text):
    return re.fullmatch(r"\d+", text) is not None


def test_find_number():
    assert find_number("id=42") == "42"
    assert find_number("abc123def") == "123"
    assert find_number("no digits") is None

def test_starts_with_digits():
    assert starts_with_digits("123abc") is True
    assert starts_with_digits("abc123") is False

def test_is_all_digits():
    assert is_all_digits("123") is True
    assert is_all_digits("123abc") is False
    assert is_all_digits("") is False
