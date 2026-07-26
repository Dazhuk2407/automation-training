"""
Приклад 3: Кілька маркерів на тесті + маркер на класі та файлі.

Демонструє:
- стек декораторів (smoke + api на одному тесті);
- маркер на цілому класі (@pytest.mark.regression над class);
- маркер на цілому файлі через pytestmark.

Усі маркери (smoke, regression — глобальні; api, ui, critical — з conftest.py)
зареєстровані, тому файл збирається під --strict-markers.

Запуск: pytest example_3_multiple_markers.py -v
"""

import pytest


# Маркер на весь файл: усі тести модуля стають api-тестами.
pytestmark = pytest.mark.api


@pytest.mark.smoke
@pytest.mark.critical
def test_health_check():
    """Кілька маркерів: smoke + critical (+ api з pytestmark файлу)."""
    service_up = True
    assert service_up


@pytest.mark.regression
class TestCheckout:
    """Маркер regression навішено на цілий клас — усі методи його отримають."""

    def test_add_to_cart(self):
        cart = ["item-1"]
        assert len(cart) == 1

    def test_apply_coupon(self):
        price = 100
        discount = 20
        assert price - discount == 80

    @pytest.mark.critical
    def test_place_order(self):
        """Метод має і regression (з класу), і critical (свій)."""
        order = {"status": "placed"}
        assert order["status"] == "placed"
