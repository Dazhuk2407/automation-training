"""
Вправа 1: Базовий xfail.

Додайте декоратор @pytest.mark.xfail(reason="...") там, де вказано в TODO,
і замініть pass на потрібний assert.

Пам'ятайте:
- xfail-тест ВИКОНУЄТЬСЯ; якщо падає → xfailed (не failure).
- reason обов'язковий (номер тікета / опис бага).
- xfail-тест, що проходить → xpassed (теж не failure без strict).

Запуск: pytest exercise_1_xfail.py -rxX -v
Очікуваний підсумок: 0 failed.
"""

import pytest


# TODO: додайте @pytest.mark.xfail(reason="bug #1: ділення дає неправильний результат")
def test_known_bug_division():
    """Відомий баг — тест має падати → xfailed."""
    # TODO: замініть pass на падаючий assert, напр.: assert 10 / 2 == 6
    pass


# TODO: додайте @pytest.mark.xfail(reason="bug #2: конкатенація зламана")
def test_known_bug_concat():
    """Відомий баг — тест має падати → xfailed."""
    # TODO: замініть pass на падаючий assert, напр.: assert "a" + "b" == "ab!"
    pass


# TODO: додайте @pytest.mark.xfail(reason="bug #3: можливо вже пофіксили")
def test_maybe_fixed():
    """Тест проходить → xpassed (без strict → не failure)."""
    # TODO: замініть pass на assert, що ПРОХОДИТЬ, напр.: assert 2 + 2 == 4
    pass


# TODO: додайте @pytest.mark.xfail(reason="bug #4: сортування нестабільне")
def test_known_bug_sort():
    """Відомий баг — тест має падати → xfailed."""
    # TODO: замініть pass на падаючий assert, напр.: assert sorted([2, 1]) == [2, 1]
    pass


def test_normal():
    """Звичайний тест БЕЗ маркера — має проходити."""
    # TODO: замініть pass на assert, що проходить, напр.: assert isinstance(1, int)
    pass
