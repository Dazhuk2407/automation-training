"""
Приклад 1: Passing тест та реально падаючий assert.

Запуск: pytest example_1_pass_and_fail.py -v
Результат: 1 passed, 1 failed. Подивіться на traceback.
"""


def test_passing():
    """Цей тест проходить."""
    assert 2 + 2 == 4


def test_failing_assertion():
    """Цей тест падає — подивіться на вивід pytest."""
    result = 5
    assert result == 10