"""Вправа 1: читання та запис файлів. Запуск: pytest exercise_1_files.py -v"""


def save_lines(path, lines):
    # TODO: відкрити path у режимі "w" (encoding="utf-8") і записати
    # TODO: кожен елемент lines окремим рядком (з "\n")
    pass

def read_lines(path):
    # TODO: відкрити path у режимі "r" (encoding="utf-8")
    # TODO: повернути список рядків без "\n" (використай strip())
    pass

def append_line(path, line):
    # TODO: відкрити path у режимі "a" (encoding="utf-8")
    # TODO: дописати line у кінець (з "\n")
    pass

def test_save_and_read(tmp_path):
    # TODO: p = tmp_path / "d.txt"; save_lines(p, ["a", "b"])
    # TODO: assert read_lines(p) == ["a", "b"]
    pass

def test_save_overwrites(tmp_path):
    # TODO: save_lines двічі у той самий файл, assert що лишився другий вміст
    pass

def test_read_strips_newline(tmp_path):
    # TODO: save_lines(p, ["admin"]); assert read_lines(p) == ["admin"]
    pass

def test_append_keeps_previous(tmp_path):
    # TODO: save_lines(p, ["one"]); append_line(p, "two")
    # TODO: assert read_lines(p) == ["one", "two"]
    pass

def test_append_creates_file(tmp_path):
    # TODO: append_line до неіснуючого файлу, assert read_lines == ["hi"]
    pass
