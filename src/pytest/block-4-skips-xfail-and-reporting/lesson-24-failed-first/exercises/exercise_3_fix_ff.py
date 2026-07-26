"""
Вправа 3: Виправ очікуваний порядок.

Один тест навмисно падає — у ньому НЕПРАВИЛЬНИЙ очікуваний порядок.

Крок 1: Запустіть файл — один тест падає.
Крок 2: Прочитайте вивід pytest — який реальний порядок повертає failed_first?
Крок 3: Виправте очікуване значення в assert.
Крок 4: Заповніть блок ВІДПОВІДЬ.

Запуск: pytest exercise_3_fix_ff.py -v
"""


def failed_first(all_tests, last_results):
    """Впалі минулого разу першими, потім решта."""
    failed = [t for t in all_tests if last_results.get(t) == "failed"]
    rest = [t for t in all_tests if last_results.get(t) != "failed"]
    return failed + rest


def test_reorders_correctly():
    """Цей тест падає — очікуваний порядок неправильний. Виправте його."""
    tests = ["test_login", "test_logout", "test_signup"]
    results = {
        "test_login": "passed",
        "test_logout": "failed",
        "test_signup": "passed",
    }
    # ❌ Неправильний очікуваний порядок — впалий test_logout має бути ПЕРШИМ
    assert failed_first(tests, results) == [
        "test_login", "test_logout", "test_signup"
    ]


def test_all_present():
    """Цей тест працює правильно — усі тести на місці."""
    tests = ["test_login", "test_logout", "test_signup"]
    results = {"test_logout": "failed"}
    assert sorted(failed_first(tests, results)) == sorted(tests)


def test_length_unchanged():
    """Цей тест працює правильно — довжина збережена."""
    tests = ["test_login", "test_logout", "test_signup"]
    results = {"test_logout": "failed"}
    assert len(failed_first(tests, results)) == 3


# ВІДПОВІДЬ:
# Реальний порядок від failed_first: _______________
# Помилка в очікуваному значенні була: _______________
# Я виправив на: _______________
