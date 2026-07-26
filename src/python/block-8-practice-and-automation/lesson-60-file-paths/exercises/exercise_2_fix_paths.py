"""Вправа 2: знайди та виправ баг. Запуск: pytest exercise_2_fix_paths.py -v

Один з тестів падає. Знайди рядок з коментарем `# BUG:` та виправ його.
"""
from pathlib import Path


def is_absolute(p):
    return Path(p).is_absolute()

def normalize(p):
    # BUG: забули resolve() — ".." не прибирається, шлях не нормалізується
    return Path(p)

def join_path(base, *parts):
    result = Path(base)
    for part in parts:
        result = result / part
    return result

def parent_dir(p):
    return Path(p).parent

def test_is_absolute():
    assert is_absolute("/etc/hosts") is True
    assert is_absolute("data/x.txt") is False

def test_normalize_removes_dotdot():
    assert normalize("/a/b/../c") == Path("/a/c")

def test_join_path():
    assert join_path("/srv", "logs", "app.txt") == Path("/srv/logs/app.txt")

def test_parent_dir():
    assert parent_dir("/srv/logs/app.txt") == Path("/srv/logs")
