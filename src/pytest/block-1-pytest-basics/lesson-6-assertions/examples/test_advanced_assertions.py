"""
Lesson 6: Example 2 - Advanced Assertions
"""
import pytest


def test_exception_assertions():
    """Тест assertions для виключень."""

    # Базовий test для виключення
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0

    # Тест для ValueError
    with pytest.raises(ValueError):
        int("not a number")

    # Тест для KeyError
    with pytest.raises(KeyError):
        d = {"a": 1}
        _ = d["missing_key"]

    # Тест для IndexError
    with pytest.raises(IndexError):
        lst = [1, 2, 3]
        _ = lst[10]


def test_exception_messages():
    """Тест повідомлень в виключеннях."""

    # Перевірка повідомлення у виключенні
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")

    # З регулярним виразом
    with pytest.raises(ValueError, match=r"invalid.*for int"):
        int("xyz")


def test_collection_assertions():
    """Тест assertions для колекцій."""

    # Списки
    assert [1, 2, 3] == [1, 2, 3]
    assert [1, 2, 3] != [1, 2, 4]
    assert len([1, 2, 3]) == 3
    assert 2 in [1, 2, 3]

    # Словники
    assert {"a": 1} == {"a": 1}
    assert len({"a": 1, "b": 2}) == 2
    assert "a" in {"a": 1}
    assert "c" not in {"a": 1, "b": 2}

    # Вкладені структури
    matrix = [[1, 2], [3, 4]]
    assert matrix[0][0] == 1
    assert matrix[1][1] == 4


def test_string_assertions():
    """Тест assertions для рядків."""

    # Базова рівність
    assert "hello" == "hello"
    assert "hello" != "world"

    # Методи рядків
    assert "HELLO".lower() == "hello"
    assert "hello".upper() == "HELLO"
    assert "hello world".title() == "Hello World"

    # Contain
    assert "test" in "pytest"
    assert "java" not in "pytest"

    # Prefix/Suffix
    assert "pytest".startswith("py")
    assert "pytest".endswith("est")

    # Length
    assert len("pytest") == 6


def test_numeric_assertions():
    """Тест assertions для чисел."""

    # Integers
    assert 10 == 10
    assert 10 > 5
    assert 5 < 10

    # Floats
    assert 3.14 > 3
    assert 3.14 < 4

    # Float equality з tolerance
    import pytest
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 22 / 7 == pytest.approx(3.142857, rel=1e-5)

