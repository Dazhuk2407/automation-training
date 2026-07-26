"""Приклад 2: шлях відносно скрипта через Path(__file__). Запуск: pytest example_2_script_relative.py -v"""
from pathlib import Path

HERE = Path(__file__).parent


def data_path(name):
    return HERE / "data" / name

def script_dir():
    return HERE

def test_data_path_is_absolute():
    assert data_path("file.txt").is_absolute()

def test_data_path_name():
    assert data_path("users.json").name == "users.json"

def test_script_dir_independent_of_cwd():
    # Path(__file__).parent не залежить від cwd — це тека самого файлу
    assert script_dir() == Path(__file__).resolve().parent

def test_write_and_read_with_tmp_path(tmp_path):
    # Реальний файл лише через tmp_path fixture
    target = tmp_path / "sub" / "out.txt"
    target.parent.mkdir(parents=True)
    target.write_text("hello", encoding="utf-8")
    assert target.exists()
    assert target.read_text(encoding="utf-8") == "hello"
