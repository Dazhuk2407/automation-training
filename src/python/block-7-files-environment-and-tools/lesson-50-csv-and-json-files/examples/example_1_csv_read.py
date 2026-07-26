"""Приклад 1: читання CSV. Запуск: pytest example_1_csv_read.py -v"""
import csv


def read_rows(path):
    """Прочитати CSV як список рядків-списків (разом із заголовком)."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def read_dicts(path):
    """Прочитати CSV як список словників (за заголовком)."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _make_csv(path):
    path.write_text("name,age,role\nAlice,30,admin\nBob,25,user\n", encoding="utf-8")


def test_read_rows(tmp_path):
    p = tmp_path / "users.csv"
    _make_csv(p)
    rows = read_rows(p)
    assert rows[0] == ["name", "age", "role"]
    assert rows[1] == ["Alice", "30", "admin"]
    assert len(rows) == 3


def test_read_rows_values_are_str(tmp_path):
    p = tmp_path / "users.csv"
    _make_csv(p)
    rows = read_rows(p)
    assert rows[1][1] == "30"
    assert isinstance(rows[1][1], str)


def test_read_dicts(tmp_path):
    p = tmp_path / "users.csv"
    _make_csv(p)
    dicts = read_dicts(p)
    assert dicts[0]["name"] == "Alice"
    assert dicts[1]["role"] == "user"
    assert len(dicts) == 2


def test_read_dicts_age_is_str(tmp_path):
    p = tmp_path / "users.csv"
    _make_csv(p)
    dicts = read_dicts(p)
    assert dicts[0]["age"] == "30"
    assert int(dicts[0]["age"]) == 30
