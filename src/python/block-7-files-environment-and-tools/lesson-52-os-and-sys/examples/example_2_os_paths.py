"""Приклад 2: os.path. Запуск: pytest example_2_os_paths.py -v"""
import os


def file_name(path):
    return os.path.basename(path)


def folder(path):
    return os.path.dirname(path)


def extension(path):
    # splitext повертає (root, ext)
    return os.path.splitext(path)[1]


def build_log_path(*parts):
    return os.path.join(*parts)


def test_file_name():
    assert file_name("/home/user/report.txt") == "report.txt"


def test_folder():
    assert folder("/home/user/report.txt") == "/home/user"


def test_extension():
    assert extension("report.txt") == ".txt"
    assert extension("archive.tar.gz") == ".gz"


def test_build_log_path():
    assert build_log_path("logs", "run", "out.log") == os.path.join("logs", "run", "out.log")
