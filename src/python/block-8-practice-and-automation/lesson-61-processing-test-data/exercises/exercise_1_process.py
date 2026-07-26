"""Вправа 1: обробка логів. Запуск: pytest exercise_1_process.py -v"""


def parse_line(line):
    # TODO: розбити line.strip().split() у dict {"date", "level", "test", "status"}
    pass

def count_failed(lines):
    # TODO: return sum(1 for ln in lines if ln.strip().split()[-1] == "FAILED")
    pass

def pass_rate(lines):
    # TODO: total = len(lines); if total == 0: return 0.0
    # TODO: return count PASSED / total
    pass

def test_parse_line():
    # TODO: assert parse_line("2024-01-15 INFO test_a PASSED")["status"] == "PASSED"
    pass

def test_count_failed():
    # TODO: assert count_failed(["a PASSED", "b FAILED", "c FAILED"]) == 2
    pass

def test_count_failed_none():
    # TODO: assert count_failed(["a PASSED", "b PASSED"]) == 0
    pass

def test_pass_rate():
    # TODO: assert pass_rate(["a PASSED", "b FAILED", "c PASSED", "d PASSED"]) == 0.75
    pass

def test_pass_rate_empty():
    # TODO: assert pass_rate([]) == 0.0
    pass
