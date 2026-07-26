"""
Приклад 1: Базова ідея --lf.

Реальний `pytest --lf` бере результати минулого прогону і запускає лише
ті тести, що впали. Тут ми симулюємо цей вибір чистою функцією на даних.

Запуск: pytest example_1_lf_concept.py -v
"""


def select_failed(all_tests, last_results):
    """Повернути тести, що впали минулого разу (аналог відбору --lf).

    all_tests: список імен тестів (порядок зберігається).
    last_results: dict name -> "passed" / "failed".
    """
    return [t for t in all_tests if last_results.get(t) == "failed"]


def test_selects_only_failed():
    """З набору вибираються лише впалі тести."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "failed", "test_c": "passed"}
    assert select_failed(tests, results) == ["test_b"]


def test_multiple_failed_keep_order():
    """Кілька впалих — порядок з початкового набору зберігається."""
    tests = ["test_a", "test_b", "test_c", "test_d"]
    results = {
        "test_a": "failed",
        "test_b": "passed",
        "test_c": "failed",
        "test_d": "passed",
    }
    assert select_failed(tests, results) == ["test_a", "test_c"]


def test_all_passed_selects_nothing():
    """Якщо все зелене — відбір порожній (далі це обробить --lfnf)."""
    tests = ["test_a", "test_b"]
    results = {"test_a": "passed", "test_b": "passed"}
    assert select_failed(tests, results) == []


def test_unknown_test_treated_as_not_failed():
    """Тест, якого немає в результатах, не вважається впалим."""
    tests = ["test_a", "test_new"]
    results = {"test_a": "failed"}
    assert select_failed(tests, results) == ["test_a"]
