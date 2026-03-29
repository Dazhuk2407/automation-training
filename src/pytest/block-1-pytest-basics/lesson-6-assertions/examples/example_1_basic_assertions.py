"""
Приклад 1: Базові assertions — порівняння, boolean, типи, membership.

Запуск: pytest example_1_basic_assertions.py -v
"""


def test_comparison():
    """Порівняння значень."""
    assert 5 == 5
    assert 5 != 4
    assert 5 > 3
    assert 5 < 10
    assert 5 >= 5
    assert 5 <= 5


def test_boolean():
    """Truthiness — правильний стиль."""
    assert True
    assert not False
    assert 5 > 3
    assert not (5 < 3)


def test_none():
    """Перевірка на None."""
    value = None
    assert value is None

    other = 42
    assert other is not None


def test_type_check():
    """Перевірка типів через isinstance."""
    assert isinstance(5, int)
    assert isinstance("hello", str)
    assert isinstance([1, 2], list)
    assert isinstance(3.14, (int, float))


def test_membership():
    """Перевірка належності."""
    assert 3 in [1, 2, 3]
    assert "test" in "pytest"
    assert "name" in {"name": "Alice"}
    assert 10 not in [1, 2, 3]


def test_collection_equality():
    """Порівняння колекцій."""
    assert [1, 2, 3] == [1, 2, 3]
    assert {"a": 1} == {"a": 1}
    assert (1, 2) == (1, 2)