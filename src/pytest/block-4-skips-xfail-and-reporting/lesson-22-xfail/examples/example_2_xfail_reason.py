"""
Приклад 2: xfail з reason поряд зі звичайними passing-тестами.

reason пояснює, ЧОМУ тест падає (номер тікета). У звіті з -rx причина видима.
Умовний xfail: маркер активний лише якщо умова істинна.

Запуск: pytest example_2_xfail_reason.py -rx -v
Очікуваний підсумок: 0 failed (passed + xfailed).
"""

import sys

import pytest


def test_addition():
    """Звичайний робочий тест."""
    assert 2 + 3 == 5


def test_string_upper():
    """Звичайний робочий тест."""
    assert "abc".upper() == "ABC"


@pytest.mark.xfail(reason="JIRA-456: парсер дати не обробляє порожній рядок")
def test_date_parser_bug():
    """Відомий баг із зрозумілою причиною → xfailed."""
    value = int("")   # кидає ValueError → xfailed
    assert value == 0


@pytest.mark.xfail(
    sys.version_info < (3, 0),
    reason="ця поведінка недоступна на Python 2",
)
def test_conditional_xfail():
    """Умовний xfail: на Python 3 умова False → звичайний тест, що проходить."""
    assert isinstance("текст", str)
