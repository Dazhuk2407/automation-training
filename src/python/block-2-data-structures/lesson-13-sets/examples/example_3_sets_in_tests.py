"""
Приклад 3: Множини в реальних тестах.

Запуск: pytest example_3_sets_in_tests.py -v
"""


def test_required_fields_present():
    """API повертає всі обов'язкові поля."""
    required = {"id", "name", "email"}
    response = {"id": 1, "name": "Alice", "email": "a@t.com", "avatar": None}
    assert required.issubset(response.keys())


def test_no_duplicate_ids():
    """Перевірити що ID унікальні."""
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]
    ids = [u["id"] for u in users]
    assert len(ids) == len(set(ids)), "Duplicate IDs found"


def test_new_endpoints():
    """Знайти нові endpoints у v2."""
    v1 = {"/users", "/auth", "/products"}
    v2 = {"/users", "/auth", "/products", "/orders", "/payments"}
    new = v2 - v1
    assert new == {"/orders", "/payments"}


def test_removed_features():
    """Знайти видалені features."""
    before = {"dark_mode", "export_csv", "notifications", "chat"}
    after = {"dark_mode", "notifications", "chat"}
    removed = before - after
    assert removed == {"export_csv"}


def test_deduplicate_errors():
    """Прибрати дублікати помилок."""
    errors = ["timeout", "404", "timeout", "500", "timeout", "404"]
    unique = set(errors)
    assert len(unique) == 3
    assert "timeout" in unique