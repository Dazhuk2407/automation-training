"""
Приклад 3: Практичні паттерни в тестах.

Запуск: pytest example_3_practical.py -v
"""


def get_display_name(user):
    """nickname або name як fallback."""
    return user.get("nickname") or user["name"]


def format_result(passed, total):
    """Форматувати результат тестів."""
    status = "ALL PASSED" if passed == total else f"{passed}/{total} passed"
    return status


def get_env_label(env):
    """Мітка середовища."""
    return "PROD" if env == "production" else env.upper()


def test_display_with_nickname():
    assert get_display_name({"name": "Alice", "nickname": "ally"}) == "ally"


def test_display_fallback():
    assert get_display_name({"name": "Alice"}) == "Alice"


def test_all_passed():
    assert format_result(10, 10) == "ALL PASSED"


def test_partial_passed():
    assert format_result(8, 10) == "8/10 passed"


def test_env_production():
    assert get_env_label("production") == "PROD"


def test_env_staging():
    assert get_env_label("staging") == "STAGING"