"""
Вправа 1: Логіка відбору --lf (last_failed).

Функцію-симуляцію last_failed() вже надано нижче — НЕ змінюйте її.
Ваше завдання: замінити pass на правильний assert у кожному тесті.

Нагадування:
- є впалі  → повертаються лише вони;
- впалих немає, lfnf="all"  → усі тести;
- впалих немає, lfnf="none" → порожній список.

Запуск: pytest exercise_1_lf.py -v
"""


def last_failed(all_tests, last_results, lfnf="all"):
    """Симуляція вибору тестів для --lf (готова, не змінювати)."""
    failed = [t for t in all_tests if last_results.get(t) == "failed"]
    if failed:
        return failed
    return list(all_tests) if lfnf == "all" else []


def test_only_failed_selected():
    """Впав лише test_b — саме він і має повернутись."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "failed", "test_c": "passed"}
    # TODO: замініть pass на: assert last_failed(tests, results) == ["test_b"]
    pass


def test_two_failed_keep_order():
    """Впали test_a і test_c — порядок з набору зберігається."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "failed", "test_b": "passed", "test_c": "failed"}
    # TODO: замініть pass на: assert last_failed(tests, results) == ["test_a", "test_c"]
    pass


def test_none_failed_runs_all():
    """Все зелене, lfnf за замовчуванням — запускаємо всі."""
    tests = ["test_a", "test_b"]
    results = {"test_a": "passed", "test_b": "passed"}
    # TODO: замініть pass на: assert last_failed(tests, results) == ["test_a", "test_b"]
    pass


def test_none_failed_lfnf_none():
    """Все зелене, lfnf='none' — не запускаємо нічого."""
    tests = ["test_a", "test_b"]
    results = {"test_a": "passed", "test_b": "passed"}
    # TODO: замініть pass на: assert last_failed(tests, results, lfnf="none") == []
    pass


def test_empty_cache_runs_all():
    """Порожній кеш (перший прогін) → усі тести."""
    tests = ["test_a", "test_b", "test_c"]
    results = {}
    # TODO: замініть pass на: assert last_failed(tests, results) == ["test_a", "test_b", "test_c"]
    pass
