"""Вправа 1: file paths. Запуск: pytest exercise_1_paths.py -v"""
from pathlib import Path


def is_absolute(p):
    # TODO: return Path(p).is_absolute()
    pass

def to_absolute(p):
    # TODO: return Path(p).resolve()
    pass

def join_safe(base, *parts):
    # TODO: з'єднати base з parts через оператор / та повернути Path
    pass

def test_is_absolute_true():
    # TODO: assert is_absolute("/etc/hosts") is True
    pass

def test_is_absolute_false():
    # TODO: assert is_absolute("data/x.txt") is False
    pass

def test_to_absolute_removes_dotdot():
    # TODO: assert to_absolute("/a/b/../c") == Path("/a/c")
    pass

def test_join_safe():
    # TODO: assert join_safe("/srv", "a", "b.txt") == Path("/srv/a/b.txt")
    pass

def test_join_safe_name():
    # TODO: assert join_safe("/srv", "a", "b.txt").name == "b.txt"
    pass
