"""Вправа 1: CSV та JSON. Запуск: pytest exercise_1_csv_json.py -v"""
import csv
import json


def save_csv(path, rows, fieldnames):
    # TODO: відкрити path на запис з newline="", encoding="utf-8"
    # TODO: створити csv.DictWriter(f, fieldnames=fieldnames)
    # TODO: викликати writeheader() і writerows(rows)
    pass

def read_csv_dicts(path):
    # TODO: відкрити path з newline="", encoding="utf-8"
    # TODO: return list(csv.DictReader(f))
    pass

def save_json(path, obj):
    # TODO: відкрити path на запис з encoding="utf-8"
    # TODO: json.dump(obj, f, indent=2)
    pass

def test_save_and_read_csv(tmp_path):
    # TODO: p = tmp_path / "users.csv"
    # TODO: save_csv(p, [{"name": "A", "age": "30"}], ["name", "age"])
    # TODO: assert read_csv_dicts(p)[0]["name"] == "A"
    pass

def test_csv_values_are_str(tmp_path):
    # TODO: p = tmp_path / "users.csv"
    # TODO: save_csv(p, [{"name": "A", "age": "30"}], ["name", "age"])
    # TODO: assert read_csv_dicts(p)[0]["age"] == "30"
    pass

def test_csv_header(tmp_path):
    # TODO: p = tmp_path / "users.csv"
    # TODO: save_csv(p, [{"name": "A", "age": "30"}], ["name", "age"])
    # TODO: assert p.read_text(encoding="utf-8").splitlines()[0] == "name,age"
    pass

def test_save_json(tmp_path):
    # TODO: p = tmp_path / "data.json"
    # TODO: save_json(p, {"passed": 2})
    # TODO: assert json.loads(p.read_text(encoding="utf-8"))["passed"] == 2
    pass

def test_json_indent(tmp_path):
    # TODO: p = tmp_path / "data.json"
    # TODO: save_json(p, {"a": 1})
    # TODO: assert "\n" in p.read_text(encoding="utf-8")
    pass
