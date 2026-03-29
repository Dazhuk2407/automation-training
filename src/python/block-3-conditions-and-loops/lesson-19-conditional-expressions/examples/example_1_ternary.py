"""
Приклад 1: Тернарний оператор.

Запуск: pytest example_1_ternary.py -v
"""


def test_basic_ternary():
    """Базовий тернарний оператор."""
    status = 200
    result = "ok" if status == 200 else "error"
    assert result == "ok"


def test_ternary_false():
    """Тернарний при False умові."""
    status = 500
    result = "ok" if status == 200 else "error"
    assert result == "error"


def test_ternary_with_comparison():
    """Тернарний з порівнянням."""
    age = 20
    category = "adult" if age >= 18 else "minor"
    assert category == "adult"


def test_ternary_in_fstring():
    """Тернарний всередині f-string."""
    count = 5
    message = f"{count} {'test' if count == 1 else 'tests'} passed"
    assert message == "5 tests passed"


def test_ternary_assignment():
    """Вибір значення."""
    is_admin = True
    access_level = "full" if is_admin else "limited"
    assert access_level == "full"