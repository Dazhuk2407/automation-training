"""Приклад 2: запис CSV. Запуск: pytest example_2_csv_write.py -v"""
import csv


def write_rows(path, rows):
    """Записати список списків через csv.writer."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_dicts(path, rows, fieldnames):
    """Записати список словників через csv.DictWriter із заголовком."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def read_back(path):
    """Допоміжне читання назад як список словників."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_write_rows(tmp_path):
    p = tmp_path / "out.csv"
    write_rows(p, [["name", "age"], ["Alice", "30"], ["Bob", "25"]])
    rows = read_back(p)
    assert rows[0]["name"] == "Alice"
    assert rows[1]["age"] == "25"


def test_write_dicts(tmp_path):
    p = tmp_path / "out.csv"
    data = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
    write_dicts(p, data, fieldnames=["name", "age"])
    rows = read_back(p)
    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"


def test_writeheader_present(tmp_path):
    p = tmp_path / "out.csv"
    write_dicts(p, [{"name": "A", "age": "1"}], fieldnames=["name", "age"])
    first_line = p.read_text(encoding="utf-8").splitlines()[0]
    assert first_line == "name,age"


def test_no_blank_lines(tmp_path):
    p = tmp_path / "out.csv"
    write_rows(p, [["a"], ["b"]])
    lines = p.read_text(encoding="utf-8").splitlines()
    assert lines == ["a", "b"]
