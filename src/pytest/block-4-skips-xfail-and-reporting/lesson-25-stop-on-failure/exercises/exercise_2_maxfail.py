"""
Вправа 2: Логіка `--maxfail=N`.

Реалізацію run_until_maxfail НЕ чіпайте — вона вже готова.
Замініть pass на правильний assert (див. таблицю в EXERCISES.md).
Пам'ятайте: тести, що ПРОХОДЯТЬ, лічильник помилок не збільшують.

Запуск: pytest exercise_2_maxfail.py -v
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
    """Стоп після 2 помилок: [fail, pass, fail, pass], maxfail=2 -> 3."""
    # TODO: замініть pass на:
    #   assert run_until_maxfail(["failed", "passed", "failed", "passed"], 2) == 3
    pass


def test_maxfail_three():
    """Стоп після 3 помилок: [fail, fail, pass, fail, pass], maxfail=3 -> 4."""
    # TODO: замініть pass на:
    #   assert run_until_maxfail(["failed", "failed", "passed", "failed", "passed"], 3) == 4
    pass


def test_passes_dont_count():
    """Проходження не рахуються: одна помилка при maxfail=2 -> виконано всі 5."""
    # TODO: замініть pass на:
    #   assert run_until_maxfail(["passed", "passed", "failed", "passed", "passed"], 2) == 5
    pass


def test_not_enough_fails():
    """Падінь менше за maxfail: [fail, pass, pass], maxfail=3 -> 3."""
    # TODO: замініть pass на:
    #   assert run_until_maxfail(["failed", "passed", "passed"], 3) == 3
    pass
