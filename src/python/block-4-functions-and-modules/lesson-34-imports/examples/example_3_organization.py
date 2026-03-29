"""Приклад 3: Організація імпортів за PEP 8. Запуск: pytest example_3_organization.py -v"""

# 1. Стандартна бібліотека
import json
import os
from collections import defaultdict

# 2. Сторонні пакети
import pytest


def test_organized_imports():
    """Імпорти організовані за PEP 8."""
    data = json.dumps({"test": True})
    assert isinstance(data, str)


def test_defaultdict():
    """collections.defaultdict."""
    counts = defaultdict(int)
    counts["a"] += 1
    counts["a"] += 1
    counts["b"] += 1
    assert counts["a"] == 2
    assert counts["b"] == 1
    assert counts["c"] == 0  # default = 0


def test_environ_get():
    """os.environ.get з default."""
    value = os.environ.get("NONEXISTENT_VAR", "default")
    assert value == "default"


def test_pytest_approx():
    """pytest як сторонній пакет."""
    assert 0.1 + 0.2 == pytest.approx(0.3)