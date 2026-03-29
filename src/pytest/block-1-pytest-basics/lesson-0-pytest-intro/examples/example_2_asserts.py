"""
Приклад 2: Різні види assert

Assert — це перевірка: "Я очікую, що це правда".
Якщо assert не пройде — тест падає і pytest покаже що саме пішло не так.

Запуск: pytest example_2_asserts.py -v
"""


def test_equality():
    """Перевірка на рівність."""
    assert 2 + 2 == 4
    assert "hello" == "hello"


def test_inequality():
    """Перевірка на нерівність."""
    assert 2 + 2 != 5
    assert "hello" != "world"


def test_comparison():
    """Перевірка порівнянь."""
    assert 10 > 5
    assert 3 < 7
    assert 5 >= 5
    assert 5 <= 5


def test_boolean():
    """Перевірка True/False."""
    assert True
    assert not False
    assert bool(1)
    assert not bool(0)


def test_none():
    """Перевірка на None."""
    value = None
    assert value is None

    other = 42
    assert other is not None


def test_membership():
    """Перевірка чи елемент є в колекції."""
    assert "h" in "hello"
    assert 3 in [1, 2, 3]
    assert "key" in {"key": "value"}


def test_type_check():
    """Перевірка типу даних."""
    assert isinstance(42, int)
    assert isinstance("hello", str)
    assert isinstance([1, 2], list)