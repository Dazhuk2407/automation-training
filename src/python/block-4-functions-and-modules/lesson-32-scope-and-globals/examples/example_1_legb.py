"""Приклад 1: LEGB правило. Запуск: pytest example_1_legb.py -v"""


GLOBAL_VAR = "global"

def test_local_scope():
    x = "local"
    assert x == "local"

def test_global_scope():
    assert GLOBAL_VAR == "global"

def test_local_shadows_global():
    GLOBAL_VAR = "local_shadow"  # це LOCAL змінна, не global
    assert GLOBAL_VAR == "local_shadow"

def test_global_unchanged():
    """Попередній тест не змінив global."""
    assert GLOBAL_VAR == "global"

def test_builtin_scope():
    assert len([1, 2, 3]) == 3  # len — built-in