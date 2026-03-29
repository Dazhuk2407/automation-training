"""
Приклад 2: Логічні, membership та identity оператори.
Запуск: pytest example_2_logical_membership.py -v
"""


def test_logical_and():
    assert True and True
    assert not (True and False)


def test_logical_or():
    assert True or False
    assert not (False or False)


def test_logical_not():
    assert not False
    assert not (5 < 3)


def test_membership_list():
    codes = [200, 301, 404]
    assert 200 in codes
    assert 500 not in codes


def test_membership_string():
    assert "test" in "pytest"
    assert "java" not in "python"


def test_membership_dict():
    config = {"host": "localhost", "port": 8080}
    assert "host" in config      # перевіряє ключі
    assert "localhost" not in config  # НЕ перевіряє значення


def test_identity_none():
    value = None
    assert value is None
    assert value is not True


def test_identity_vs_equality():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert a == b      # рівність значень
    assert a is not b  # різні об'єкти