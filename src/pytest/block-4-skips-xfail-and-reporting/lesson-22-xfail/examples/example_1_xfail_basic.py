"""
Приклад 1: Базовий xfail — тест реально падає → статус xfailed (не failure).

Ключова ідея: pytest ВИКОНУЄ тіло тесту. Оскільки він падає, а ми
очікували падіння, статус — xfailed, і це НЕ рахується як failure.

Запуск: pytest example_1_xfail_basic.py -rx -v
Очікуваний підсумок: 0 failed (кілька xfailed).
"""

import pytest


@pytest.mark.xfail(reason="bug #123: округлення float неточне")
def test_known_bug():
    """Відомий баг — тест падає, але це очікувано → xfailed."""
    assert round(2.675, 2) == 2.68   # реально дає 2.67 → падає → xfailed


@pytest.mark.xfail(reason="bug #124: конкатенація ще не працює")
def test_another_known_bug():
    """Ще один очікуваний провал → xfailed."""
    assert 1 + 1 == 3   # падає → xfailed


def test_normal_pass():
    """Звичайний тест, що проходить — для контрасту."""
    assert 2 + 2 == 4
