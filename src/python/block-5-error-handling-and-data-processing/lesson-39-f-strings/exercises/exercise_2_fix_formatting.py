"""Вправа 2: Виправ помилку. Запуск: pytest exercise_2_fix_formatting.py -v

Тести падають, бо один зі специфікаторів форматування неправильний.
Знайди функцію з коментарем # BUG і виправ специфікатор, щоб тести стали зелені.
"""


def format_price(value):
    # BUG: :.1f дає лише 1 знак після коми замість 2
    return f"{value:.1f}"

def format_pass_rate(passed, total):
    ratio = passed / total
    return f"{ratio:.1%}"

def format_row(name, status):
    return f"{name:<10}{status:>6}"

def test_price():
    assert format_price(19.5) == "19.50"

def test_pass_rate():
    assert format_pass_rate(8, 10) == "80.0%"

def test_row_status():
    assert format_row("login", "PASS") == "login       PASS"

def test_row_fail():
    assert format_row("logout", "FAIL") == "logout      FAIL"
