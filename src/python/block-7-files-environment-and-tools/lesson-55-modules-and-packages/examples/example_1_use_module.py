"""Приклад 1: імпорт власного модуля. Запуск: pytest example_1_use_module.py -v"""
import os
import sys

# Додаємо теку цього файлу в sys.path, щоб import helpers працював звідусіль
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import helpers
from helpers import double


def test_import_module():
    assert helpers.greet("Alice") == "Hello, Alice"


def test_from_import():
    assert double(21) == 42


def test_module_has_name():
    # У імпортованого модуля __name__ дорівнює його імені, не "__main__"
    assert helpers.__name__ == "helpers"
