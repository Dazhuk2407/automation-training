"""Вправа 2: виправ помилку. Запуск: pytest exercise_2_fix_patterns.py -v

Патерни нижче написані з помилкою — один тест падає.
Знайди баг у regex (позначений # BUG:) та виправ його.
Після фіксу всі тести мають бути зеленими.
"""
import re


def extract_first_number(text):
    # BUG: \d бере лише ОДНУ цифру, а треба одну або більше (\d+)
    m = re.search(r"\d", text)
    return m.group() if m else None

def is_valid_date(s):
    return re.fullmatch(r"\d{4}-\d{2}-\d{2}", s) is not None

def mask_numbers(text):
    return re.sub(r"\d+", "***", text)


def test_extract_first_number():
    assert extract_first_number("id=42") == "42"

def test_extract_first_number_none():
    assert extract_first_number("no digits") is None

def test_is_valid_date():
    assert is_valid_date("2026-07-26") is True
    assert is_valid_date("26-07-2026") is False

def test_mask_numbers():
    assert mask_numbers("user 42 paid 100") == "user *** paid ***"
