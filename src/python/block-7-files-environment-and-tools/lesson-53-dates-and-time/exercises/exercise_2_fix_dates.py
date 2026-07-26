"""Вправа 2: знайди й виправ баг. Запуск: pytest exercise_2_fix_dates.py -v

Один з тестів падає через баг у коді (позначено `# BUG:`).
Знайди його, виправ — і всі тести стануть зеленими.
"""
from datetime import datetime, date, timedelta


def format_iso(dt):
    # BUG: невірний формат-код — має бути "%Y-%m-%d", а не "%m-%d-%Y"
    return dt.strftime("%m-%d-%Y")

def parse_iso(text):
    return datetime.strptime(text, "%Y-%m-%d")

def next_week(dt):
    return dt + timedelta(days=7)

def days_between(d1, d2):
    return (d2 - d1).days


def test_format_iso():
    dt = datetime(2024, 1, 15, 10, 30, 0)
    assert format_iso(dt) == "2024-01-15"

def test_parse_iso():
    assert parse_iso("2024-01-15") == datetime(2024, 1, 15, 0, 0, 0)

def test_next_week():
    dt = datetime(2024, 1, 15, 10, 0, 0)
    assert next_week(dt) == datetime(2024, 1, 22, 10, 0, 0)

def test_days_between():
    assert days_between(date(2024, 1, 1), date(2024, 1, 8)) == 7
