"""Приклад 2: модуль traceback. Запуск: pytest example_2_traceback_module.py -v"""
import traceback


def safe_run(func):
    """Виконати func; при винятку повернути traceback як рядок (логування)."""
    try:
        return func()
    except Exception:
        return traceback.format_exc()


def exception_type_name(func):
    """Повернути ім'я типу винятку, що кинула func."""
    try:
        func()
    except Exception as exc:
        return type(exc).__name__
    return None


def format_last_line(func):
    """Повернути останній рядок traceback: 'Тип: меседж'."""
    try:
        func()
    except Exception:
        return traceback.format_exc().strip().splitlines()[-1]


def _boom():
    raise ValueError("bad input")


def test_safe_run_returns_traceback_text():
    result = safe_run(_boom)
    assert "Traceback (most recent call last)" in result


def test_safe_run_contains_type_and_message():
    result = safe_run(_boom)
    assert "ValueError: bad input" in result


def test_exception_type_name():
    assert exception_type_name(_boom) == "ValueError"


def test_format_last_line():
    assert format_last_line(_boom) == "ValueError: bad input"


def test_no_exception_returns_value():
    assert safe_run(lambda: 42) == 42
