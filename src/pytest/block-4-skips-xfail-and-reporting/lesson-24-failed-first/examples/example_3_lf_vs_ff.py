"""
Приклад 3: last_failed (--lf) vs failed_first (--ff) на одних даних.

Дві функції на тих самих вхідних даних показують ключову різницю:
- last_failed  (--lf): повертає ЛИШЕ впалі тести;
- failed_first (--ff): повертає ВСІ тести, але впалі — першими.

Запуск: pytest example_3_lf_vs_ff.py -v
"""


def last_failed(all_tests, last_results):
    """--lf: лише тести, що впали минулого разу (у їх порядку)."""
    return [t for t in all_tests if last_results.get(t) == "failed"]


def failed_first(all_tests, last_results):
    """--ff: усі тести, але впалі минулого разу — першими."""
    failed = [t for t in all_tests if last_results.get(t) == "failed"]
    rest = [t for t in all_tests if last_results.get(t) != "failed"]
    return failed + rest


# спільні дані для порівняння двох режимів
TESTS = ["test_a", "test_b", "test_c", "test_d"]
RESULTS = {
    "test_a": "passed",
    "test_b": "failed",
    "test_c": "passed",
    "test_d": "failed",
}


def test_lf_returns_only_failed():
    """--lf лишає тільки впалі — passing відкинуто."""
    assert last_failed(TESTS, RESULTS) == ["test_b", "test_d"]


def test_ff_returns_all():
    """--ff лишає всі тести — впалі першими, решта потім."""
    assert failed_first(TESTS, RESULTS) == [
        "test_b", "test_d", "test_a", "test_c"
    ]


def test_ff_is_superset_of_lf():
    """Результат --ff містить усе з --lf і ще решту."""
    lf = last_failed(TESTS, RESULTS)
    ff = failed_first(TESTS, RESULTS)
    assert set(lf).issubset(set(ff))
    assert len(ff) > len(lf)


def test_both_start_with_same_failed():
    """Початок --ff збігається з повним списком --lf."""
    lf = last_failed(TESTS, RESULTS)
    ff = failed_first(TESTS, RESULTS)
    assert ff[:len(lf)] == lf


def test_lf_faster_ff_full_coverage():
    """--lf запускає менше (швидше), --ff — увесь набір (покриття)."""
    lf = last_failed(TESTS, RESULTS)
    ff = failed_first(TESTS, RESULTS)
    assert len(lf) == 2          # лише впалі
    assert len(ff) == len(TESTS)  # усі тести
