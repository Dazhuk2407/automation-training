"""Вправа 1: JSON. Запуск: pytest exercise_1_json.py -v"""
import json

RAW = '{"users": [{"id": 1, "email": "a@test.com"}, {"id": 2, "email": "b@test.com"}]}'


def count_users(raw_json):
    # TODO: return len(json.loads(raw_json)["users"])
    pass

def get_email(raw_json, user_id):
    # TODO: пройти по json.loads(raw_json)["users"] і повернути email для user_id (інакше None)
    pass

def to_json(obj):
    # TODO: return json.dumps(obj)
    pass

def test_count():
    # TODO: assert count_users(RAW) == 2
    pass

def test_get_email():
    # TODO: assert get_email(RAW, 1) == "a@test.com"
    pass

def test_get_email_missing():
    # TODO: assert get_email(RAW, 99) is None
    pass

def test_to_json_returns_str():
    # TODO: assert isinstance(to_json({"a": 1}), str)
    pass

def test_roundtrip():
    # TODO: assert json.loads(to_json({"x": [1, 2]})) == {"x": [1, 2]}
    pass
