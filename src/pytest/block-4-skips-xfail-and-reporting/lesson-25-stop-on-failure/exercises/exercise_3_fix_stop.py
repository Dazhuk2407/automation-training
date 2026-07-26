"""
Вправа 3: Знайди і виправ.

Один assert про кількість виконаних тестів НЕПРАВИЛЬНИЙ — через це один тест падає.

Крок 1: Запустіть файл — один тест навмисно падає.
Крок 2: Прочитайте вивід pytest — яке число очікувалось, а яке отримано?
Крок 3: Виправте неправильне очікуване значення.
Крок 4: Заповніть блок ВІДПОВІДЬ.

Запуск: pytest exercise_3_fix_stop.py -v
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


def test_stop_on_first_correct():
    """Цей тест правильний: -x зупиняється на першому fail -> виконано 2."""
    assert run_until_maxfail(["passed", "failed", "passed", "failed"], 1) == 2


def test_maxfail_two_broken():
    """Цей тест ПАДАЄ — очікуване значення неправильне, виправте його.

    [fail, pass, fail, pass] при maxfail=2: зупинка на другому fail (3-й тест),
    отже реально виконано 3, а не 4.
    """
    # TODO: виправте очікуване число
    assert run_until_maxfail(["failed", "passed", "failed", "passed"], 2) == 4


def test_all_pass_correct():
    """Цей тест правильний: падінь немає -> виконуються всі 3."""
    assert run_until_maxfail(["passed", "passed", "passed"], 1) == 3


# ВІДПОВІДЬ:
# Неправильний тест: _______________
# pytest показав (expected vs actual): _______________
# Правильне число виконаних: _______________
