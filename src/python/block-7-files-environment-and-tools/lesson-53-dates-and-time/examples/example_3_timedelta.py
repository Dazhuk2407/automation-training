"""Приклад 3: timedelta. Запуск: pytest example_3_timedelta.py -v"""
from datetime import datetime, date, timedelta


def days_between(d1, d2):
    return (d2 - d1).days

def add_days(dt, n):
    return dt + timedelta(days=n)

def subtract_days(dt, n):
    return dt - timedelta(days=n)

def duration_seconds(start, end):
    return (end - start).total_seconds()

def log_filename(dt):
    return f"test_run_{dt.strftime('%Y-%m-%d_%H-%M-%S')}.log"


def test_days_between():
    assert days_between(date(2024, 1, 1), date(2024, 1, 8)) == 7

def test_add_days():
    dt = datetime(2024, 1, 15, 10, 0, 0)
    assert add_days(dt, 7) == datetime(2024, 1, 22, 10, 0, 0)

def test_subtract_days():
    dt = datetime(2024, 1, 15, 10, 0, 0)
    assert subtract_days(dt, 1) == datetime(2024, 1, 14, 10, 0, 0)

def test_duration_seconds():
    start = datetime(2024, 1, 15, 10, 0, 0)
    end = datetime(2024, 1, 15, 10, 0, 45)
    assert duration_seconds(start, end) == 45.0

def test_log_filename():
    dt = datetime(2024, 1, 15, 10, 30, 0)
    assert log_filename(dt) == "test_run_2024-01-15_10-30-00.log"
