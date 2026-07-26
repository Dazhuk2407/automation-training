"""
Приклад 1: Концепція `pytest -x` (== `--maxfail=1`).

Реальний `-x` зупиняє прогін після ПЕРШОГО падіння. Тут ми симулюємо це
чистою функцією: скільки тестів реально виконалось, поки не набралась
одна помилка.

Запуск: pytest example_1_x_concept.py -v
"""


def run_until_maxfail(results, maxfail):
    """Симуляція зупинки прогону після maxfail помилок.

    results: список "passed"/"failed" у порядку виконання.
    Повертає, скільки тестів РЕАЛЬНО виконалось до зупинки.
    """
    fails = 0
    executed = 0
    for r in results:
        executed += 1
        if r == "failed":
            fails += 1
            if fails >= maxfail:
                break
    return executed


def test_stop_on_first_failure():
    # -x == maxfail=1: [pass, fail, pass, fail] -> виконано 2 (стоп на першому fail)
    assert run_until_maxfail(["passed", "failed", "passed", "failed"], 1) == 2


def test_first_test_fails_immediately():
    # Перший же тест падає -> виконано лише 1
    assert run_until_maxfail(["failed", "passed", "passed"], 1) == 1


def test_x_equals_maxfail_one():
    # -x і --maxfail=1 дають однаковий результат
    results = ["passed", "passed", "failed", "passed"]
    assert run_until_maxfail(results, 1) == run_until_maxfail(results, 1)
    assert run_until_maxfail(results, 1) == 3


def test_all_pass_runs_everything():
    # Якщо падінь немає — виконуються всі тести
    assert run_until_maxfail(["passed", "passed", "passed"], 1) == 3
