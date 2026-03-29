"""
Демонстрація падаючого тесту.

Запустіть і подивіться як pytest показує помилку:
    pytest tests/test_failing_demo.py -v

Це навчальний приклад — в реальному проєкті падаючих тестів бути не повинно.
"""

from src.calculator import add


def test_add_works():
    """Цей тест пройде."""
    assert add(2, 3) == 5


def test_add_intentionally_wrong():
    """Цей тест впаде — неправильне очікуване значення."""
    assert add(2, 3) == 99