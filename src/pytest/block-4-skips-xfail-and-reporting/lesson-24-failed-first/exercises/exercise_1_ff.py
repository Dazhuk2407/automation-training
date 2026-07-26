"""
Вправа 1: Перевірка failed_first (симуляція --ff).

Функція failed_first уже надана. Замініть pass на правильний assert.

Запуск: pytest exercise_1_ff.py -v
"""


def failed_first(all_tests, last_results):
    """Впалі минулого разу першими, потім решта."""
    failed = [t for t in all_tests if last_results.get(t) == "failed"]
    rest = [t for t in all_tests if last_results.get(t) != "failed"]
    return failed + rest


def test_single_failed_first():
    """Впалий test_b має стати першим."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "failed", "test_c": "passed"}
    # TODO: замініть pass на:
    # assert failed_first(tests, results) == ["test_b", "test_a", "test_c"]
    pass


def test_all_tests_present():
    """--ff нічого не пропускає — усі тести на місці."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "failed", "test_c": "passed"}
    # TODO: замініть pass на:
    # assert sorted(failed_first(tests, results)) == sorted(tests)
    pass


def test_no_failures_keeps_order():
    """Нічого не впало — порядок незмінний."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "passed", "test_c": "passed"}
    # TODO: замініть pass на:
    # assert failed_first(tests, results) == ["test_a", "test_b", "test_c"]
    pass


def test_two_failed_first():
    """Обидва впалі йдуть перед passing."""
    tests = ["test_a", "test_b", "test_c", "test_d"]
    results = {
        "test_a": "passed",
        "test_b": "failed",
        "test_c": "passed",
        "test_d": "failed",
    }
    # TODO: замініть pass на:
    # assert failed_first(tests, results) == ["test_b", "test_d", "test_a", "test_c"]
    pass


def test_length_preserved():
    """Довжина результату дорівнює довжині вхідного списку."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_b": "failed"}
    # TODO: замініть pass на:
    # assert len(failed_first(tests, results)) == len(tests)
    pass
