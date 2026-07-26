"""Вправа 2: знайди та виправ помилку.

ДЕЯКІ тести нижче падають через навмисну помилку у коді функцій.
Знайди рядок з коментарем `# BUG:` та виправ його, щоб УСІ тести стали зелені.
Запуск: pytest exercise_2_finally.py -v
"""


def safe_divide(a, b):
    try:
        return a / b
    # BUG: тут ловиться не той виняток — при діленні на 0 буде ZeroDivisionError,
    # а не ValueError, тому дефолт не спрацьовує. Заміни на потрібний.
    except ValueError:
        return 0.0


def with_cleanup(data):
    log = []
    try:
        log.append("start")
        if not data:
            raise ValueError("empty")
        log.append("work")
    except ValueError:
        log.append("error")
    finally:
        log.append("cleanup")
    return log


def parse_or_default(value, default=0):
    try:
        return int(value)
    except ValueError:
        return default


def test_safe_divide_ok():
    assert safe_divide(10, 2) == 5.0


def test_safe_divide_zero():
    # цей тест падає, поки не виправлено BUG
    assert safe_divide(10, 0) == 0.0


def test_with_cleanup():
    assert with_cleanup([1]) == ["start", "work", "cleanup"]
    assert with_cleanup([]) == ["start", "error", "cleanup"]


def test_parse_or_default():
    assert parse_or_default("42") == 42
    assert parse_or_default("bad", -1) == -1
