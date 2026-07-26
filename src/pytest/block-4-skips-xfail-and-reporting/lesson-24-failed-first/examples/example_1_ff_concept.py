"""
Приклад 1: Концепція failed-first (--ff).

Реальний `pytest --ff` перевпорядковує тести: впалі минулого разу — першими,
далі решта. Тут ми моделюємо цю логіку чистою функцією failed_first, щоб
перевірити її звичайними тестами (БЕЗ запуску pytest всередині pytest).

Запуск: pytest example_1_ff_concept.py -v
"""


def failed_first(all_tests, last_results):
    """Повернути новий порядок: впалі минулого разу першими, потім решта.

    all_tests    — список імен тестів у звичайному порядку
    last_results — словник {ім'я_тесту: "passed" | "failed"} з минулого прогону
    """
    failed = [t for t in all_tests if last_results.get(t) == "failed"]
    rest = [t for t in all_tests if last_results.get(t) != "failed"]
    return failed + rest


def test_ff_reorders():
    """Впалий тест піднімається на початок."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "failed", "test_c": "passed"}
    assert failed_first(tests, results) == ["test_b", "test_a", "test_c"]


def test_ff_runs_all_tests():
    """--ff запускає ВСІ тести — нічого не пропущено."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "failed", "test_c": "passed"}
    reordered = failed_first(tests, results)
    assert sorted(reordered) == sorted(tests)
    assert len(reordered) == len(tests)


def test_ff_failed_go_first():
    """Обидва впалі йдуть перед усіма passing."""
    tests = ["test_a", "test_b", "test_c", "test_d"]
    results = {
        "test_a": "passed",
        "test_b": "failed",
        "test_c": "passed",
        "test_d": "failed",
    }
    assert failed_first(tests, results) == [
        "test_b", "test_d", "test_a", "test_c"
    ]


def test_ff_no_failures_keeps_order():
    """Якщо нічого не впало — порядок не змінюється."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "passed", "test_c": "passed"}
    assert failed_first(tests, results) == ["test_a", "test_b", "test_c"]


def test_ff_all_failed_keeps_order():
    """Якщо впало все — порядок теж не змінюється (усі вже 'першими')."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "failed", "test_b": "failed", "test_c": "failed"}
    assert failed_first(tests, results) == ["test_a", "test_b", "test_c"]
