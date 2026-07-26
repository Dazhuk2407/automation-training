"""
Приклад 2: Regression-набір — повне покриття, включно з критичними тестами.

Regression перевіряє "чи ми нічого не зламали?".
Критичні тести мають ДВА маркери (smoke + regression) — це реалізує
принцип smoke ⊂ regression: повний прогін regression включає і smoke.

Запуск усього файлу:        pytest example_2_regression_suite.py -v
Тільки regression:          pytest example_2_regression_suite.py -m regression -v
Тільки smoke (підмножина):  pytest example_2_regression_suite.py -m smoke -v
"""

import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_login_valid_user():
    """Критичний: входить і в smoke, і в regression."""
    result = {"logged_in": True}
    assert result["logged_in"] is True


@pytest.mark.regression
def test_login_with_expired_token():
    """Краєвий випадок: тільки regression."""
    token = {"valid": False, "reason": "expired"}
    assert token["valid"] is False


@pytest.mark.regression
def test_password_reset_link_single_use():
    """Краєвий випадок: посилання одноразове — тільки regression."""
    link = {"used": True, "reusable": False}
    assert link["reusable"] is False


@pytest.mark.regression
@pytest.mark.slow
def test_generate_yearly_report():
    """Повільний краєвий випадок: тільки regression, не smoke."""
    report = {"pages": 120, "generated": True}
    assert report["generated"] is True
    assert report["pages"] > 0


@pytest.mark.regression
def test_user_list_pagination():
    """Краєвий випадок: пагінація — тільки regression."""
    page = {"items": [1, 2, 3], "page": 2, "per_page": 3}
    assert len(page["items"]) <= page["per_page"]
