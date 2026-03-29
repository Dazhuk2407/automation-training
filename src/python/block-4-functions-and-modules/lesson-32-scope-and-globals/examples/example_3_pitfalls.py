"""Приклад 3: Shadowing та типові пастки. Запуск: pytest example_3_pitfalls.py -v"""

import pytest


def test_shadowing_builtin():
    """Не перезаписуйте built-in імена."""
    # Збережемо оригінальний len
    original_len = len
    assert original_len([1, 2, 3]) == 3

def test_local_does_not_affect_global():
    """Local присвоєння не змінює global."""
    x = "global_value"
    def modify():
        x = "local_value"  # це LOCAL x
        return x
    assert modify() == "local_value"
    assert x == "global_value"  # global не змінився

def test_unbound_local_error():
    """UnboundLocalError коли Python бачить присвоєння."""
    x = 10
    def broken():
        # Python бачить `x = ...` нижче і вважає x local
        # Але ми намагаємось прочитати його ДО присвоєння
        result = x  # UnboundLocalError
        x = 20
        return result

    with pytest.raises(UnboundLocalError):
        broken()