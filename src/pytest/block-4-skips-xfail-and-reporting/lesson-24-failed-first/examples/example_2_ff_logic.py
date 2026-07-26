"""
Приклад 2: Деталі логіки failed-first.

Розбираємо тонкощі перевпорядкування:
- відносний порядок усередині груп зберігається;
- невідомі тести (немає в кеші) вважаються "не впалими" → йдуть у решту;
- порожній кеш = звичайний порядок (перевпорядковувати нема що).

Запуск: pytest example_2_ff_logic.py -v
"""


def failed_first(all_tests, last_results):
    """Впалі минулого разу першими (у їх порядку), потім решта (у їх порядку)."""
    failed = [t for t in all_tests if last_results.get(t) == "failed"]
    rest = [t for t in all_tests if last_results.get(t) != "failed"]
    return failed + rest


def test_relative_order_within_failed():
    """Серед впалих зберігається їх взаємний порядок."""
    tests = ["test_a", "test_b", "test_c", "test_d"]
    results = {
        "test_a": "failed",
        "test_b": "passed",
        "test_c": "failed",
        "test_d": "passed",
    }
    # test_a перед test_c, бо так вони йшли у вихідному списку
    assert failed_first(tests, results) == [
        "test_a", "test_c", "test_b", "test_d"
    ]


def test_relative_order_within_rest():
    """Серед passing теж зберігається взаємний порядок."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "failed", "test_c": "passed"}
    reordered = failed_first(tests, results)
    # test_a досі перед test_c
    assert reordered.index("test_a") < reordered.index("test_c")


def test_unknown_test_goes_to_rest():
    """Тест, якого немає в кеші, трактується як не-впалий."""
    tests = ["test_a", "test_new", "test_b"]
    results = {"test_a": "passed", "test_b": "failed"}  # про test_new нічого невідомо
    assert failed_first(tests, results) == ["test_b", "test_a", "test_new"]


def test_empty_cache_keeps_order():
    """Порожній кеш (перший прогін) — звичайний порядок."""
    tests = ["test_a", "test_b", "test_c"]
    results = {}  # прогонів ще не було
    assert failed_first(tests, results) == ["test_a", "test_b", "test_c"]


def test_length_is_preserved():
    """Перевпорядкування не додає і не втрачає тестів."""
    tests = ["test_a", "test_b", "test_c", "test_d", "test_e"]
    results = {"test_c": "failed", "test_e": "failed"}
    reordered = failed_first(tests, results)
    assert len(reordered) == len(tests)
    assert set(reordered) == set(tests)
