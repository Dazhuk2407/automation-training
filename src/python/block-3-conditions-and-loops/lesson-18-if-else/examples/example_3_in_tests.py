"""
Приклад 3: Умовна логіка у тестових сценаріях.

Запуск: pytest example_3_in_tests.py -v
"""


def classify_response_time(ms):
    """Класифікувати час відповіді API."""
    if ms < 100:
        return "fast"
    elif ms < 500:
        return "normal"
    else:
        return "slow"


def get_user_level(score):
    """Визначити рівень користувача за балами."""
    if score >= 90:
        return "expert"
    elif score >= 70:
        return "intermediate"
    elif score >= 50:
        return "beginner"
    else:
        return "novice"


def test_response_boundaries():
    """Тест граничних значень."""
    assert classify_response_time(99) == "fast"
    assert classify_response_time(100) == "normal"   # boundary
    assert classify_response_time(499) == "normal"
    assert classify_response_time(500) == "slow"      # boundary


def test_user_levels():
    """Тест всіх рівнів."""
    assert get_user_level(95) == "expert"
    assert get_user_level(75) == "intermediate"
    assert get_user_level(55) == "beginner"
    assert get_user_level(30) == "novice"


def test_user_level_boundaries():
    """Тест boundary values."""
    assert get_user_level(90) == "expert"
    assert get_user_level(89) == "intermediate"
    assert get_user_level(70) == "intermediate"
    assert get_user_level(69) == "beginner"
    assert get_user_level(50) == "beginner"
    assert get_user_level(49) == "novice"