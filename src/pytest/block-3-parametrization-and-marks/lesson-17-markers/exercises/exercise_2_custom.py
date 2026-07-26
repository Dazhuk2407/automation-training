"""
Вправа 2: Власні маркери (api, ui, critical) + кілька маркерів на тесті.

Маркери вже проставлено. Власні маркери (api, ui, critical) зареєстровано
у exercises/conftest.py — тому файл збирається під --strict-markers.
Ваше завдання — замінити pass на правильний assert (див. docstring).

Запуск: pytest exercise_2_custom.py -v
"""

import pytest


@pytest.mark.api
def test_response_status():
    """Перевірте що response['status'] == 201."""
    response = {"status": 201}
    # TODO: замініть pass на: assert response["status"] == 201
    pass


@pytest.mark.api
def test_response_has_id():
    """Перевірте що 'id' є серед ключів response."""
    response = {"id": 42, "name": "alice"}
    # TODO: замініть pass на: assert "id" in response
    pass


@pytest.mark.ui
def test_button_visible():
    """Перевірте що 'submit' є у списку elements."""
    elements = ["header", "submit", "footer"]
    # TODO: замініть pass на: assert "submit" in elements
    pass


@pytest.mark.critical
def test_payment_completed():
    """Перевірте що payment['status'] == 'completed'."""
    payment = {"status": "completed"}
    # TODO: замініть pass на: assert payment["status"] == "completed"
    pass


@pytest.mark.smoke
@pytest.mark.api
def test_health_endpoint():
    """Кілька маркерів (smoke + api). Перевірте що service_up є truthy."""
    service_up = True
    # TODO: замініть pass на: assert service_up
    pass
