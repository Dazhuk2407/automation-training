"""Вправа 1: базові патерни. Запуск: pytest exercise_1_regex.py -v"""
import re


def find_all_digits(text):
    # TODO: return re.findall(r"\d+", text)
    pass

def extract_error_code(log):
    # TODO: m = re.search(r"error code (\d+)", log); return int(m.group(1)) if m else None
    pass

def is_valid_phone(s):
    # TODO: return re.fullmatch(r"\d{3}-\d{3}-\d{4}", s) is not None
    pass

def test_find_all_digits():
    # TODO: assert find_all_digits("a1 b22 c333") == ["1", "22", "333"]
    pass

def test_find_all_digits_empty():
    # TODO: assert find_all_digits("no digits") == []
    pass

def test_extract_error_code():
    # TODO: assert extract_error_code("failed with error code 500") == 500
    pass

def test_extract_error_code_none():
    # TODO: assert extract_error_code("all ok") is None
    pass

def test_is_valid_phone():
    # TODO: assert is_valid_phone("123-456-7890") is True
    pass
