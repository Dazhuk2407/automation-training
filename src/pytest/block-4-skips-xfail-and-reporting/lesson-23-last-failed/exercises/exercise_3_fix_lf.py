"""
Вправа 3: Знайди і виправ.

Крок 1: Запустіть файл — один тест навмисно падає.
Крок 2: Прочитайте вивід pytest — який результат --lf насправді очікується?
Крок 3: Заповніть блок ВІДПОВІДЬ.
Крок 4: Виправте очікуване значення, щоб тест проходив.

Запуск: pytest exercise_3_fix_lf.py -v
"""


def last_failed(all_tests, last_results, lfnf="all"):
    """Симуляція вибору тестів для --lf (готова, не змінювати)."""
    failed = [t for t in all_tests if last_results.get(t) == "failed"]
    if failed:
        return failed
    return list(all_tests) if lfnf == "all" else []


def test_lf_picks_failed():
    """Цей тест падає — впав test_c, а не test_a. Виправте очікуване."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "passed", "test_c": "failed"}
    # ПОМИЛКА: тут очікують ["test_a"], хоча впав test_c
    assert last_failed(tests, results) == ["test_a"]


def test_lf_no_failures_runs_all():
    """Цей тест правильний: впалих немає → усі тести."""
    tests = ["test_a", "test_b"]
    results = {"test_a": "passed", "test_b": "passed"}
    assert last_failed(tests, results) == ["test_a", "test_b"]


def test_lf_lfnf_none_runs_nothing():
    """Цей тест правильний: впалих немає, lfnf='none' → нічого."""
    tests = ["test_a", "test_b"]
    results = {"test_a": "passed", "test_b": "passed"}
    assert last_failed(tests, results, lfnf="none") == []


# ВІДПОВІДЬ:
# У test_lf_picks_failed насправді впав тест: _______________
# Отже --lf має повернути: _______________
# Я виправив очікуване значення на: _______________
