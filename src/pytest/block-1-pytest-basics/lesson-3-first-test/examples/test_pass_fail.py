"""
Lesson 3: Example 3 - Pass and Fail Examples
"""


def test_passing_assertion():
    """✅ Цей тест проходить."""
    x = 10
    assert x == 10
    assert x > 5
    assert x < 20


def test_multiple_assertions():
    """✅ Тест з кількома assertions."""
    name = "pytest"
    assert isinstance(name, str)
    assert len(name) > 0
    assert name.startswith("py")


# def test_failing_assertion():
#     """❌ Цей тест падає (закоментований)."""
#     x = 10
#     assert x == 20  # AssertionError: assert 10 == 20


def test_boolean_checks():
    """✅ Тест булевих значень."""
    is_active = True
    is_disabled = False

    assert is_active
    assert not is_disabled
    assert is_active is True
    assert is_disabled is False


def test_equality_vs_identity():
    """✅ Тест рівності vs ідентичності."""
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    assert a == b      # рівність значень
    assert a is not b  # різні об'єкти
    assert a is c      # той самий об'єкт

