"""Вправа 1: pathlib. Запуск: pytest exercise_1_pathlib.py -v"""
from pathlib import Path


def get_extension(path):
    # TODO: return Path(path).suffix
    pass

def join_paths(*parts):
    # TODO: з'єднай частини через Path та оператор /
    pass

def list_txt_files(folder):
    # TODO: return sorted(p.name for p in folder.glob("*.txt"))
    pass

def test_extension():
    # TODO: assert get_extension("report.csv") == ".csv"
    pass

def test_extension_no_ext():
    # TODO: assert get_extension("README") == ""
    pass

def test_join():
    # TODO: assert join_paths("a", "b", "c") == Path("a/b/c")
    pass

def test_list_txt(tmp_path):
    # TODO: створи .txt файли через tmp_path і перевір list_txt_files
    pass

def test_list_txt_empty(tmp_path):
    # TODO: assert list_txt_files(tmp_path) == []
    pass
