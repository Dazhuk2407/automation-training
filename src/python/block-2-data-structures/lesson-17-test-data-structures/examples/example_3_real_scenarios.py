"""
Приклад 3: Реальні сценарії перевірок складних даних.

Запуск: pytest example_3_real_scenarios.py -v
"""


def get_orders_response():
    """Імітація API response зі замовленнями."""
    return {
        "status": 200,
        "data": {
            "orders": [
                {"id": 101, "user_id": 1, "total": 150.00, "status": "completed", "items": ["laptop_case"]},
                {"id": 102, "user_id": 2, "total": 49.99, "status": "pending", "items": ["mouse", "keyboard"]},
                {"id": 103, "user_id": 1, "total": 299.99, "status": "completed", "items": ["monitor"]},
            ],
        },
    }


def test_all_orders_have_required_fields():
    """Кожне замовлення має обов'язкові поля."""
    required = {"id", "user_id", "total", "status", "items"}
    orders = get_orders_response()["data"]["orders"]
    for order in orders:
        assert required.issubset(order.keys()), f"Order {order.get('id')} missing fields"


def test_completed_orders_total():
    """Сума completed замовлень."""
    orders = get_orders_response()["data"]["orders"]
    completed = [o for o in orders if o["status"] == "completed"]
    total = sum(o["total"] for o in completed)
    assert total == 449.99


def test_no_duplicate_order_ids():
    """ID замовлень унікальні."""
    orders = get_orders_response()["data"]["orders"]
    ids = [o["id"] for o in orders]
    assert len(ids) == len(set(ids))


def test_user_orders():
    """Замовлення конкретного користувача."""
    orders = get_orders_response()["data"]["orders"]
    user_1_orders = [o for o in orders if o["user_id"] == 1]
    assert len(user_1_orders) == 2


def test_all_items_not_empty():
    """Кожне замовлення має хоча б один товар."""
    orders = get_orders_response()["data"]["orders"]
    for order in orders:
        assert len(order["items"]) > 0, f"Order {order['id']} has no items"