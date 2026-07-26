"""
Вправа 1: Класифікація тестів у набори.

Функція suite_of вже написана. Ваше завдання — замінити pass на правильний
assert у кожному тесті, спираючись на правила класифікації.

Правила:
  {"smoke"}                 -> "smoke"
  {"regression"}            -> "regression"
  {"smoke", "regression"}   -> "smoke"   (smoke ⊂ regression, пріоритет smoke)
  без smoke/regression      -> "uncategorized"

Запуск: pytest exercise_1_suite.py -v
"""


def suite_of(markers):
    if "smoke" in markers:
        return "smoke"
    if "regression" in markers:
        return "regression"
    return "uncategorized"


def test_smoke_marker():
    """Тест лише з маркером smoke належить до набору 'smoke'."""
    # TODO: замініть pass на: assert suite_of({"smoke"}) == "smoke"
    pass


def test_regression_marker():
    """Тест лише з маркером regression належить до набору 'regression'."""
    # TODO: замініть pass на: assert suite_of({"regression"}) == "regression"
    pass


def test_both_markers_prefer_smoke():
    """Тест з обома маркерами класифікуємо як 'smoke'."""
    # TODO: замініть pass на: assert suite_of({"smoke", "regression"}) == "smoke"
    pass


def test_no_suite_marker():
    """Тест без smoke/regression — 'uncategorized'."""
    # TODO: замініть pass на: assert suite_of({"slow"}) == "uncategorized"
    pass


def test_empty_markers():
    """Тест без жодного маркера — 'uncategorized'."""
    # TODO: замініть pass на: assert suite_of(set()) == "uncategorized"
    pass
