"""Приклад 2: імпорт із пакета. Запуск: pytest example_2_package_import.py -v"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mypackage.calc import add, multiply
from mypackage import strings
import mypackage


def test_import_from_module():
    assert add(2, 3) == 5
    assert multiply(2, 4) == 8


def test_import_whole_module():
    assert strings.shout("hi") == "HI!"
    assert strings.is_empty("   ") is True


def test_reexport_from_init():
    # __init__.py реекспортує add, тож доступно з пакета напряму
    assert mypackage.add(10, 5) == 15
