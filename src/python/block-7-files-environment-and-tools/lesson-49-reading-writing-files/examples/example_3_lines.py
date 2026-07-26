"""Приклад 3: читання рядків, ітерація, strip. Запуск: pytest example_3_lines.py -v"""


def save_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def read_lines_raw(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()

def read_lines_clean(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]

def count_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

def test_readlines_keeps_newline(tmp_path):
    p = tmp_path / "d.txt"
    save_lines(p, ["a", "b"])
    assert read_lines_raw(p) == ["a\n", "b\n"]

def test_strip_removes_newline(tmp_path):
    p = tmp_path / "d.txt"
    save_lines(p, ["admin", "user"])
    assert read_lines_clean(p) == ["admin", "user"]

def test_count_lines(tmp_path):
    p = tmp_path / "d.txt"
    save_lines(p, ["x", "y", "z"])
    assert count_lines(p) == 3
