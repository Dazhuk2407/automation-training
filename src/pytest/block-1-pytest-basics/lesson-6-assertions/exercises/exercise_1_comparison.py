"""
Вправа 1: Порівняння та boolean.

Замініть pass на правильний assert.
Зверніть увагу: assert condition, а не assert condition is True.

Запуск: pytest exercise_1_comparison.py -v
"""


def test_equality():
    """10 має дорівнювати 10."""
    # TODO: замініть pass на: assert 10 == 10
    pass


def test_inequality():
    """'hello' не дорівнює 'world'."""
    # TODO: замініть pass на: assert "hello" != "world"
    pass


def test_greater():
    """15 більше за 10."""
    # TODO: замініть pass на: assert 15 > 10
    pass


def test_truthiness():
    """True є truthy — використовуйте assert condition."""
    # TODO: замініть pass на: assert True
    pass


def test_none():
    """None перевіряється через is None."""
    value = None
    # TODO: замініть pass на: assert value is None
    pass


def test_not_none():
    """42 не є None."""
    value = 42
    # TODO: замініть pass на: assert value is not None
    pass