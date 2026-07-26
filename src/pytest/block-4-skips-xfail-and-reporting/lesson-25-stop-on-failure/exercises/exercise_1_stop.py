"""
Вправа 1: Логіка `-x` (== `--maxfail=1`).

Реалізацію run_until_maxfail НЕ чіпайте — вона вже готова.
Замініть pass на правильний assert (див. таблицю в EXERCISES.md).

Запуск: pytest exercise_1_stop.py -v
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


def test_stop_on_first():
    """-x зупиняється на першому fail: [pass, fail, pass, fail], maxfail=1 -> 2."""
    # TODO: замініть pass на:
    #   assert run_until_maxfail(["passed", "failed", "passed", "failed"], 1) == 2
    pass


def test_first_fails():
    """Перший тест падає: [fail, pass, pass], maxfail=1 -> 1."""
    # TODO: замініть pass на:
    #   assert run_until_maxfail(["failed", "passed", "passed"], 1) == 1
    pass


def test_all_pass():
    """Падінь немає: [pass, pass, pass], maxfail=1 -> 3."""
    # TODO: замініть pass на:
    #   assert run_until_maxfail(["passed", "passed", "passed"], 1) == 3
    pass


def test_last_fails():
    """Падіння лише останнє: [pass, pass, fail], maxfail=1 -> 3."""
    # TODO: замініть pass на:
    #   assert run_until_maxfail(["passed", "passed", "failed"], 1) == 3
    pass
