"""
Приклад 3: Маркери (коротке знайомство).

Запуск:
    pytest example_3_markers_preview.py -v               → всі 4 тести
    pytest example_3_markers_preview.py -m fast -v        → тільки fast
    pytest example_3_markers_preview.py -m "not slow" -v  → все крім slow
"""

import pytest


@pytest.mark.fast
def test_quick_math():
    """Швидкий тест з маркером fast."""
    assert 2 + 2 == 4


@pytest.mark.fast
def test_quick_string():
    """Ще один швидкий тест."""
    assert "a" in "abc"


@pytest.mark.slow
def test_slow_operation():
    """Повільний тест з маркером slow."""
    import time
    time.sleep(0.1)
    assert True


@pytest.mark.skip(reason="Feature not implemented yet")
def test_not_ready():
    """Цей тест буде пропущений."""
    assert False