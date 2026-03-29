"""
Приклад 1: Positional vs keyword аргументи.
Запуск: pytest example_1_positional_keyword.py -v
"""


def create_user(name, role):
    return {"name": name, "role": role}


def test_positional():
    """Порядок має значення."""
    user = create_user("Alice", "admin")
    assert user["name"] == "Alice"
    assert user["role"] == "admin"


def test_keyword():
    """Порядок НЕ важливий — імена задають відповідність."""
    user = create_user(role="admin", name="Alice")
    assert user["name"] == "Alice"
    assert user["role"] == "admin"


def test_mixed():
    """Positional + keyword."""
    user = create_user("Alice", role="admin")
    assert user["name"] == "Alice"
    assert user["role"] == "admin"


def test_positional_order_matters():
    """Переплутаний порядок — баг."""
    user = create_user("admin", "Alice")
    assert user["name"] == "admin"  # name = "admin" — не те що хотіли
    assert user["role"] == "Alice"