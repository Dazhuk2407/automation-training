"""
Вправа 1: Відбір за підрядком імені (симуляція -k).

Функція select_by_name вже реалізована — вона симулює pytest -k.
Ваше завдання: замінити pass на правильний assert у кожному тесті.

Запуск: pytest exercise_1_filter.py -v
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


def test_filter_login():
    """-k login забирає лише login-тест."""
    names = ["test_login_valid", "test_logout", "test_signup"]
    # TODO: замініть pass на:
    # assert select_by_name(names, "login") == ["test_login_valid"]
    pass


def test_filter_matches_two():
    """Підрядок 'login' зачіпляє обидва login-тести."""
    names = ["test_login_valid", "test_login_invalid", "test_logout"]
    # TODO: assert що результат == ["test_login_valid", "test_login_invalid"]
    pass


def test_filter_case_insensitive():
    """-k регістронезалежний."""
    names = ["test_login_valid", "test_signup"]
    # TODO: assert select_by_name(names, "LOGIN") == ["test_login_valid"]
    pass


def test_filter_no_match():
    """Якщо підрядка немає — порожній список."""
    names = ["test_login", "test_logout"]
    # TODO: assert select_by_name(names, "signup") == []
    pass


def test_filter_signup():
    """-k signup забирає лише signup-тест."""
    names = ["test_login", "test_signup_new", "test_logout"]
    # TODO: assert select_by_name(names, "signup") == ["test_signup_new"]
    pass
