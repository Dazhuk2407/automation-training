"""Приклад 3: агрегація результатів. Запуск: pytest example_3_aggregate.py -v"""


def count_by_status(lines):
    counts = {}
    for ln in lines:
        status = ln.strip().split()[-1]
        counts[status] = counts.get(status, 0) + 1
    return counts

def count_level(lines, level):
    return sum(1 for ln in lines if level in ln.split())

def pass_rate(lines):
    total = len(lines)
    if total == 0:
        return 0.0
    passed = sum(1 for ln in lines if ln.strip().split()[-1] == "PASSED")
    return passed / total

def build_report(lines):
    counts = count_by_status(lines)
    total = len(lines)
    rate = pass_rate(lines) * 100
    header = f"TOTAL: {total} tests ({rate:.1f}% passed)"
    body = "\n".join(f"{status}: {n}" for status, n in counts.items())
    return f"{header}\n{body}" if body else header

def test_count_by_status():
    logs = [
        "2024-01-15 INFO test_a PASSED",
        "2024-01-15 INFO test_b FAILED",
        "2024-01-15 INFO test_c PASSED",
    ]
    assert count_by_status(logs) == {"PASSED": 2, "FAILED": 1}

def test_count_level():
    logs = [
        "2024-01-15 INFO test_a PASSED",
        "2024-01-15 ERROR test_b FAILED",
        "2024-01-15 ERROR test_c FAILED",
    ]
    assert count_level(logs, "ERROR") == 2
    assert count_level(logs, "INFO") == 1

def test_pass_rate():
    logs = [
        "2024-01-15 INFO test_a PASSED",
        "2024-01-15 INFO test_b FAILED",
        "2024-01-15 INFO test_c PASSED",
        "2024-01-15 INFO test_d PASSED",
    ]
    assert pass_rate(logs) == 0.75

def test_pass_rate_empty():
    assert pass_rate([]) == 0.0

def test_build_report():
    logs = [
        "2024-01-15 INFO test_a PASSED",
        "2024-01-15 INFO test_b FAILED",
        "2024-01-15 INFO test_c PASSED",
        "2024-01-15 INFO test_d PASSED",
    ]
    report = build_report(logs)
    assert "TOTAL: 4 tests (75.0% passed)" in report
    assert "PASSED: 3" in report
    assert "FAILED: 1" in report
