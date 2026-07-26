"""Приклад 1: читання traceback. Запуск: pytest example_1_read_traceback.py -v"""
import traceback


def capture_zero_division():
    try:
        return 1 / 0
    except ZeroDivisionError:
        return traceback.format_exc()


def capture_key_error():
    data = {"name": "Alice"}
    try:
        return data["age"]
    except KeyError:
        return traceback.format_exc()


def last_line(tb_text):
    """Останній рядок traceback = 'тип: повідомлення'."""
    return tb_text.strip().splitlines()[-1]


def test_capture_contains_type():
    assert "ZeroDivisionError" in capture_zero_division()


def test_capture_contains_message():
    assert "division by zero" in capture_zero_division()


def test_last_line_is_type_and_message():
    assert last_line(capture_zero_division()) == "ZeroDivisionError: division by zero"


def test_capture_contains_function_name():
    # у стеку є ім'я функції, де стався виняток
    assert "capture_zero_division" in capture_zero_division()


def test_key_error_last_line():
    assert last_line(capture_key_error()) == "KeyError: 'age'"
