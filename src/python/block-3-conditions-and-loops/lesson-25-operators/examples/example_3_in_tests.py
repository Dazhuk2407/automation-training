"""
Приклад 3: Оператори у тестових перевірках.
Запуск: pytest example_3_in_tests.py -v
"""


def test_status_in_range():
    """Перевірка що статус код у діапазоні."""
    status = 201
    assert 200 <= status < 300


def test_response_time_acceptable():
    """Час відповіді в межах норми."""
    time_ms = 150
    assert 0 < time_ms < 500


def test_user_has_access():
    """Перевірка доступу через логічні оператори."""
    user = {"role": "admin", "active": True}
    has_access = user["role"] == "admin" and user["active"]
    assert has_access


def test_required_field_present():
    """Перевірка наявності поля через in."""
    response = {"id": 1, "name": "Alice", "email": "alice@t.com"}
    assert "email" in response
    assert response.get("phone") is None


def test_even_odd():
    """Парність через модуль."""
    assert 10 % 2 == 0  # парне
    assert 7 % 2 != 0   # непарне


def test_augmented_assignment():
    """Присвоєння з операцією."""
    total = 0
    total += 10
    total += 20
    total *= 2
    assert total == 60