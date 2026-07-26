"""
Вправа 2: Порядок і крайні випадки перевпорядкування.

Функція failed_first уже надана. Замініть pass на правильний assert.

Запуск: pytest exercise_2_ordering.py -v
"""


def failed_first(all_tests, last_results):
    """Впалі минулого разу першими (у їх порядку), потім решта (у їх порядку)."""
    failed = [t for t in all_tests if last_results.get(t) == "failed"]
    rest = [t for t in all_tests if last_results.get(t) != "failed"]
    return failed + rest


def test_relative_order_failed():
    """Серед впалих зберігається їх взаємний порядок."""
    tests = ["test_a", "test_b", "test_c", "test_d"]
    results = {
        "test_a": "failed",
        "test_b": "passed",
        "test_c": "failed",
        "test_d": "passed",
    }
    # TODO: замініть pass на:
    # assert failed_first(tests, results) == ["test_a", "test_c", "test_b", "test_d"]
    pass


def test_relative_order_rest():
    """Серед passing зберігається їх взаємний порядок."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "failed", "test_c": "passed"}
    reordered = failed_first(tests, results)
    # TODO: замініть pass на:
    # assert reordered.index("test_a") < reordered.index("test_c")
    pass


def test_unknown_goes_to_rest():
    """Тест без запису в кеші трактується як не-впалий."""
    tests = ["test_a", "test_new", "test_b"]
    results = {"test_a": "passed", "test_b": "failed"}
    # TODO: замініть pass на:
    # assert failed_first(tests, results) == ["test_b", "test_a", "test_new"]
    pass


def test_empty_cache_keeps_order():
    """Порожній кеш (перший прогін) → звичайний порядок."""
    tests = ["test_a", "test_b", "test_c"]
    results = {}
    # TODO: замініть pass на:
    # assert failed_first(tests, results) == ["test_a", "test_b", "test_c"]
    pass


def test_failed_prefix():
    """Перші N елементів результату — це саме впалі тести."""
    tests = ["test_a", "test_b", "test_c", "test_d"]
    results = {"test_b": "failed", "test_d": "failed"}
    reordered = failed_first(tests, results)
    # TODO: замініть pass на:
    # assert reordered[:2] == ["test_b", "test_d"]
    pass
