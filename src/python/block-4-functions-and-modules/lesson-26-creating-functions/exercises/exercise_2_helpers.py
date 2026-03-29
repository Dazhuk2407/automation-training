"""
Вправа 2: Helper-функції для тестів.
Запуск: pytest exercise_2_helpers.py -v
"""


def make_user(name, role):
    """Створити словник користувача з active=True."""
    # TODO: замініть pass на: return {"name": name, "role": role, "active": True}
    pass


def is_success_code(code):
    """True якщо 200 <= code < 300."""
    # TODO: замініть pass на: return 200 <= code < 300
    pass


def format_price(amount):
    """Форматувати ціну: '$X.XX'."""
    # TODO: замініть pass на: return f"${amount:.2f}"
    pass


def test_make_user():
    # TODO: замініть pass на:
    #   user = make_user("Alice", "admin")
    #   assert user == {"name": "Alice", "role": "admin", "active": True}
    pass

def test_success_code():
    # TODO: замініть pass на:
    #   assert is_success_code(200) is True
    #   assert is_success_code(404) is False
    pass

def test_format_price():
    # TODO: замініть pass на:
    #   assert format_price(9.9) == "$9.90"
    #   assert format_price(100) == "$100.00"
    pass