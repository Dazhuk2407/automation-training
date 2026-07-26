"""Приклад 3: Рядки для звітів та логів у тестах. Запуск: pytest example_3_qa_reports.py -v"""


def format_result(passed, total):
    ratio = passed / total
    return f"PASSED: {passed}/{total} ({ratio:.1%})"

def format_log(level, message):
    return f"[{level:^7}] {message}"

def format_duration(name, seconds):
    return f"{name}: {seconds:.2f}s"

def format_row(name, status):
    return f"{name:<12}{status:>6}"

def test_format_result():
    assert format_result(8, 10) == "PASSED: 8/10 (80.0%)"
    assert format_result(10, 10) == "PASSED: 10/10 (100.0%)"

def test_format_log():
    assert format_log("INFO", "start") == "[ INFO  ] start"
    assert format_log("ERROR", "boom") == "[ ERROR ] boom"

def test_format_duration():
    assert format_duration("login_test", 1.2) == "login_test: 1.20s"

def test_format_row():
    assert format_row("login", "PASS") == "login         PASS"

def test_price_literal():
    assert f"{19.5:.2f}" == "19.50"
