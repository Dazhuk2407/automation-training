"""
Вправа 3: Знайдіть і виправте помилку у класифікації наборів.

Один із тестів навмисно падає — у ньому неправильне очікування набору.

Крок 1: Запустіть файл — рівно один тест падає.
Крок 2: Прочитайте вивід pytest — яке значення повернула suite_of насправді?
Крок 3: Згадайте правило smoke ⊂ regression (пріоритет smoke).
Крок 4: Виправте очікуване значення в assert і заповніть блок ВІДПОВІДЬ.

Запуск: pytest exercise_3_fix_suite.py -v
"""


def suite_of(markers):
    if "smoke" in markers:
        return "smoke"
    if "regression" in markers:
        return "regression"
    return "uncategorized"


def test_smoke():
    """Правильний тест — проходить."""
    assert suite_of({"smoke"}) == "smoke"


def test_both_markers():
    """Цей тест ПАДАЄ — очікуване значення набору неправильне."""
    # Тест позначений і smoke, і regression. За правилом smoke має пріоритет.
    assert suite_of({"smoke", "regression"}) == "regression"


def test_uncategorized():
    """Правильний тест — проходить."""
    assert suite_of({"slow"}) == "uncategorized"


# ВІДПОВІДЬ:
# Падав тест: _______________
# suite_of({"smoke", "regression"}) повертає: _______________
# Причина: за правилом smoke ⊂ regression пріоритет має _______________
# Я виправив очікуване значення на: _______________
