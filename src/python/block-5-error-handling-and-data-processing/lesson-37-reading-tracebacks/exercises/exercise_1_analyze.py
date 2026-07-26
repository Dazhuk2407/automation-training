"""Вправа 1: аналіз traceback. Запуск: pytest exercise_1_analyze.py -v"""
import traceback


def get_error_type(func):
    # TODO: викликати func у try/except; повернути type(exc).__name__
    pass

def capture_message(func):
    # TODO: у except повернути traceback.format_exc()
    pass

def last_line(func):
    # TODO: повернути останній рядок traceback: format_exc().strip().splitlines()[-1]
    pass

def test_error_type():
    # TODO: assert get_error_type(lambda: 1 / 0) == "ZeroDivisionError"
    pass

def test_error_type_key():
    # TODO: assert get_error_type(lambda: {}["x"]) == "KeyError"
    pass

def test_capture_contains_type():
    # TODO: assert "ZeroDivisionError" in capture_message(lambda: 1 / 0)
    pass

def test_capture_contains_traceback_header():
    # TODO: assert "Traceback" in capture_message(lambda: 1 / 0)
    pass

def test_last_line():
    # TODO: assert last_line(lambda: 1 / 0) == "ZeroDivisionError: division by zero"
    pass
