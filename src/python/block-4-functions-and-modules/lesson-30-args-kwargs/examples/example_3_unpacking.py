"""Приклад 3: Unpacking та практичні паттерни. Запуск: pytest example_3_unpacking.py -v"""


def create_user(name, role, active):
    return {"name": name, "role": role, "active": active}


def assert_fields(data, **expected):
    """Перевірити поля словника."""
    for key, value in expected.items():
        assert data.get(key) == value


def test_unpack_list():
    args = ["Alice", "admin", True]
    user = create_user(*args)
    assert user["name"] == "Alice"


def test_unpack_dict():
    kwargs = {"name": "Bob", "role": "user", "active": True}
    user = create_user(**kwargs)
    assert user == kwargs


def test_assert_fields_helper():
    user = {"name": "Alice", "role": "admin", "age": 25}
    assert_fields(user, name="Alice", role="admin")


def test_merge_dicts_with_unpack():
    defaults = {"timeout": 30, "verify": True}
    overrides = {"timeout": 60}
    config = {**defaults, **overrides}
    assert config == {"timeout": 60, "verify": True}