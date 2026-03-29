"""
Приклад 3: Ітерація по словниках та використання в тестах.

Запуск: pytest example_3_iteration.py -v
"""


def test_iterate_keys():
    """Ітерація по ключах."""
    config = {"host": "localhost", "port": 8080, "debug": True}
    keys = list(config.keys())
    assert "host" in keys
    assert "port" in keys
    assert len(keys) == 3


def test_iterate_values():
    """Ітерація по значеннях."""
    scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
    values = list(scores.values())
    assert max(values) == 95
    assert min(values) == 87


def test_iterate_items():
    """Ітерація по парах ключ-значення."""
    user = {"name": "Alice", "age": 25, "role": "admin"}
    items = list(user.items())
    assert ("name", "Alice") in items
    assert ("age", 25) in items


def test_check_required_fields():
    """Реальний тест: перевірити обов'язкові поля API response."""
    response = {
        "id": 1,
        "name": "Alice",
        "email": "alice@test.com",
        "created_at": "2024-01-15",
    }
    required = ["id", "name", "email"]
    for field in required:
        assert field in response, f"Missing required field: {field}"


def test_all_values_not_none():
    """Перевірити що жодне значення не None."""
    config = {"host": "localhost", "port": 8080, "timeout": 30}
    for key, value in config.items():
        assert value is not None, f"Config '{key}' is None"