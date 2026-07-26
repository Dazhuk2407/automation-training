"""
Вправа 3: Знайди і виправ неправильне очікування відбору.

Один із тестів має НЕПРАВИЛЬНИЙ очікуваний результат відбору і тому падає.
Функція `select_by_marker` — правильна, помилка саме в assert.

Крок 1: Запустіть файл — рівно один тест падає.
Крок 2: Прочитайте вивід pytest — що реально відбирає вираз?
Крок 3: Виправте очікуваний список у падаючому тесті.
Крок 4: Заповніть блок ВІДПОВІДЬ унизу.

Запуск: pytest exercise_3_fix_selection.py -v
"""

from marker_selection import select_by_marker


TESTS = [
    {"name": "test_login", "markers": {"smoke"}},
    {"name": "test_quick_check", "markers": {"smoke", "slow"}},
    {"name": "test_edge_case", "markers": {"regression"}},
    {"name": "test_report", "markers": {"regression", "slow"}},
]


def _names(tests):
    return [t["name"] for t in tests]


def test_smoke_selection():
    """Правильний тест: `smoke` відбирає test_login та test_quick_check."""
    selected = select_by_marker(TESTS, "smoke")
    assert _names(selected) == ["test_login", "test_quick_check"]


def test_smoke_and_not_slow_selection():
    """ПАДАЄ: очікуваний результат неправильний.

    `smoke and not slow` відкидає test_quick_check (він slow),
    тож у відборі лишається лише test_login.
    """
    selected = select_by_marker(TESTS, "smoke and not slow")
    # Неправильне очікування — виправте його:
    assert _names(selected) == ["test_login", "test_quick_check"]


def test_regression_selection():
    """Правильний тест: `regression` відбирає test_edge_case та test_report."""
    selected = select_by_marker(TESTS, "regression")
    assert _names(selected) == ["test_edge_case", "test_report"]


# ВІДПОВІДЬ:
# Падав тест: _______________
# Вираз "smoke and not slow" реально відбирає: _______________
# (бо test_quick_check має маркер slow і відкидається через `not slow`)
# Я виправив очікуваний список на: _______________
