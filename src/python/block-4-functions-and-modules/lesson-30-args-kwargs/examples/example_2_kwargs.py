"""Приклад 2: **kwargs та комбінування. Запуск: pytest example_2_kwargs.py -v"""


def build_config(**kwargs):
    return kwargs

def create_entity(entity_type, **fields):
    return {"type": entity_type, **fields}

def log(level, *messages, **meta):
    return {"level": level, "messages": messages, "meta": meta}

def test_build_config():
    config = build_config(host="localhost", port=8080)
    assert config == {"host": "localhost", "port": 8080}

def test_create_entity():
    user = create_entity("user", name="Alice", role="admin")
    assert user == {"type": "user", "name": "Alice", "role": "admin"}

def test_log_combined():
    result = log("ERROR", "timeout", "retry", host="api.com")
    assert result["level"] == "ERROR"
    assert result["messages"] == ("timeout", "retry")
    assert result["meta"] == {"host": "api.com"}

def test_kwargs_is_dict():
    def check(**kwargs):
        return type(kwargs)
    assert check(a=1) == dict