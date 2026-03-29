"""Вправа 2: **kwargs та unpacking. Запуск: pytest exercise_2_kwargs.py -v"""


def build_query(**kwargs):
    """Побудувати query string: 'key1=val1&key2=val2'."""
    # TODO: return "&".join(f"{k}={v}" for k, v in kwargs.items())
    pass

def merge_configs(defaults, **overrides):
    """Об'єднати defaults з overrides."""
    # TODO: return {**defaults, **overrides}
    pass

def assert_contains(data, **expected):
    """Перевірити що data містить expected поля."""
    # TODO:
    #   for key, value in expected.items():
    #       assert data[key] == value
    pass

def test_build_query():
    # TODO: assert build_query(page="1", limit="10") == "page=1&limit=10"
    pass

def test_merge():
    # TODO:
    #   result = merge_configs({"a": 1, "b": 2}, b=20, c=30)
    #   assert result == {"a": 1, "b": 20, "c": 30}
    pass

def test_assert_contains():
    user = {"name": "Alice", "role": "admin", "age": 25}
    # TODO: assert_contains(user, name="Alice", role="admin")
    pass

def test_unpack_call():
    def add(a, b):
        return a + b
    # TODO:
    #   data = {"a": 3, "b": 7}
    #   assert add(**data) == 10
    pass