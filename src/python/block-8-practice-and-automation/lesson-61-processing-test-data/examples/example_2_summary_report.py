"""Приклад 2: підрахунок + summary-рядок. Запуск: pytest example_2_summary_report.py -v"""


def count_status(lines, status):
    return sum(1 for ln in lines if ln.strip().split()[-1] == status)

def pass_rate(lines):
    total = len(lines)
    if total == 0:
        return 0.0
    return count_status(lines, "PASSED") / total

def summary_line(lines):
    total = len(lines)
    passed = count_status(lines, "PASSED")
    rate = (passed / total * 100) if total else 0.0
    return f"PASSED: {passed}/{total} ({rate:.1f}%)"

def test_count_status():
    logs = ["test_a PASSED", "test_b FAILED", "test_c PASSED"]
    assert count_status(logs, "PASSED") == 2
    assert count_status(logs, "FAILED") == 1

def test_pass_rate():
    logs = ["test_a PASSED", "test_b FAILED", "test_c PASSED", "test_d PASSED"]
    assert pass_rate(logs) == 0.75

def test_pass_rate_empty():
    assert pass_rate([]) == 0.0

def test_summary_line():
    logs = ["test_a PASSED", "test_b FAILED", "test_c PASSED", "test_d PASSED"]
    assert summary_line(logs) == "PASSED: 3/4 (75.0%)"

def test_summary_line_empty():
    assert summary_line([]) == "PASSED: 0/0 (0.0%)"
