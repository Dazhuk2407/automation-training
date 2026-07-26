"""
Вправа 1: Застосуйте готові маркери (smoke, regression, slow).

Маркери вже проставлено над кожним тестом.
Ваше завдання — замінити pass на правильний assert (див. docstring тесту).
Маркер не впливає на pass/fail — важливо лише щоб assert був істинним.

Запуск: pytest exercise_1_apply_markers.py -v
"""

import pytest


@pytest.mark.smoke
def test_status_code_ok():
    """Перевірте що status_code == 200."""
    status_code = 200
    # TODO: замініть pass на: assert status_code == 200
    pass


@pytest.mark.smoke
def test_user_is_authenticated():
    """Перевірте що authenticated є truthy (assert condition)."""
    authenticated = True
    # TODO: замініть pass на: assert authenticated
    pass


@pytest.mark.regression
def test_cart_total():
    """Перевірте що сума кошика 30 + 70 == 100."""
    total = 30 + 70
    # TODO: замініть pass на: assert total == 100
    pass


@pytest.mark.regression
def test_username_in_response():
    """Перевірте що 'alice' є у списку users."""
    users = ["alice", "bob"]
    # TODO: замініть pass на: assert "alice" in users
    pass


@pytest.mark.slow
def test_large_dataset_length():
    """Перевірте що довжина набору == 1000."""
    data = list(range(1000))
    # TODO: замініть pass на: assert len(data) == 1000
    pass
