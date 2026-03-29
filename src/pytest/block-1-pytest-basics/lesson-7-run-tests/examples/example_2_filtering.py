"""
Приклад 2: Тести для демонстрації фільтрації через -k.

Запуск:
    pytest example_2_filtering.py -k "login" -v    → 2 тести
    pytest example_2_filtering.py -k "not slow" -v → 5 тестів
    pytest example_2_filtering.py -k "auth" -v     → 1 тест
"""


def test_login_success():
    """Тест успішного логіну."""
    assert True


def test_login_failure():
    """Тест невдалого логіну."""
    assert True


def test_auth_token():
    """Тест аутентифікаційного токена."""
    assert True


def test_user_profile():
    """Тест профілю користувача."""
    assert True


def test_slow_database_query():
    """Повільний тест (для демонстрації -k 'not slow')."""
    assert True


def test_fast_calculation():
    """Швидкий тест."""
    assert True