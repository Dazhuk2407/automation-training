"""Приклад 3: __name__ та атрибути модуля. Запуск: pytest example_3_module_attributes.py -v"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mypackage.calc as calc


def current_mode(name):
    # Демонструє логіку __name__ guard як чисту функцію
    return "script" if name == "__main__" else "imported"


def test_current_mode():
    assert current_mode("__main__") == "script"
    assert current_mode("mypackage.calc") == "imported"


def test_module_has_functions():
    # Модуль — це об'єкт з атрибутами-функціями
    assert hasattr(calc, "add")
    assert hasattr(calc, "multiply")


def test_call_via_module():
    assert calc.add(1, 1) == 2
