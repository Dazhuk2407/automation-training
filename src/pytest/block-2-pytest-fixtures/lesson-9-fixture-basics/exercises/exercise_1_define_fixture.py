"""
Вправа 1: Оголосіть фікстуру.

Тут вам треба ДОПИСАТИ фікстури (тіла позначені pass) і використати їх
у тестах. Замініть кожен pass згідно з підказкою у TODO.

Нагадування:
- Фікстура — це функція з декоратором @pytest.fixture.
- Значення повертають через return.
- Тест отримує фікстуру, приймаючи її ім'я як параметр.

Запуск: pytest exercise_1_define_fixture.py -v
"""

import pytest


@pytest.fixture
def sample_number():
    """Фікстура має повернути число 42."""
    # TODO: замініть pass на: return 42
    pass


@pytest.fixture
def sample_list():
    """Фікстура має повернути список [10, 20, 30]."""
    # TODO: замініть pass на: return [10, 20, 30]
    pass


@pytest.fixture
def sample_user():
    """Фікстура має повернути dict {"name": "Bob", "age": 30}."""
    # TODO: замініть pass на: return {"name": "Bob", "age": 30}
    pass


def test_number_value(sample_number):
    """sample_number має дорівнювати 42."""
    # TODO: замініть pass на: assert sample_number == 42
    pass


def test_list_sum(sample_list):
    """Сума sample_list має дорівнювати 60."""
    # TODO: замініть pass на: assert sum(sample_list) == 60
    pass


def test_list_length(sample_list):
    """Довжина sample_list має дорівнювати 3."""
    # TODO: замініть pass на: assert len(sample_list) == 3
    pass


def test_user_name(sample_user):
    """Ім'я користувача має бути 'Bob'."""
    # TODO: замініть pass на: assert sample_user["name"] == "Bob"
    pass


def test_user_age(sample_user):
    """Вік користувача має бути 30."""
    # TODO: замініть pass на: assert sample_user["age"] == 30
    pass
