"""Вправа 2: знайди та виправ баг.

У функції нижче є рядок з поміткою `# BUG:`.
Через нього один із тестів падає. Знайди помилку, виправ її,
і переконайся що всі 4 тести проходять: pytest exercise_2_fix_report.py -v
"""


def count_status(lines, status):
    return sum(1 for ln in lines if ln.strip().split()[-1] == status)

def pass_rate(lines):
    total = len(lines)
    if total == 0:
        return 0.0
    passed = count_status(lines, "PASSED")
    return passed / passed  # BUG: ділить на passed замість total

def summary_line(lines):
    total = len(lines)
    passed = count_status(lines, "PASSED")
    rate = (passed / total * 100) if total else 0.0
    return f"PASSED: {passed}/{total} ({rate:.1f}%)"

def test_count_status():
    logs = ["a PASSED", "b FAILED", "c PASSED"]
    assert count_status(logs, "PASSED") == 2

def test_pass_rate():
    logs = ["a PASSED", "b FAILED", "c PASSED", "d PASSED"]
    assert pass_rate(logs) == 0.75

def test_pass_rate_empty():
    assert pass_rate([]) == 0.0

def test_summary_line():
    logs = ["a PASSED", "b FAILED", "c PASSED", "d PASSED"]
    assert summary_line(logs) == "PASSED: 3/4 (75.0%)"
