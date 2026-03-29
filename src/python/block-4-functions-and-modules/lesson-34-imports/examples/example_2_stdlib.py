"""Приклад 2: Стандартна бібліотека. Запуск: pytest example_2_stdlib.py -v"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path


def test_os_environ():
    """os.environ — змінні оточення."""
    home = os.environ.get("HOME") or os.environ.get("USERPROFILE")
    assert home is not None


def test_json_roundtrip():
    """json.dumps → json.loads."""
    data = {"name": "Alice", "age": 25}
    json_str = json.dumps(data)
    restored = json.loads(json_str)
    assert restored == data


def test_datetime():
    """datetime для роботи з датами."""
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    assert tomorrow > now


def test_pathlib():
    """pathlib — сучасна робота з шляхами."""
    p = Path("/home/user/file.txt")
    assert p.suffix == ".txt"
    assert p.stem == "file"