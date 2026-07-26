"""Вправа 2: знайди і виправ баг. Запуск: pytest exercise_2_fix_json.py -v

Тести нижче падають. Знайди баг, познач `# BUG`, виправ — має стати зелено.
"""
import json

RAW = '{"data": {"items": [{"name": "pen", "price": 10}, {"name": "book", "price": 25}]}}'


def parse(raw):
    # BUG: json.dumps серіалізує обʼєкт у рядок, а нам треба розпарсити рядок в обʼєкт
    return json.dumps(raw)

def first_item_name(raw):
    return json.loads(raw)["data"]["items"][0]["name"]

def total_price(raw):
    items = json.loads(raw)["data"]["items"]
    return sum(item["price"] for item in items)

def test_parse_returns_dict():
    assert isinstance(parse(RAW), dict)

def test_parse_has_data():
    assert "data" in parse(RAW)

def test_first_item_name():
    assert first_item_name(RAW) == "pen"

def test_total_price():
    assert total_price(RAW) == 35
