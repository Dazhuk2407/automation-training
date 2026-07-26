"""
Приклад 2: Власні маркери — api, ui, critical.

Ці маркери НЕ вбудовані. Вони зареєстровані у examples/conftest.py через
pytest_configure(). Без реєстрації під --strict-markers збір впав би з помилкою.

Перевірити список маркерів: pytest --markers

Запуск: pytest example_2_custom_markers.py -v
"""

import pytest


@pytest.mark.api
def test_get_users_endpoint():
    """API: GET /users повертає список."""
    response = {"status": 200, "users": ["alice", "bob"]}
    assert response["status"] == 200
    assert len(response["users"]) == 2


@pytest.mark.api
def test_create_user_endpoint():
    """API: POST /users створює користувача."""
    response = {"status": 201, "id": 42}
    assert response["status"] == 201


@pytest.mark.ui
def test_login_button_visible():
    """UI: кнопка логіну присутня на сторінці."""
    page_elements = ["header", "login_button", "footer"]
    assert "login_button" in page_elements


@pytest.mark.critical
def test_payment_is_processed():
    """Critical: платіж обробляється успішно."""
    payment = {"amount": 100, "status": "completed"}
    assert payment["status"] == "completed"
