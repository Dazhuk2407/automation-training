"""
Lesson 7: Example 1 - Marked Tests
Демонстрація маркування тестів
"""
import pytest


@pytest.mark.slow
def test_slow_operation():
    """Тест позначений як slow."""
    import time
    time.sleep(0.1)
    assert True


@pytest.mark.fast
def test_fast_operation():
    """Тест позначений як fast."""
    assert 2 + 2 == 4


@pytest.mark.unit
def test_unit():
    """Unit тест."""
    assert "hello".upper() == "HELLO"


@pytest.mark.integration
def test_integration():
    """Integration тест."""
    # Симуляція integration тесту
    assert True


@pytest.mark.skip(reason="Feature not implemented yet")
def test_not_ready():
    """Тест що буде пропущений."""
    assert False


@pytest.mark.xfail(reason="Known bug in sorting")
def test_expected_fail():
    """Тест що очікується упасти."""
    numbers = [3, 1, 2]
    assert numbers == sorted(numbers)  # Буде fail


@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    """Параметризований тест."""
    assert input ** 2 == expected


# Запустіть:
# pytest -v                    - всі тесты
# pytest -m slow -v            - тільки slow
# pytest -m "not slow" -v      - без slow
# pytest -m unit -v            - тільки unit
# pytest -m integration -v     - тільки integration

