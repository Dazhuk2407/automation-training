"""Приклад 1: Стилі імпорту. Запуск: pytest example_1_import_styles.py -v"""

# import module
import os
import json

# from module import name
from math import pi, sqrt
from collections import Counter


def test_import_module():
    """import os — використовуємо через os.xxx."""
    assert os.sep in ("/", "\\")


def test_from_import():
    """from math import pi — використовуємо напряму."""
    assert 3.14 < pi < 3.15


def test_json_loads():
    data = json.loads('{"name": "Alice"}')
    assert data["name"] == "Alice"


def test_counter():
    counts = Counter(["a", "b", "a", "c", "a"])
    assert counts["a"] == 3


def test_sqrt():
    assert sqrt(16) == 4.0