"""Приклад 3: JSON-файли. Запуск: pytest example_3_json_files.py -v"""
import json


def save_json(path, obj):
    """Записати Python-обʼєкт у JSON-файл з відступами."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)


def load_json(path):
    """Прочитати JSON-файл у Python-обʼєкт."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def test_roundtrip_dict(tmp_path):
    p = tmp_path / "data.json"
    save_json(p, {"name": "Alice", "age": 30})
    data = load_json(p)
    assert data["name"] == "Alice"
    assert data["age"] == 30


def test_types_preserved(tmp_path):
    p = tmp_path / "data.json"
    save_json(p, {"age": 30, "active": True, "tags": ["a", "b"]})
    data = load_json(p)
    assert isinstance(data["age"], int)
    assert data["active"] is True
    assert data["tags"] == ["a", "b"]


def test_nested_structure(tmp_path):
    p = tmp_path / "report.json"
    report = {"passed": 2, "cases": [{"name": "t1", "ok": True}, {"name": "t2", "ok": False}]}
    save_json(p, report)
    data = load_json(p)
    assert data["cases"][1]["name"] == "t2"
    assert data["passed"] == 2


def test_indent_written(tmp_path):
    p = tmp_path / "data.json"
    save_json(p, {"a": 1})
    text = p.read_text(encoding="utf-8")
    assert "\n" in text
    assert '  "a": 1' in text
