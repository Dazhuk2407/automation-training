"""
Lesson 6: Example 1 - Basic Assertions
"""


def test_comparison_assertions():
    """Тест порівнювальних assertions."""
    assert 5 == 5
    assert 5 != 4
    assert 5 > 3
    assert 5 < 10
    assert 5 >= 5
    assert 5 <= 5


def test_assertions_with_messages():
    """Тест assertions з повідомленнями."""
    x = 10
    y = 5

    assert x > y, f"Expected {x} > {y}"
    assert x != y, "x має бути не рівно y"
    assert x + y == 15, f"Sum should be 15, got {x + y}"


def test_membership_assertions():
    """Тест assertions для належності."""
    numbers = [1, 2, 3, 4, 5]

    assert 3 in numbers
    assert 10 not in numbers

    text = "pytest"
    assert "test" in text
    assert "java" not in text

    user = {"name": "Alice", "age": 25}
    assert "name" in user
    assert "email" not in user


def test_type_assertions():
    """Тест assertions для типів."""
    assert isinstance(5, int)
    assert isinstance("hello", str)
    assert isinstance([1, 2], list)
    assert isinstance({"a": 1}, dict)
    assert isinstance(3.14, float)

    # Кілька типів
    assert isinstance(5, (int, float))
    assert isinstance(3.14, (int, float))


def test_boolean_assertions():
    """Тест boolean assertions."""
    assert True
    assert not False
    assert 5 > 3
    assert not (5 < 3)

    # is / is not
    assert True is True
    assert False is False
    assert None is None
    assert 5 is not None

