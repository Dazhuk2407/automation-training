"""Приклад 3: resolve, безпечне з'єднання, path traversal. Запуск: pytest example_3_safe_paths.py -v"""
from pathlib import Path


def normalize(p):
    return Path(p).resolve()

def join_path(base, *parts):
    result = Path(base)
    for part in parts:
        result = result / part
    return result

def is_inside(base, candidate):
    base = Path(base).resolve()
    full = (base / candidate).resolve()
    return full == base or base in full.parents

def test_resolve_removes_dotdot():
    result = Path("/a/b/../c").resolve()
    assert result == Path("/a/c")

def test_resolve_removes_dot():
    result = Path("/a/./b/./c").resolve()
    assert result == Path("/a/b/c")

def test_join_path():
    result = join_path("/srv/uploads", "reports", "q1.csv")
    assert result == Path("/srv/uploads/reports/q1.csv")

def test_is_inside_true():
    assert is_inside("/srv/uploads", "reports/q1.csv") is True

def test_is_inside_blocks_traversal():
    assert is_inside("/srv/uploads", "../../etc/passwd") is False
