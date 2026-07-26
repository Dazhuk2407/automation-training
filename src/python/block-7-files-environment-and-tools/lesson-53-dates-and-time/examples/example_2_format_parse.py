"""Приклад 2: strftime та strptime. Запуск: pytest example_2_format_parse.py -v"""
from datetime import datetime


def format_date(dt):
    return dt.strftime("%Y-%m-%d")

def format_time(dt):
    return dt.strftime("%H:%M:%S")

def format_full(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def parse_date(text):
    return datetime.strptime(text, "%Y-%m-%d")

def parse_full(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M:%S")


def test_format_date():
    dt = datetime(2024, 1, 15, 10, 30, 0)
    assert format_date(dt) == "2024-01-15"

def test_format_time():
    dt = datetime(2024, 1, 15, 10, 30, 0)
    assert format_time(dt) == "10:30:00"

def test_format_full():
    dt = datetime(2024, 1, 15, 10, 30, 0)
    assert format_full(dt) == "2024-01-15 10:30:00"

def test_parse_date():
    assert parse_date("2024-01-15") == datetime(2024, 1, 15, 0, 0, 0)

def test_parse_full():
    assert parse_full("2024-01-15 10:30:00") == datetime(2024, 1, 15, 10, 30, 0)

def test_roundtrip():
    dt = datetime(2024, 1, 15, 0, 0, 0)
    assert parse_date(format_date(dt)) == dt
