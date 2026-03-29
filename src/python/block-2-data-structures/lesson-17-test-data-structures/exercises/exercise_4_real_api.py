"""
Вправа 4: Реальний API сценарій.
Запуск: pytest exercise_4_real_api.py -v
"""

ORDERS = [
    {"id": 101, "user_id": 1, "total": 150.00, "status": "completed", "items": ["case"]},
    {"id": 102, "user_id": 2, "total": 49.99, "status": "pending", "items": ["mouse", "pad"]},
    {"id": 103, "user_id": 1, "total": 299.99, "status": "completed", "items": ["monitor"]},
]


def test_completed_count():
    """Кількість completed замовлень == 2."""
    # TODO: замініть pass на:
    #   completed = [o for o in ORDERS if o["status"] == "completed"]
    #   assert len(completed) == 2
    pass


def test_total_sum():
    """Сума всіх total."""
    # TODO: замініть pass на:
    #   total = sum(o["total"] for o in ORDERS)
    #   assert total == 499.98
    pass


def test_user_orders():
    """Замовлення user_id == 1."""
    # TODO: замініть pass на:
    #   user_orders = [o for o in ORDERS if o["user_id"] == 1]
    #   assert len(user_orders) == 2
    pass


def test_no_empty_items():
    """Кожне замовлення має хоча б один item."""
    # TODO: замініть pass на:
    #   for order in ORDERS:
    #       assert len(order["items"]) > 0
    pass