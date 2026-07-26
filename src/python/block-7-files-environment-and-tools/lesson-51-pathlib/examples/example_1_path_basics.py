"""Приклад 1: створення та з'єднання шляхів. Запуск: pytest example_1_path_basics.py -v"""
from pathlib import Path


def build_log_path():
    return Path("data") / "logs" / "app.log"

def join_parts(*parts):
    result = Path(parts[0])
    for part in parts[1:]:
        result = result / part
    return result

def data_file(name):
    return Path("data") / name

def test_build_log_path():
    assert build_log_path() == Path("data/logs/app.log")

def test_join_parts():
    assert join_parts("a", "b", "c") == Path("a/b/c")

def test_data_file():
    assert data_file("users.json") == Path("data/users.json")

def test_slash_operator():
    assert Path("reports") / "2026" == Path("reports/2026")
