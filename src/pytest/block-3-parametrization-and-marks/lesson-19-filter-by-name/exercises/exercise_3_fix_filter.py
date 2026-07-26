"""
Вправа 3: Виправ відбір.

Один із тестів нижче падає, бо очікує НЕПРАВИЛЬНИЙ результат відбору.
Типова помилка: думати, що -k матчить МАРКЕРИ, а не імена.

Крок 1: Запустіть файл — один тест падає.
Крок 2: Прочитайте вивід pytest: який відбір насправді повертає select_by_name?
Крок 3: Заповніть блок ВІДПОВІДЬ.
Крок 4: Виправте очікуваний результат так, щоб тест проходив.

Запуск: pytest exercise_3_fix_filter.py -v
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


def test_login_substring_ok():
    """Цей тест правильний."""
    names = ["test_login_valid", "test_logout", "test_signup"]
    assert select_by_name(names, "login") == ["test_login_valid"]


def test_k_does_not_match_markers():
    """
    ЦЕЙ ТЕСТ ПАДАЄ.

    Тест 'test_big_upload' у реальності позначений @pytest.mark.slow,
    але його ІМ'Я не містить підрядка 'slow'. -k дивиться лише на ІМЕНА,
    тому select_by_name(..., "slow") НЕ поверне його.
    Очікуваний результат нижче помилковий — виправте його.
    """
    names = ["test_big_upload", "test_slow_ping", "test_fast_ping"]
    # ❌ Помилкове очікування: ніби 'slow' зачепить і test_big_upload
    assert select_by_name(names, "slow") == ["test_big_upload", "test_slow_ping"]


def test_not_admin_ok():
    """Цей тест правильний."""
    names = ["test_user_view", "test_admin_view"]
    assert select_by_name(names, "not admin") == ["test_user_view"]


# ВІДПОВІДЬ:
# select_by_name(..., "slow") насправді повертає: _______________
# Чому test_big_upload не потрапив у відбір: _______________
# Виправлене очікування: _______________
