"""
Вправа 2: Вирази -k (and / or / not).

Функція select_by_name реалізована — симулює pytest -k.
Замініть pass на правильний assert у кожному тесті.

Запуск: pytest exercise_2_expressions.py -v
"""


def _match_single(name, term):
    return term.lower() in name.lower()


def select_by_name(names, expression):
    """Симуляція pytest -k: підрядок, not X, X and Y, X or Y (по підрядку імені)."""
    expr = expression.strip()

    def keep_term(name, term):
        if term.startswith("not "):
            return not _match_single(name, term[len("not "):].strip())
        return _match_single(name, term)

    def keep(name):
        if " or " in expr:
            left, right = expr.split(" or ", 1)
            return keep_term(name, left.strip()) or keep_term(name, right.strip())
        if " and " in expr:
            left, right = expr.split(" and ", 1)
            return keep_term(name, left.strip()) and keep_term(name, right.strip())
        return keep_term(name, expr)

    return [name for name in names if keep(name)]


def test_login_and_not_admin():
    """-k 'login and not admin'."""
    names = ["test_login_valid", "test_admin_login", "test_login_admin_panel"]
    # TODO: assert select_by_name(names, "login and not admin") == ["test_login_valid"]
    pass


def test_login_or_logout():
    """-k 'login or logout'."""
    names = ["test_login_valid", "test_logout_ok", "test_signup"]
    # TODO: assert результат == ["test_login_valid", "test_logout_ok"]
    pass


def test_not_slow():
    """-k 'not slow' — усе, крім slow."""
    names = ["test_fast_ping", "test_slow_upload", "test_quick_check"]
    # TODO: assert select_by_name(names, "not slow") == ["test_fast_ping", "test_quick_check"]
    pass


def test_and_requires_both():
    """-k 'login and invalid' — обидва підрядки в імені."""
    names = ["test_login_valid", "test_login_invalid", "test_signup_invalid"]
    # TODO: assert результат == ["test_login_invalid"]
    pass


def test_or_at_least_one():
    """-k 'admin or root' — достатньо одного підрядка."""
    names = ["test_admin_panel", "test_root_access", "test_user_view"]
    # TODO: assert результат == ["test_admin_panel", "test_root_access"]
    pass
