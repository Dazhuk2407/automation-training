"""Приклад 3: читання/запис та ітерація. Запуск: pytest example_3_path_files.py -v"""
from pathlib import Path


def write_report(folder, name, text):
    path = folder / name
    path.write_text(text, encoding="utf-8")
    return path

def read_report(path):
    return path.read_text(encoding="utf-8")

def make_nested_dir(base):
    target = base / "logs" / "2026"
    target.mkdir(parents=True, exist_ok=True)
    return target

def list_txt_files(folder):
    return sorted(p.name for p in folder.glob("*.txt"))

def test_write_and_read(tmp_path):
    path = write_report(tmp_path, "report.txt", "Hello, QA!")
    assert path.exists()
    assert read_report(path) == "Hello, QA!"

def test_make_nested_dir(tmp_path):
    target = make_nested_dir(tmp_path)
    assert target.is_dir()
    assert (tmp_path / "logs").is_dir()

def test_list_txt_files(tmp_path):
    (tmp_path / "a.txt").write_text("1", encoding="utf-8")
    (tmp_path / "b.txt").write_text("2", encoding="utf-8")
    (tmp_path / "c.json").write_text("3", encoding="utf-8")
    assert list_txt_files(tmp_path) == ["a.txt", "b.txt"]

def test_checks(tmp_path):
    file_path = tmp_path / "data.log"
    file_path.write_text("x", encoding="utf-8")
    assert file_path.exists() is True
    assert file_path.is_file() is True
    assert file_path.is_dir() is False
    assert (tmp_path / "missing.log").exists() is False
