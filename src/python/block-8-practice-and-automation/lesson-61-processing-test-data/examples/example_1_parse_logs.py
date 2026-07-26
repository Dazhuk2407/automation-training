"""Приклад 1: парсинг лог-рядків у dict. Запуск: pytest example_1_parse_logs.py -v"""


def parse_line(line):
    date, level, test, status = line.strip().split()
    return {"date": date, "level": level, "test": test, "status": status}

def get_status(line):
    return line.strip().split()[-1]

def get_level(line):
    return line.strip().split()[1]

def parse_all(lines):
    return [parse_line(ln) for ln in lines]

def test_parse_line():
    result = parse_line("2024-01-15 INFO test_login PASSED")
    assert result == {
        "date": "2024-01-15",
        "level": "INFO",
        "test": "test_login",
        "status": "PASSED",
    }

def test_parse_line_strips():
    result = parse_line("  2024-01-15 ERROR test_pay FAILED\n")
    assert result["status"] == "FAILED"
    assert result["level"] == "ERROR"

def test_get_status():
    assert get_status("2024-01-15 INFO test_a PASSED") == "PASSED"
    assert get_status("2024-01-15 INFO test_b FAILED") == "FAILED"

def test_get_level():
    assert get_level("2024-01-15 WARNING test_c PASSED") == "WARNING"

def test_parse_all():
    logs = [
        "2024-01-15 INFO test_a PASSED",
        "2024-01-15 INFO test_b FAILED",
    ]
    parsed = parse_all(logs)
    assert len(parsed) == 2
    assert parsed[0]["test"] == "test_a"
    assert parsed[1]["status"] == "FAILED"
