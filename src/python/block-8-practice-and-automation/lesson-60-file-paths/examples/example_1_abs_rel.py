"""Приклад 1: абсолютні vs відносні шляхи, cwd. Запуск: pytest example_1_abs_rel.py -v"""
from pathlib import Path


def is_absolute(p):
    return Path(p).is_absolute()

def relative_to_cwd(p):
    return Path.cwd() / p

def current_dir():
    return Path.cwd()

def test_is_absolute():
    assert is_absolute("/etc/hosts") is True
    assert is_absolute("data/x.txt") is False
    assert is_absolute("../config.ini") is False

def test_relative_to_cwd():
    result = relative_to_cwd("data/x.txt")
    assert result.is_absolute()
    assert result.name == "x.txt"

def test_current_dir_is_absolute():
    assert current_dir().is_absolute()
