"""Приклад 1: запис і читання файлу. Запуск: pytest example_1_write_read.py -v"""


def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def test_write_then_read(tmp_path):
    p = tmp_path / "data.txt"
    write_text(p, "hello")
    assert read_text(p) == "hello"

def test_write_unicode(tmp_path):
    p = tmp_path / "uni.txt"
    write_text(p, "привіт 🚀")
    assert read_text(p) == "привіт 🚀"

def test_write_overwrites(tmp_path):
    p = tmp_path / "over.txt"
    write_text(p, "first")
    write_text(p, "second")
    assert read_text(p) == "second"
