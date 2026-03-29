"""
Приклад 1: Основи tuples — створення, доступ, immutability.

Запуск: pytest example_1_basics.py -v
"""

import pytest


def test_create_tuple():
    """Різні способи створення."""
    point = (10, 20)
    assert len(point) == 2

    single = (42,)  # кома обов'язкова!
    assert len(single) == 1
    assert isinstance(single, tuple)

    not_tuple = (42)  # без коми — це int
    assert isinstance(not_tuple, int)


def test_indexing():
    """Індексація — як у list."""
    status = (200, "OK", {"data": []})
    assert status[0] == 200
    assert status[1] == "OK"
    assert status[-1] == {"data": []}


def test_slicing():
    """Slicing повертає новий tuple."""
    codes = (200, 301, 404, 500)
    assert codes[:2] == (200, 301)
    assert codes[2:] == (404, 500)


def test_membership():
    """Перевірка належності."""
    allowed = (200, 201, 204)
    assert 200 in allowed
    assert 404 not in allowed


def test_immutability():
    """Tuple не можна змінити — TypeError."""
    point = (10, 20)
    with pytest.raises(TypeError):
        point[0] = 30