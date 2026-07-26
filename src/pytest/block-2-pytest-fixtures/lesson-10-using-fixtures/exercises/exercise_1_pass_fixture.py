"""
Вправа 1: Передати фікстуру як параметр.

Фікстури вже оголошені нижче. Прийміть їх як параметр тесту
і замініть pass на правильний assert.
Не викликайте фікстуру напряму (username()) — пишіть її ім'я як параметр.

Запуск: pytest exercise_1_pass_fixture.py -v
"""

import pytest


@pytest.fixture
def username():
    return "alice"


@pytest.fixture
def number():
    return 42


@pytest.fixture
def items():
    return ["a", "b", "c"]


def test_username(username):
    """username має дорівнювати 'alice'."""
    # TODO: замініть pass на: assert username == "alice"
    pass


def test_username_type(username):
    """username — це str."""
    # TODO: замініть pass на: assert isinstance(username, str)
    pass


def test_number(number):
    """number має дорівнювати 42."""
    # TODO: замініть pass на: assert number == 42
    pass


def test_number_positive(number):
    """number більше за 0."""
    # TODO: замініть pass на: assert number > 0
    pass


def test_items_length(items):
    """items містить 3 елементи."""
    # TODO: замініть pass на: assert len(items) == 3
    pass
