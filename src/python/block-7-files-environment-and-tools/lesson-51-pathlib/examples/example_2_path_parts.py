"""Приклад 2: частини шляху. Запуск: pytest example_2_path_parts.py -v"""
from pathlib import Path


def get_name(path):
    return Path(path).name

def get_stem(path):
    return Path(path).stem

def get_suffix(path):
    return Path(path).suffix

def get_parent(path):
    return Path(path).parent

def test_get_name():
    assert get_name("data/reports/report.csv") == "report.csv"

def test_get_stem():
    assert get_stem("data/reports/report.csv") == "report"

def test_get_suffix():
    assert get_suffix("report.csv") == ".csv"
    assert get_suffix("archive.tar.gz") == ".gz"

def test_get_parent():
    assert get_parent("data/reports/report.csv") == Path("data/reports")

def test_parts():
    assert Path("data/logs/app.log").parts == ("data", "logs", "app.log")
