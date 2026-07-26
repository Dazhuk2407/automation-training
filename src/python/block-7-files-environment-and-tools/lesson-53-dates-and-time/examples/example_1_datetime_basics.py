"""Приклад 1: створення дат і атрибути. Запуск: pytest example_1_datetime_basics.py -v"""
from datetime import datetime, date


def make_datetime(year, month, day, hour, minute):
    return datetime(year, month, day, hour, minute)

def make_date(year, month, day):
    return date(year, month, day)

def get_year(dt):
    return dt.year

def get_weekday(dt):
    return dt.weekday()

def now_is_datetime():
    return isinstance(datetime.now(), datetime)


def test_make_datetime():
    dt = make_datetime(2024, 1, 15, 10, 30)
    assert dt.year == 2024
    assert dt.month == 1
    assert dt.day == 15
    assert dt.hour == 10
    assert dt.minute == 30

def test_make_date():
    d = make_date(2024, 1, 15)
    assert d == date(2024, 1, 15)

def test_get_year():
    assert get_year(datetime(2024, 1, 15, 10, 30, 0)) == 2024

def test_get_weekday():
    # 15.01.2024 — понеділок → 0
    assert get_weekday(date(2024, 1, 15)) == 0

def test_now_is_datetime():
    # не порівнюємо значення now() — лише тип
    assert now_is_datetime() is True
