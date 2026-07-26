"""Вправа 2: знайди та виправ баг.

Один із методів повертає не те, що очікує тест. Знайди рядок з `# BUG:`,
виправ його так, щоб усі 4 тести проходили. Запуск: pytest exercise_2_fix_pathlib.py -v
"""
from pathlib import Path


def file_stem(path):
    # BUG: має повертати ім'я БЕЗ розширення (.stem), а не з розширенням (.name)
    return Path(path).name

def file_suffix(path):
    return Path(path).suffix

def build_path(*parts):
    result = Path(parts[0])
    for part in parts[1:]:
        result = result / part
    return result

def save_text(folder, name, text):
    path = folder / name
    path.write_text(text, encoding="utf-8")
    return path

def test_file_stem():
    assert file_stem("data/report.csv") == "report"

def test_file_suffix():
    assert file_suffix("report.csv") == ".csv"

def test_build_path():
    assert build_path("a", "b", "c") == Path("a/b/c")

def test_save_text(tmp_path):
    path = save_text(tmp_path, "out.txt", "hi")
    assert path.exists()
    assert path.read_text(encoding="utf-8") == "hi"
