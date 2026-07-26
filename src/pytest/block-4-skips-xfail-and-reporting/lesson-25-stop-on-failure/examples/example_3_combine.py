"""
Приклад 3: Поєднання порядку (`--ff`) із зупинкою (`-x`).

Спершу переупорядковуємо тести як `--ff` (раніше впалі — першими),
потім застосовуємо логіку `-x` (зупинка на першому падінні).
Ключова ідея: ПОРЯДОК задає --ff, а ЗУПИНКУ — -x. Це різні кроки.

Запуск: pytest example_3_combine.py -v
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


def failed_first_order(tests, previously_failed):
    """Симуляція `--ff`: раніше впалі тести йдуть першими, порядок стабільний.

    tests: список імен тестів у звичайному порядку збору.
    previously_failed: множина/список імен, що падали минулого разу.
    """
    failed = [t for t in tests if t in previously_failed]
    rest = [t for t in tests if t not in previously_failed]
    return failed + rest


def test_ff_puts_failed_first():
    # Раніше впав "c" -> він переміщується на початок
    order = failed_first_order(["a", "b", "c", "d"], {"c"})
    assert order == ["c", "a", "b", "d"]


def test_ff_keeps_relative_order():
    # Кілька раніше впалих зберігають відносний порядок; решта — теж
    order = failed_first_order(["a", "b", "c", "d"], {"b", "d"})
    assert order == ["b", "d", "a", "c"]


def test_ff_then_x_stops_at_first_fail():
    # --ff вивів "c" першим, і саме він досі падає -> з -x виконано лише 1
    order = failed_first_order(["a", "b", "c"], {"c"})
    # results відповідають новому порядку [c, a, b]: c досі падає
    results = ["failed", "passed", "passed"]
    assert order == ["c", "a", "b"]
    assert run_until_maxfail(results, 1) == 1


def test_x_does_not_change_order():
    # -x не переставляє тести: без раніше впалих порядок незмінний
    order = failed_first_order(["a", "b", "c"], set())
    assert order == ["a", "b", "c"]
    # а зупинка -x впливає лише на кількість виконаних
    assert run_until_maxfail(["passed", "failed", "passed"], 1) == 2
