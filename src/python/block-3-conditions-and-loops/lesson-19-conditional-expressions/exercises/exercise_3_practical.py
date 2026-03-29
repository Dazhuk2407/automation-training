"""
Вправа 3: Практичні функції з conditional expressions.
Запуск: pytest exercise_3_practical.py -v
"""


def display_name(user):
    """Повернути nickname або name як fallback."""
    # TODO: замініть pass на: return user.get("nickname") or user["name"]
    pass


def format_count(n):
    """'1 item' або 'N items'."""
    # TODO: замініть pass на: return f"{n} {'item' if n == 1 else 'items'}"
    pass


def access_level(user):
    """'full' для admin, 'read-only' для інших."""
    # TODO: замініть pass на: return "full" if user.get("role") == "admin" else "read-only"
    pass


def test_display_with_nickname():
    # TODO: замініть pass на: assert display_name({"name": "Alice", "nickname": "ally"}) == "ally"
    pass

def test_display_fallback():
    # TODO: замініть pass на: assert display_name({"name": "Alice"}) == "Alice"
    pass

def test_format_one():
    # TODO: замініть pass на: assert format_count(1) == "1 item"
    pass

def test_format_many():
    # TODO: замініть pass на: assert format_count(5) == "5 items"
    pass

def test_admin_access():
    # TODO: замініть pass на: assert access_level({"role": "admin"}) == "full"
    pass

def test_user_access():
    # TODO: замініть pass на: assert access_level({"role": "user"}) == "read-only"
    pass