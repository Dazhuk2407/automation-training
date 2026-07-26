"""Приклад 2: метасимволи, квантифікатори, класи, findall, sub.
Запуск: pytest example_2_patterns.py -v"""
import re


def extract_numbers(text):
    return re.findall(r"\d+", text)

def extract_words(text):
    return re.findall(r"[a-z]+", text)

def has_three_digits(text):
    return re.search(r"\d{3}", text) is not None

def mask_numbers(text):
    return re.sub(r"\d+", "***", text)

def squeeze_spaces(text):
    return re.sub(r"\s+", " ", text)


def test_extract_numbers():
    assert extract_numbers("a1 b22 c333") == ["1", "22", "333"]
    assert extract_numbers("no digits") == []

def test_extract_words():
    assert extract_words("aB2c de") == ["a", "c", "de"]

def test_has_three_digits():
    assert has_three_digits("code=500") is True
    assert has_three_digits("code=50") is False

def test_mask_numbers():
    assert mask_numbers("user 42 paid 100") == "user *** paid ***"

def test_squeeze_spaces():
    assert squeeze_spaces("a   b\t c") == "a b c"
