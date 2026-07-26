"""Вправа 2: виправ баг. Запуск: pytest exercise_2_fix_files.py -v

# BUG: одна з функцій працює неправильно. Знайди її, виправ і переконайся,
# що всі тести проходять. Підказка: уважно поглянь на режими відкриття файлу.
"""


def save_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]

def append_line(path, line):
    # BUG: режим "w" стирає файл — має бути "a", щоб дописувати
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

def read_all(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def test_save_and_read(tmp_path):
    p = tmp_path / "d.txt"
    save_lines(p, ["a", "b"])
    assert read_lines(p) == ["a", "b"]

def test_read_strips_newline(tmp_path):
    p = tmp_path / "d.txt"
    save_lines(p, ["admin"])
    assert read_lines(p) == ["admin"]

def test_append_keeps_previous(tmp_path):
    p = tmp_path / "d.txt"
    save_lines(p, ["one"])
    append_line(p, "two")
    assert read_lines(p) == ["one", "two"]

def test_read_all_returns_full_text(tmp_path):
    p = tmp_path / "d.txt"
    save_lines(p, ["x", "y"])
    assert read_all(p) == "x\ny\n"
