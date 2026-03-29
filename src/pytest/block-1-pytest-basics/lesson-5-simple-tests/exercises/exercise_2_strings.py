"""
Вправа 2: Тести для рядків.

Замініть pass на assert у кожному тесті.
Запуск: pytest exercise_2_strings.py -v
"""


def test_upper():
    """'hello'.upper() має повернути 'HELLO'."""
    # TODO: замініть pass на: assert "hello".upper() == "HELLO"
    pass


def test_lower():
    """'WORLD'.lower() має повернути 'world'."""
    # TODO: замініть pass на: assert "WORLD".lower() == "world"
    pass


def test_contains():
    """'test' є підрядком 'pytest'."""
    # TODO: замініть pass на: assert "test" in "pytest"
    pass


def test_not_contains():
    """'java' немає в 'python'."""
    # TODO: замініть pass на: assert "java" not in "python"
    pass


def test_starts_with():
    """URL починається з 'https://'."""
    url = "https://example.com"
    # TODO: замініть pass на: assert url.startswith("https://")
    pass


def test_split():
    """'a,b,c'.split(',') має повернути ['a', 'b', 'c']."""
    # TODO: замініть pass на: assert "a,b,c".split(",") == ["a", "b", "c"]
    pass