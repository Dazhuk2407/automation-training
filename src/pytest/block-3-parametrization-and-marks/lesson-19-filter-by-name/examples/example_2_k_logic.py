"""
Приклад 2: Симуляція логіки -k (підрядок та прості вирази).

pytest -k під капотом бере ІМ'Я тесту і перевіряє, чи задовольняє воно вираз.
Тут ми реалізуємо ту саму ідею звичайним Python-кодом, щоб її було видно.

select_by_name(names, expression) повертає імена, які "пройшли" фільтр -k.

Запуск: pytest example_2_k_logic.py -v
"""


def _match_single(name, term):
    """Один підрядок матчиться в імені (регістронезалежно) — як у pytest -k."""
    return term.lower() in name.lower()


def select_by_name(names, expression):
    """
    Симуляція pytest -k <expression> для списку імен.

    Підтримує:
      - підрядок:        "login"
      - not X:           "not admin"
      - X and Y:         "login and valid"
      - X or Y:          "login or logout"

    Матчинг завжди по ПІДРЯДКУ імені (не по маркерах).
    """
    expr = expression.strip()

    def keep(name):
        if " or " in expr:
            left, right = expr.split(" or ", 1)
            return keep_term(name, left.strip()) or keep_term(name, right.strip())
        if " and " in expr:
            left, right = expr.split(" and ", 1)
            return keep_term(name, left.strip()) and keep_term(name, right.strip())
        return keep_term(name, expr)

    def keep_term(name, term):
        if term.startswith("not "):
            return not _match_single(name, term[len("not "):].strip())
        return _match_single(name, term)

    return [name for name in names if keep(name)]


def test_k_substring():
    """Простий підрядок: -k login."""
    names = ["test_login_valid", "test_logout", "test_signup"]
    assert select_by_name(names, "login") == ["test_login_valid"]


def test_k_substring_case_insensitive():
    """-k регістронезалежний: LOGIN матчить login."""
    names = ["test_login_valid", "test_signup"]
    assert select_by_name(names, "LOGIN") == ["test_login_valid"]


def test_k_matches_multiple():
    """Підрядок може зачепити кілька імен."""
    names = ["test_login_valid", "test_login_invalid", "test_logout"]
    assert select_by_name(names, "login") == [
        "test_login_valid",
        "test_login_invalid",
    ]


def test_k_not():
    """-k 'not admin' — усе, крім admin-тестів."""
    names = ["test_user_view", "test_admin_view", "test_admin_delete"]
    assert select_by_name(names, "not admin") == ["test_user_view"]


def test_k_no_match_returns_empty():
    """Якщо підрядок ніде не зустрічається — порожній відбір."""
    names = ["test_login", "test_logout"]
    assert select_by_name(names, "signup") == []
