"""
Приклад 2: Повна логіка --lf, включно з поведінкою --lfnf.

Коли впалих немає, реальний pytest за замовчуванням запускає ВСІ тести
(--lfnf all). Тут ми моделюємо це параметром lfnf.

Запуск: pytest example_2_lf_logic.py -v
"""


def last_failed(all_tests, last_results, lfnf="all"):
    """Симуляція вибору тестів для --lf.

    all_tests: список імен тестів.
    last_results: dict name -> "passed" / "failed".
    lfnf: поведінка коли впалих немає — "all" (усі) або "none" (жодного).

    Повертає:
      - список впалих тестів, якщо такі є;
      - інакше — усі тести (lfnf="all") або порожній список (lfnf="none").
    """
    failed = [t for t in all_tests if last_results.get(t) == "failed"]
    if failed:
        return failed
    return list(all_tests) if lfnf == "all" else []


def test_lf_only_failed():
    """Є впалі — повертаємо лише їх."""
    tests = ["test_a", "test_b", "test_c"]
    results = {"test_a": "passed", "test_b": "failed", "test_c": "passed"}
    assert last_failed(tests, results) == ["test_b"]


def test_lf_none_failed_runs_all():
    """Впалих немає, lfnf за замовчуванням — запускаємо всі."""
    tests = ["test_a", "test_b"]
    results = {"test_a": "passed", "test_b": "passed"}
    assert last_failed(tests, results) == ["test_a", "test_b"]


def test_lf_none_failed_lfnf_none_runs_nothing():
    """Впалих немає, lfnf='none' — не запускаємо нічого."""
    tests = ["test_a", "test_b"]
    results = {"test_a": "passed", "test_b": "passed"}
    assert last_failed(tests, results, lfnf="none") == []


def test_lf_empty_cache_runs_all():
    """Порожній кеш (перший прогін) = немає впалих → усі."""
    tests = ["test_a", "test_b", "test_c"]
    results = {}
    assert last_failed(tests, results) == ["test_a", "test_b", "test_c"]


def test_lf_all_failed_returns_all():
    """Усе впало — повертаємо весь набір як впалий."""
    tests = ["test_a", "test_b"]
    results = {"test_a": "failed", "test_b": "failed"}
    assert last_failed(tests, results) == ["test_a", "test_b"]
