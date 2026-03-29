"""
Вправа 4: Assert з повідомленнями.

Додайте message тільки де це дійсно потрібно для контексту.
Прості порівняння НЕ потребують message — pytest сам покаже diff.

Запуск: pytest exercise_4_messages.py -v
"""


def test_simple_no_message():
    """Простий assert — message НЕ потрібен."""
    # TODO: замініть pass на: assert 2 + 2 == 4
    pass


def test_with_context():
    """Перевірка з контекстом — message корисний."""
    users = ["Alice", "Bob", "Charlie"]
    target = "Alice"
    # TODO: замініть pass на:
    #   assert target in users, f"User '{target}' not found in user list"
    pass


def test_precondition():
    """Перевірка передумови — message пояснює чому це важливо."""
    items = [1, 2, 3]
    # TODO: замініть pass на:
    #   assert len(items) > 0, "Items list must not be empty before processing"
    pass