"""
Вправа 3: «Виправ» — відомий баг НЕ позначений xfail і ПАДАЄ.

Наразі рівно ОДИН тест падає (test_known_bug_rounding): він відтворює відомий
баг, але не позначений маркером xfail, тому в підсумку буде 1 failed.

Ваше завдання (один з варіантів):
  A) Позначити падаючий тест @pytest.mark.xfail(reason="...") → стане xfailed.
  B) АБО виправити сам assert так, щоб тест проходив.

Після вашого виправлення: 0 failed (буде або 1 xfailed, або все passed).

Запуск: pytest exercise_3_fix_xfail.py -rxX -v
"""

import pytest


def test_known_bug_rounding():
    """Відомий баг: округлення float неточне. ЗАРАЗ падає (1 failed)."""
    # TODO: позначте цю функцію @pytest.mark.xfail(reason="bug #6: округлення")
    #       АБО виправте assert (напр., round(2.675, 2) == 2.67).
    assert round(2.675, 2) == 2.68


def test_addition_works():
    """Цей тест коректний — проходить."""
    assert 2 + 2 == 4


def test_string_works():
    """Цей тест коректний — проходить."""
    assert "py" + "test" == "pytest"


# ВІДПОВІДЬ:
# Варіант A (позначити як очікуваний баг):
#     @pytest.mark.xfail(reason="bug #6: округлення float неточне")
#     def test_known_bug_rounding():
#         assert round(2.675, 2) == 2.68   # → xfailed, 0 failed
#
# Варіант B (виправити assert під реальну поведінку):
#     def test_known_bug_rounding():
#         assert round(2.675, 2) == 2.67   # → passed, 0 failed
