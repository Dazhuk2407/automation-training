"""
Приклад 1: Готові (зареєстровані) маркери — smoke, regression, slow.

Маркер НЕ змінює результат тесту — усі тести нижче проходять.
Маркер лише «тегує» тест для вибіркового запуску:
    pytest example_1_builtin_markers.py -m smoke -v

Маркери smoke/regression/slow зареєстровані глобально в кореневому pytest.ini.

Запуск: pytest example_1_builtin_markers.py -v
"""

import pytest


@pytest.mark.smoke
def test_homepage_opens():
    """Smoke: головна сторінка відкривається."""
    status_code = 200
    assert status_code == 200


@pytest.mark.smoke
def test_user_can_login():
    """Smoke: базовий сценарій логіну."""
    logged_in = True
    assert logged_in


@pytest.mark.regression
def test_password_reset_flow():
    """Regression: повний сценарій відновлення пароля."""
    steps = ["request", "email", "confirm", "reset"]
    assert len(steps) == 4


@pytest.mark.slow
def test_large_report_generation():
    """Slow: генерація великого звіту (повільний тест)."""
    rows = list(range(10_000))
    assert len(rows) == 10_000
