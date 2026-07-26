"""Вправа 1: дати й час. Запуск: pytest exercise_1_dates.py -v"""
from datetime import datetime, date, timedelta


def format_date(dt):
    # TODO: return dt.strftime("%Y-%m-%d")
    pass

def parse_date(text):
    # TODO: return datetime.strptime(text, "%Y-%m-%d")
    pass

def days_between(d1, d2):
    # TODO: return (d2 - d1).days
    pass

def test_format_date():
    # TODO: assert format_date(datetime(2024, 1, 15, 10, 30, 0)) == "2024-01-15"
    pass

def test_parse_date():
    # TODO: assert parse_date("2024-01-15") == datetime(2024, 1, 15, 0, 0, 0)
    pass

def test_days_between():
    # TODO: assert days_between(date(2024, 1, 1), date(2024, 1, 8)) == 7
    pass

def test_days_between_same():
    # TODO: assert days_between(date(2024, 1, 1), date(2024, 1, 1)) == 0
    pass

def test_roundtrip():
    # TODO: assert format_date(parse_date("2024-01-15")) == "2024-01-15"
    pass
