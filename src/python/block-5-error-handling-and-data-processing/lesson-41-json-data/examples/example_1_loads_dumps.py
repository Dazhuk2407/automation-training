"""Приклад 1: json.loads та json.dumps. Запуск: pytest example_1_loads_dumps.py -v"""
import json


def parse_user(raw):
    return json.loads(raw)

def to_json(obj):
    return json.dumps(obj)

def pretty(obj):
    return json.dumps(obj, indent=2, sort_keys=True)

def to_json_cyrillic(obj):
    return json.dumps(obj, ensure_ascii=False)

def test_parse():
    data = parse_user('{"name": "Alice", "age": 30}')
    assert data["name"] == "Alice"
    assert data["age"] == 30

def test_parse_returns_dict():
    data = parse_user('{"a": 1}')
    assert isinstance(data, dict)

def test_to_json_returns_str():
    text = to_json({"name": "Bob"})
    assert isinstance(text, str)
    assert '"name"' in text

def test_type_mapping():
    data = json.loads('{"count": 3, "ratio": 0.5, "ok": true, "note": null}')
    assert data["count"] == 3
    assert data["ratio"] == 0.5
    assert data["ok"] is True
    assert data["note"] is None

def test_array_maps_to_list():
    data = json.loads('[1, 2, 3]')
    assert data == [1, 2, 3]
    assert isinstance(data, list)

def test_pretty_sorted():
    text = pretty({"b": 2, "a": 1})
    assert text.index('"a"') < text.index('"b"')
    assert "\n" in text

def test_cyrillic():
    text = to_json_cyrillic({"місто": "Київ"})
    assert "Київ" in text

def test_roundtrip():
    obj = {"a": 1, "b": [2, 3]}
    assert json.loads(json.dumps(obj)) == obj
