"""Приклад 2: рівні логування. Запуск: pytest example_2_levels.py -v"""
import logging

LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def order_index(name):
    return LEVELS.index(name)

def is_more_severe(a, b):
    return logging.getLevelName(a) > logging.getLevelName(b)

def should_log(msg_level, min_level):
    return logging.getLevelName(msg_level) >= logging.getLevelName(min_level)

def test_order():
    assert order_index("DEBUG") == 0
    assert order_index("CRITICAL") == 4

def test_is_more_severe():
    assert is_more_severe("ERROR", "INFO") is True
    assert is_more_severe("DEBUG", "WARNING") is False

def test_should_log():
    assert should_log("ERROR", "WARNING") is True
    assert should_log("INFO", "WARNING") is False

def test_levels_ascending():
    values = [logging.getLevelName(n) for n in LEVELS]
    assert values == sorted(values)
