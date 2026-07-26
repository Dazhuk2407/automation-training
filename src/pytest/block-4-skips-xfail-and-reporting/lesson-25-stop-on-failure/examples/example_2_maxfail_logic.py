"""
Приклад 2: Узагальнена логіка `--maxfail=N`.

Прогін зупиняється, коли накопичилось N падінь. Тести, що проходять,
на лічильник помилок НЕ впливають.

Запуск: pytest example_2_maxfail_logic.py -v
"""


def run_until_maxfail(results, maxfail):
    """Скільки тестів виконалось до зупинки після maxfail помилок."""
    fails = 0
    executed = 0
    for r in results:
        executed += 1
        if r == "failed":
            fails += 1
            if fails >= maxfail:
                break
    return executed


def test_maxfail_two():
    # Стоп після 2 помилок: [fail, pass, fail, pass] -> виконано 3
    assert run_until_maxfail(["failed", "passed", "failed", "passed"], 2) == 3


def test_maxfail_three():
    # Стоп після 3 помилок: [fail, fail, pass, fail, pass] -> виконано 4
    assert run_until_maxfail(["failed", "failed", "passed", "failed", "passed"], 3) == 4


def test_passes_do_not_count():
    # Проходження не збільшують лічильник: одна помилка серед проходжень
    # при maxfail=2 не зупиняє -> виконуються всі 5
    assert run_until_maxfail(["passed", "passed", "failed", "passed", "passed"], 2) == 5


def test_not_enough_failures_runs_all():
    # Падінь менше за maxfail -> виконуються всі тести
    assert run_until_maxfail(["failed", "passed", "passed"], 3) == 3


def test_maxfail_reached_exactly_at_end():
    # N-та помилка — останній тест: виконались усі
    assert run_until_maxfail(["passed", "failed", "passed", "failed"], 2) == 4
