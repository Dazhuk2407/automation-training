"""Приклад 2: режими w/a/r та encoding. Запуск: pytest example_2_modes.py -v"""


def write_line(path, line):
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

def append_line(path, line):
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def read_all(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def test_write_mode_replaces(tmp_path):
    p = tmp_path / "log.txt"
    write_line(p, "one")
    write_line(p, "two")
    assert read_all(p) == "two\n"

def test_append_mode_keeps(tmp_path):
    p = tmp_path / "log.txt"
    write_line(p, "one")
    append_line(p, "two")
    assert read_all(p) == "one\ntwo\n"

def test_append_creates_file(tmp_path):
    p = tmp_path / "new.txt"
    append_line(p, "created")
    assert read_all(p) == "created\n"
