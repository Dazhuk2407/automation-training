"""
Приклад 3: Симуляція складніших виразів -k (and / or / not разом).

Той самий select_by_name, що і в example_2 (файл самодостатній), але тести
показують поведінку виразів, які найчастіше пишуть у реальному -k.

Запуск: pytest example_3_k_expressions.py -v
"""


def _match_single(name, term):
    """Один підрядок матчиться в імені (регістронезалежно)."""
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
    """-k 'login and not admin' — login-тести без admin в імені."""
    names = ["test_login_valid", "test_admin_login", "test_login_admin_panel"]
    assert select_by_name(names, "login and not admin") == ["test_login_valid"]


def test_login_or_logout():
    """-k 'login or logout' — обидві фічі разом."""
    names = ["test_login_valid", "test_logout_ok", "test_signup"]
    assert select_by_name(names, "login or logout") == [
        "test_login_valid",
        "test_logout_ok",
    ]


def test_not_slow():
    """-k 'not slow' — усе, крім тестів зі 'slow' в імені."""
    names = ["test_fast_ping", "test_slow_upload", "test_quick_check"]
    assert select_by_name(names, "not slow") == ["test_fast_ping", "test_quick_check"]


def test_and_requires_both():
    """'login and valid' — обидва підрядки мають бути в імені."""
    names = ["test_login_valid", "test_login_invalid", "test_valid_token"]
    assert select_by_name(names, "login and valid") == [
        "test_login_valid",
        "test_login_invalid",
    ]


def test_or_needs_at_least_one():
    """'admin or root' — достатньо одного підрядка."""
    names = ["test_admin_panel", "test_root_access", "test_user_view"]
    assert select_by_name(names, "admin or root") == [
        "test_admin_panel",
        "test_root_access",
    ]


def test_substring_too_broad():
    """Демонстрація анти-патерна: 'log' чіпляє зайве (login, logout, logger)."""
    names = ["test_login", "test_logout", "test_logger_config"]
    assert select_by_name(names, "log") == [
        "test_login",
        "test_logout",
        "test_logger_config",
    ]
